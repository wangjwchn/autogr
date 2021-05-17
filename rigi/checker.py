from z3 import *
from .utils import *
from .table import *
from .tableIns import *
import copy
import time
from multiprocessing import Manager, Pool, Process, Queue

GenArgv = None
GenState = None

def judge(assn):    
    solver = Solver()
    solver.set("timeout", 5000)
    solver.add(Not(assn))
    result = solver.check()
    if result == unsat:
        return True
    elif result == sat:
        return False
    else:
        return None

def show(b):
    if b == True:
        return ""
    else:
        return "X"

def state_list(state):
    l = []
    for s in list(state.values()):
        l.append(s.data)
    return l

def argv_list(argv):
    l = []
    for a in list(argv.values()):
        l.extend(list(a.values()))
    return l

def new_state(state):
    ns = {}
    for (k,v) in list(state.items()):
        ns[k] = TableInstance(v.table)
        ns[k].data = copy.deepcopy(v.data)
    return ns

def state_axiom(state):
    axiom = True
    for s in list(state.values()):
        axiom = And(axiom,s.axiom)
    return axiom

def ASSN_COMMUTE(g1,c1,f1,g2,c2,f2,A,GS,GA):
    stateA = GS()
    argvA = GA()
    stateB = GS()
    argvB = GA()
    state = GS()
    return ForAll(state_list(stateA)+argv_list(argvA)+state_list(stateB)+argv_list(argvB)+state_list(state),
                Implies(And(
                    state_axiom(stateA), state_axiom(stateB), state_axiom(state),
                    c1(new_state(state),argvA), c1(f2(new_state(state),argvB),argvA),
                    c2(new_state(state),argvB), c2(f1(new_state(state),argvA),argvB),
                    A(argvA,argvB), g1(new_state(stateA),argvA),g2(new_state(stateB),argvB))
                ,state_eq(f2(f1(new_state(state),argvA),argvB),
                           f1(f2(new_state(state),argvB),argvA))))

def ASSN_DIS(g1,c1,f1,g2,c2,f2,A,GS,GA):
    state = GS()
    state_ = GS()
    argvA = GA()
    argvB = GA()
    return ForAll(argv_list(argvA)+argv_list(argvB)+state_list(state), 
        Implies(And(state_axiom(state),state_axiom(state_),A(argvA,argvB),g1(new_state(state_),argvA),c1(new_state(state),argvA)),
        Implies(g2(new_state(state),argvB),g2(f1(new_state(state),argvA),argvB))))

def proc_check(queue, cls, op1_index, op2_index, sop1_index, sop2_index):
    app = cls()
    op2 = app.ops[op2_index]
    op1 = app.ops[op1_index]
    g1,c1,f1 = op1.sops[sop1_index]
    g2,c2,f2 = op2.sops[sop2_index]
    success1 = judge(ASSN_COMMUTE(g1,c1,f1,g2,c2,f2,app.axiom,app.state,app.argv)) 
    success2 = judge(ASSN_DIS(g1,c1,f1,g2,c2,f2,app.axiom,app.state,app.argv)) \
           and judge(ASSN_DIS(g2,c2,f2,g1,c1,f1,app.axiom,app.state,app.argv))    
    queue.put((op1.__class__.__name__,op2.__class__.__name__,sop1_index,sop2_index,success1,success2))

def proc_show(signal, queue, cls):
    app = cls()
    non_commute = 0
    semantic_va = 0
    exist = 0
    n_workers = signal.get(True)

    L = str(max([len(op.__class__.__name__) for op in app.ops]) + 2)
    print('   '+ '-'*106)
    print("  |{:^31s}|{:^6s}|{:^30s}|{:^7s}|{:^9s}|{:^10s}|{:^7s}|".format("OPERATION", "PATH", "OPERATION\'", "PATH\'", "COMMUTE", "SEMANTIC", "EXIST"))

    while True:
        time.sleep(0.05)
        try:
            name1, name2, index1, index2, success1, success2 = queue.get(False)
            n_workers -= 1
            print('   '+ '-'*106)
            print("  |{:^31}|{:^6s}|{:^30s}|{:^6s}".format(name2,"No."+str(index2),name1,"No."+str(index1)), end=' ')
            if success1 != True:
                non_commute = non_commute + 1
            print("|{:^8s}".format(show(success1)), end=' ')
            if success2 != True:
                semantic_va = semantic_va + 1
            print("|{:^9s}".format(show(success2)), end=' ')
            if success1 != True or success2 != True:
                exist = exist + 1
            print("|{:^7s}|".format(show(success1 and success2)))
            if n_workers == 0:
                break
        except:
            pass

    print('   '+ '-'*106)
    print("  |{:^77s}|{:^9s}|{:^10s}|{:^7s}|".format("TOTAL RESTRICTIONS",str(non_commute),str(semantic_va),str(exist)))
    print('   '+ '-'*106)
            
        

def check_parallel(cls, nthread):
    p = Manager().Queue()
    q = Manager().Queue()
    pool = Pool(nthread)
    p_show = pool.apply_async(proc_show,(p,q,cls))
    app = cls()
    n_workers = 0
    for i in range(len(app.ops)):
        for j in range(i,len(app.ops)):
            for m in range(len(app.ops[j].sops)):
                for n in range(0 if i != j else m,len(app.ops[i].sops)):
                    pool.apply_async(proc_check, (q,cls,j,i,m,n))
                    n_workers += 1
    p.put(n_workers)
    pool.close()
    pool.join()
   


def check(app):
    non_commute = 0
    semantic_va = 0
    exist = 0

    L = str(max([len(op.__class__.__name__) for op in app.ops]) + 2)
    print('   '+ '-'*106)
    print("  |{:^31s}|{:^6s}|{:^30s}|{:^7s}|{:^9s}|{:^10s}|{:^7s}|".format("OPERATION", "PATH", "OPERATION\'", "PATH\'", "COMMUTE", "SEMANTIC", "EXIST"))
    for i in range(len(app.ops)):
        op2 = app.ops[i]
        for j in range(i,len(app.ops)):
            op1 = app.ops[j]
            for m in range(len(op1.sops)):
                g1,c1,f1 = op1.sops[m]
                for n in range(0 if i != j else m,len(op2.sops)):
                    g2,c2,f2 = op2.sops[n]
                    print('   '+ '-'*106)
                    print("  |{:^31}|{:^6s}|{:^30s}|{:^6s}".format(op2.__class__.__name__,"No."+str(n),op1.__class__.__name__,"No."+str(m)), end=' ')
                    success1 = judge(ASSN_COMMUTE(g1,c1,f1,g2,c2,f2,app.axiom,app.state,app.argv)) 
                    if success1 != True:
                        non_commute = non_commute + 1
                    print("|{:^8s}".format(show(success1)), end=' ')
                    success2 = judge(ASSN_DIS(g1,c1,f1,g2,c2,f2,app.axiom,app.state,app.argv)) and judge(ASSN_DIS(g2,c2,f2,g1,c1,f1,app.axiom,app.state,app.argv))
                    if success2 != True:
                        semantic_va = semantic_va + 1
                    print("|{:^9s}".format(show(success2)), end=' ')
                    if success1 != True or success2 != True:
                        exist = exist + 1
                    print("|{:^7s}|".format(show(success1 and success2)))
    print('   '+ '-'*106)
    print("  |{:^77s}|{:^9s}|{:^10s}|{:^7s}|".format("TOTAL RESTRICTIONS",str(non_commute),str(semantic_va),str(exist)))
    print('   '+ '-'*106)


