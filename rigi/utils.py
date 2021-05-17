from z3 import *
from .checker import *
from .axioms import *
from copy import deepcopy
import time

def ID(name ,total = []):
    m = 0
    if total:
        m = total[-1]
    total.append(m + 1)
    return name + str(total[-1])

def gen_id(total = []):
    m = 0
    if total:
        m = total[-1]
    total.append(m + 1)
    return str(total[-1])

def Implies2(P,Q):
    return And(Implies(P,Q),Implies(Q,P))

def z3_list_eq(X,Y):
    X_eq_Y = [ X[i] == Y[i] for i in range(len(X)) ]
    return simplify(And(X_eq_Y))

def state_eq(X,Y):
    X_eq_Y = [ (X[i].data == Y[i].data) for i in list(X.keys())]
    return And(X_eq_Y)

def z3_dict_eq(X,Y):
    X_eq_Y = [ X[i] == Y[i] for i in list(X.keys())]
    return And(X_eq_Y)

def TUID(l):
    l_ = deepcopy(l)
    l_.sort()
    return '_' + ''.join(l_)

def RelEqual():
    return lambda x,y: x == y

def RelNotEqual():
    return lambda x,y: x != y

def RelLessOrEqual():
    return lambda x,y: x <= y

def RelLess():
    return lambda x,y: x < y

