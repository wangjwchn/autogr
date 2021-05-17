from z3 import *
from .enum import *
from .utils import *

class ArgvBuilder(object):
    
    Type = Enum(["INT","STRING","REAL","BOOL"])

    def __init__(self):
        super(ArgvBuilder, self).__init__()
        self.op = None
        self.argv = {}
        self.data = {}

    def __save(self):
    	if self.op != None:
    	    self.data[self.op] = self.argv
    	    self.op = None
    	    self.argv = {}


    def NewOp(self, name):
    	self.__save()
    	self.op = name

    def AddArgv(self, name, typ):
        if typ == ArgvBuilder.Type.INT:
            self.argv[name] = Int(ID(name))
        elif typ == ArgvBuilder.Type.STRING:
            self.argv[name] = String(ID(name))
        elif typ == ArgvBuilder.Type.REAL:
            self.argv[name] = Real(ID(name))
        elif typ == ArgvBuilder.Type.BOOL:
            self.argv[name] = Bool(ID(name))
        else:
            raise TypeError(" invalid type")
    	
    def Build(self):
    	self.__save()
    	return self.data












