
import math as math
import sympy as sy
from numpy import *

#constants
g = 9.80665
G = 6.67 * 10**-11

def ref():
    print("-------------\n\n")
    print("vf = v0 + a*t")
    print("xf = x0 + v0*t + (1/2)a*t^2")
    print("vf^2 = v0^2 + 2a(xf - x0)\n")
#ref()
def kmPerHrToMPerS(km):
    m = (km*1000)/60**2
    return(m)
def mPerSToKmPerH(m):
    km = (m/1000)*60**2
    return(km)
def miPerHrToFtPerS(mi):
    ft = (mi*5280)/60**2
    return(ft)

def mToFt(m):
   return(m * 3.280839895)

def ftToM(m):
   return(m / 3.280839895)

def arrToDegrees(arr):
    new = [0] * len(arr)
    for x in range(len(arr)):
        new[x] = math.degrees(arr[x])
    return new
def unit(arr): 
    temp = 0
    for x in arr:
        temp = temp + x**2
    return arr/sy.sqrt(temp)
def magnitude(arr):
    temp = 0
    for x in arr:
        temp = temp + x**2
    return sy.sqrt(temp)
def angle(arr):
    return degrees(math.atan(arr[1]/arr[0]))

#----------------------
theta = sy.symbols('theta')
r = 0.85
m = 0.25
w = 7.5
F_g = m*g

eq1 = g/(w**2*r)-sy.cos(theta) 
answer = sy.solve(eq1, theta)
print("theta = ", arrToDegrees( answer))

#----------------------
print('##')
#----------------------
m = 0.35
w = 7.5
F_g = m*g
r = 0.5
U_s = 0.25
U_k = 0.2
theta = 75 

F_fx, F_fy = sy.symbols('F_fx'), sy.symbols('F_fy')
#F_N = m*w**2*r - m*g*sin(radians(theta))

vecF_g = array([0, -m*g])
vecF_c = array([-m*w**2*r*sy.sin(radians(theta)),0])
vecF_N = vecF_c - vecF_g
F_fMax = U_s * magnitude(vecF_N)

#orth = sy.symbols('orth')
#eq = vecF_N[0] + vecF_N[1]*orth
#orth = sy.solve(eq, orth)[0]

#vecF_f = array([F_fx, F_fy]) * unit(array([1, orth]))

vecF_f = vecF_N + vecF_g
#eq =  vecF_N + vecF_f + vecF_g

#F_fx = sy.solve(eq[0], F_fx)[0]
#F_fy = sy.solve(eq[1], F_fy)[0]
#F_f = magnitude(array([F_fx, F_fy]))

F_f = magnitude(vecF_f)

#vecF_f = F_f *  unit(array([1, orth]))
print("angle = ", angle(vecF_f))

if (F_f < F_fMax):
    print("collar stays, F_f = ", F_f)

else:
    F_f = U_k *  magnitude(vecF_N)
    print("collar falls, F_f = ", F_f)

