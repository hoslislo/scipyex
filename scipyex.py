'''
scipy is a python library used for scientific computing and technical computing.
Some of the modules:
constants: physical constants and conversion factors
integrate: numerical integration routines
'''
import scipy.constants

print "scipy.pi: ", scipy.pi
print "scipy.constants.pi: ", scipy.constants.pi
print "SciPy pi = %.16f" % scipy.constants.pi
print "SciPy pi = %.16f" % scipy.pi

'''
Methods for Integrating Functions given function object:
quad -- General purpose integration
etc.

y = x^2 from x=0 to x=1
'''

from scipy.integrate import quad

def integrand(x):
    return x**2

ans = quad(integrand, 0, 1)
print ans
ans, err = quad(integrand, 0, 1)
print ans
print err

'''
scipy.pi:  3.14159265359
scipy.constants.pi:  3.14159265359
SciPy pi = 3.1415926535897931
SciPy pi = 3.1415926535897931
(0.33333333333333337, 3.700743415417189e-15)
0.333333333333
3.70074341542e-15
'''