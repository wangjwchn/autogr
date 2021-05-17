from z3 import *

class Assn(object):
    
    def __init__(self):
        super(Assn, self).__init__()
        self.assn = True

    def add(self,assn):
        self.assn = And(self.assn, assn)

    def build(self):
        return self.assn
        