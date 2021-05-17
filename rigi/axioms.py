from z3 import *

def __Unique(idA,idB):
    return idA != idB

def __TimeStamp(tA,tB):
    return tA != tB

def AxiomUniqueArgument(opname,arg):
    def Axiom(argvA,argvB):
        A = argvA[opname][arg]
        B = argvB[opname][arg]
        return And(__Unique(A,B))
    return Axiom

def AxiomUniqueArguments(opname,args):
    def Axiom(argvA,argvB):
        P = False
        for arg in args:
            A = argvA[opname][arg]
            B = argvB[opname][arg]
            P = Or(P, __Unique(A,B))
        return P
    return Axiom

def AxiomTimeStamp(opname,arg):
    def Axiom(argvA,argvB):
        A = argvA[opname][arg]
        B = argvB[opname][arg]
        return And(__TimeStamp(A,B))
    return Axiom

def BuildArgvAxiom(op_list):
    return AxiomsAnd(*list([x.axiom for x in op_list]))

def AxiomRemoveWin(op1,argv_list1,op2,argv_list2):
    def Axiom(argvA,argvB):
        P1 = False
        for argv1,argv2 in zip(argv_list1,argv_list2):
            A = argvA[op1][argv1]
            B = argvB[op2][argv2]
            P1 = Or(P1, __Unique(A,B))
        P2 = False
        for argv1,argv2 in zip(argv_list1,argv_list2):
            A = argvB[op1][argv1]
            B = argvA[op2][argv2]
            P2 = Or(P2, __Unique(A,B))
        return And(P1,P2)
    return Axiom

def AxiomCausal(op1,argv_list1,op2,argv_list2):
    def Axiom(argvA,argvB):
        P1 = False
        for argv1,argv2 in zip(argv_list1,argv_list2):
            A = argvA[op1][argv1]
            B = argvB[op2][argv2]
            P1 = Or(P1, __Unique(A,B))
        P2 = False
        for argv1,argv2 in zip(argv_list1,argv_list2):
            A = argvB[op1][argv1]
            B = argvA[op2][argv2]
            P2 = Or(P2, __Unique(A,B))
        return And(P1,P2)
    return Axiom

def AxiomsAnd(*axioms):
    def Axiom(argvA,argvB):
        P = True
        for axiom in axioms:
            P = And(P,axiom(argvA,argvB))
        return P
    return Axiom

def AxiomAnd(axiom1,axiom2):
    def Axiom(argvA,argvB):
        return And(axiom1(argvA,argvB),axiom2(argvA,argvB))
    return Axiom

def AxiomEmpty():
    def Axiom(argvA,argvB):
        return True
    return Axiom