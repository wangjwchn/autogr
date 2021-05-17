# False: use inexact machine representation of real numbers
use_exact_real_numbers = True

from z3 import RealSort, FPSort, Real, FP

if use_exact_real_numbers:
    DoubleType = RealSort()
    Double = Real
else:
    DoubleType = FPSort(11, 53)
    Double = lambda name: FP(name, DoubleType)
