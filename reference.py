import math as m
import sympy as s
import numpy as n

#constants
g = 9.81
G = 6.67 * 10**-11



def ref():
    print("-------------\n\n")
    print("vf = v0 + a*t")
    print("xf = x0 + v0*t + (1/2)a*t^2")
    print("vf^2 = v0^2 + 2a(xf - x0)\n")

ref()

def kmPerHrToMPerS(km):
    m = (km*1000)/60**2
    return(m)


def miPerHrToFtPerS(mi):
    ft = (mi*5280)/60**2
    return(ft)


