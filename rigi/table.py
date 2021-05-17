from z3 import *
from . import *
from .enum import *
from .axioms import *
from .utils import *

class Table(object):
    Type = Enum(["INT","STRING","REAL","BOOL"])

    def __init__(self, name):
        super(Table, self).__init__()
        self.name = name

        # key: attribute name
        # value: z3 type
        self.attrs = {}

        # primary keys list
        self.pkeys = []

        # --- after build ------
        # key: primary key constructor
        # value: z3 type of the primary key
        # self.key_type_dict = {}

        # key: primary key constructor
        # value: primary keys name list
        # self.key_name_dict = {}

        # if we have mutiple primary key, then we have non-empty axiom
        self.axiom = AxiomEmpty()

        # the z3 type of all primary keys
        self.key_type = None

        # the z3 type of all fileds
        self.value_type = None

        # value: filed name list
        # self.attrs_name = None

    def addAttr(self, attr_name, attr_type):
        self.attrs[attr_name] = self.__toZ3Type(attr_type)

    def setPKey(self, *pkey_name_list):
        self.pkeys.append(pkey_name_list)

    def build(self):
        if len(self.pkeys) == 0:
            self.pkeys.append(list(sorted(self.attrs.keys())))
        self.key_type = Datatype('T_KEY_'+self.name)
        for pk in self.pkeys:
            pk = list(pk) # single primary key list
            kid = TUID(pk)
            attrs_only_key = []
            for k in sorted(pk):
                attrs_only_key.append((k,self.attrs[k]))
            self.key_type.declare(kid,*attrs_only_key)
        self.key_type = self.key_type.create()

        self.value_type = Datatype('T_VALUE_'+self.name)
        self.value_type.declare('new',*list(sorted(self.attrs.items())))
        self.value_type.declare('nil')
        self.value_type = self.value_type.create()


    def keyInstance(self,pkey_name_list):
        pkey_dict = {}
        for pkey_name in sorted(pkey_name_list):
            typ = self.attrs[pkey_name]
            if typ == IntSort():
                pkey_dict[pkey_name] = Int(ID(pkey_name))
            elif typ == StringSort():
                pkey_dict[pkey_name] = String(ID(pkey_name))
            elif typ == DoubleType:
                pkey_dict[pkey_name] = Real(ID(pkey_name))
            elif typ == BoolSort():
                pkey_dict[pkey_name] = Bool(ID(pkey_name))
            else:
                raise TypeError(" invalid type")
        return pkey_dict

    def __toZ3Type(self,typ):
        if typ == Table.Type.INT:
            return IntSort()
        elif typ == Table.Type.STRING:
            return StringSort()
        elif typ == Table.Type.REAL:
            return DoubleType
        elif typ == Table.Type.BOOL:
            return BoolSort()
        else:
            raise TypeError(" invalid type")
