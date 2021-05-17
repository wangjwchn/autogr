from z3 import *
from .enum import *
from .table import *
from .utils import *
from .assn import *

class TableInstance(object):

    def __init__(self, table):
        super(TableInstance, self).__init__()
        self.table = table
        self.name = table.name
        self.key_type = table.key_type
        self.value_type = table.value_type
        self.data = Array(ID('TABLE_' + table.name), self.key_type, self.value_type)
        self.attr_list = list([k_v1[0] for k_v1 in sorted(table.attrs.items())])
        self.axiom = self.__initAxiom()

    def __initAxiom(self):
        A = Assn()

        # forall k1 k1' K1, (k1:K1 /\ k1':K1 /\ k1 != k1' /\ Table[k1] != Table[k1']) => (exists k2 K2, (k2:K2) => Table[k1].K2 != Table[k1'].K2)
        for pkey1 in self.table.pkeys:
            ins1 = self.table.keyInstance(pkey1)
            ins2 = self.table.keyInstance(pkey1)
            for pkey2 in self.table.pkeys:
                F = False
                for k in pkey2:
                    F = Or(F, self.get(ins1,k) != self.get(ins2,k))
            A.add(ForAll(list(ins1.values()) + list(ins2.values()),Implies(Not(z3_list_eq(list(ins1.values()),list(ins2.values()))),F)))
        
        # forall k1 k2 K1 K2, (k1:K1 /\ k2:K2 /\ K1 != K2 /\ Table[k1].K2 == k2 /\ Table[k2].K1 == k1) => (Table[k1] == Table[k2])
        for i in range(len(list(self.table.pkeys))):
            for j in range(i + 1,len(list(self.table.pkeys))):
                pk1 = list(self.table.pkeys)[i]
                pk2 = list(self.table.pkeys)[j]
                if pk1 != pk2:
                    ins1 = self.table.keyInstance(pk1)
                    ins2 = self.table.keyInstance(pk2)
                    R = True
                    P = True
                    for k in pk1:
                        P = And(P, self.get(ins2,k) == ins1[k])
                    for k in pk2:
                        P = And(P, self.get(ins1,k) == ins2[k])
                    Q = self.get(ins1) == self.get(ins2)
                    A.add(ForAll(list(ins1.values())+ list(ins2.values()),And(R,Implies(P,Q))))

        #####  Note: The following two axioms are fixed in the add function
        # forall k1 K1 K2, (k1:K1 /\ K1 != K2) => Table[Table[k1].K2] not nil
        # for i in range(len(list(self.table.pkeys))):
        #     for j in range(i + 1,len(list(self.table.pkeys))):
        #         pk1 = list(self.table.pkeys)[i]
        #         pk2 = list(self.table.pkeys)[j]
        #         if pk1 != pk2:
        #             ins1 = self.table.keyInstance(pk1)
        #             ins2 = self.table.keyInstance(pk2)  
        #             ins2by1 = dict(zip(pk2, [self.get(ins1, k2) for k2,_ in ins2.items()]))    
        #             A.add(ForAll(list(ins1.values()) + list(ins2.values()),And(self.notNil(ins2by1))))

        # forall k1 k1' K1 K2, (k1:K1 /\ k1':K1 /\ k1 != k1' /\ K1 != K2) => Table[k1].K2 != Table[k1'].K2
        # for i in range(len(list(self.table.pkeys))):
        #     for j in range(i + 1,len(list(self.table.pkeys))):
        #         pk1 = list(self.table.pkeys)[i]
        #         pk2 = list(self.table.pkeys)[j]
        #         if pk1 != pk2:
        #             ins1 = self.table.keyInstance(pk1)
        #             ins1_ = self.table.keyInstance(pk1)
        #             ins2 = self.table.keyInstance(pk2) 
        #             ins2by1 = dict(zip(pk2, [self.get(ins1, k2) for k2,_ in ins2.items()]))
        #             ins2by1_ = dict(zip(pk2, [self.get(ins1_, k2) for k2,_ in ins2.items()]))
        #             A.add(ForAll(list(ins1.values()) + list(ins1_.values()) + list(ins2.values()),
        #                 Implies(list(ins1.values())[0] != list(ins1_.values())[0], list(ins2by1.values())[0] != list(ins2by1_.values())[0])))
        
        return A.build()


    def __makeKey(self,key_dict):
        return self.key_type.__dict__[TUID(list(key_dict.keys()))](*list([k_v[1] for k_v in sorted(key_dict.items())]))

    def __makeValue(self,key_dict,value_dict):
        return self.value_type.new(*list([value_dict[attr_name] if attr_name in value_dict else self.get(key_dict,attr_name) for attr_name in self.attr_list]))

    def __isKey(self,key_dict):
        for pkey in list(self.table.pkeys):
            if set(pkey) >= set(key_dict.keys()):
                return True
        return False

    def notNil(self, key_dict):
        return Not(self.Nil(key_dict))

    def Nil(self, key_dict):
        if self.__isKey(key_dict):
            return self.get(key_dict) == self.value_type.nil
        else:
            key_list = self.__makeIncompleteKeys(key_dict)
            if key_list != []:
                A = Assn()
                # print key_list
                for key_ins in key_list:
                    P = Assn()
                    for key_name in key_dict:
                        if key_name in key_ins:
                            P.add(key_ins[key_name] == key_dict[key_name])
                    Q = Assn()
                    Q.add(self.get(key_ins) == self.value_type.nil)
                    A.add(ForAll(list(key_ins.values()),Implies(P.build(),Q.build())))
                return A.build()
            else:
                return self.XyRel(key_dict, self.value_type.nil, None, RelEqual())

    def delete(self, key_dict):
        z3id = self.__makeKey(key_dict)
        for pkey in list(self.table.pkeys):
            if set(pkey) != set(key_dict.keys()):
                pkey_dict = {}
                for k in pkey:
                    pkey_dict[k] = self.get(key_dict,k)
                z3id = self.__makeKey(pkey_dict)
                self.data = Store(self.data, z3id, self.value_type.nil)
        self.data = Store(self.data, z3id, self.value_type.nil)

    def get(self, key_dict, value_name = None):
        z3id = self.__makeKey(key_dict)
        values = Select(self.data, z3id)
        if value_name == None:
            return values
        else:
            return self.value_type.__dict__[value_name](values)

    def add(self, key_dict, value_dict):
        z3id = self.__makeKey(key_dict)
        value_dict.update(key_dict)
        z3value = self.__makeValue(key_dict,value_dict)
        self.data = Store(self.data, z3id, z3value)
        for pkey in list(self.table.pkeys):
            if set(pkey) != set(key_dict.keys()) \
               and (set(pkey) & set(value_dict.keys())): # update the data if it is indeed updated
                # print(set(pkey), value_dict)
                pkey_dict = {}
                for k in pkey:
                    pkey_dict[k] = self.get(key_dict,k)
                z3id = self.__makeKey(pkey_dict)
                self.data = Store(self.data, z3id, z3value)

    def update(self, key_dict, value_dict):
        z3id = self.__makeKey(key_dict)
        if value_dict == None:
            self.delete(key_dict)
        else:
            self.add(key_dict, value_dict)

    def __makeIncompleteKey(self, key_dict):
        # find a key
        for pkey in list(self.table.pkeys):
            if set(pkey) >= set(key_dict.keys()):
                ins = self.table.keyInstance(pkey)
                return ins
        return None

    def __makeIncompleteKeys(self, key_dict):
        # find a key
        key_list = []
        for pkey in list(self.table.pkeys):
            if set(pkey) >= set(key_dict.keys()):
                key_list.append(self.table.keyInstance(pkey))
        return key_list

    def XYRel(self, X_dict, Y_dict, name, R):
        key_list_x = self.__makeIncompleteKeys({})
        key_list_y = self.__makeIncompleteKeys({})
        A = Assn()
        for key_ins_x,key_ins_y in zip(key_list_x,key_list_y):
            P1 = Assn()
            for X_name, X_value in list(X_dict.items()):
                P1.add(self.get(key_ins_x,X_name) == X_value)
            P2 = Assn()
            for Y_name, Y_value in list(Y_dict.items()):
                P2.add(self.get(key_ins_y,Y_name) == Y_value)
            Q = Assn()
            Q.add(R(self.get(key_ins_x,name),self.get(key_ins_y,name)))
            A.add(ForAll(list(key_ins_x.values()) + list(key_ins_y.values()),Implies(And(P1.build(),P2.build()),Q.build())))
        return A.build()

    def XyRel(self, X_dict, Y, name, R):
        key_list_x = self.__makeIncompleteKeys({})
        A = Assn()
        for key_ins_x in key_list_x:
            P = Assn()
            for X_name, X_value in list(X_dict.items()):
                P.add(self.get(key_ins_x,X_name) == X_value)
            Q = Assn()
            Q.add(R(self.get(key_ins_x,name),Y))
            A.add(ForAll(list(key_ins_x.values()),Implies(P.build(),Q.build())))
        return A.build()
