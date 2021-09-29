
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

vecF_c = array([m*w**2*r*sy.sin(radians(theta)),0])
vecF_g = array([0, -m*g])

unitF_N = array([-sin(radians(theta)), cos(radians(theta))])
F_N = -(dot(unitF_N, vecF_g) + dot(unitF_N, vecF_c))
vecF_N = F_N * unitF_N

vecF_f = vecF_c + vecF_g + vecF_N

F_fMax = U_s * magnitude(vecF_N)

F_f = magnitude(vecF_f)

print("angle = ", angle(vecF_f))

if (F_f < F_fMax):
    print("collar stays, F_f = ", F_f)

else:
    F_f = U_k *  magnitude(vecF_N)
    print("collar falls, F_f = ", F_f)

#----------------------
print('##')
#----------------------
m = 0.35
w = 7.5
F_g = m*g
r = 0.5
U_s = 0.25
U_k = 0.2
theta = 40 

vecF_c = array([m*w**2*r*sy.sin(radians(theta)),0])
vecF_g = array([0, -m*g])

unitF_N = array([-sin(radians(theta)), cos(radians(theta))])
F_N = -(dot(unitF_N, vecF_g) + dot(unitF_N, vecF_c))
vecF_N = F_N * unitF_N

vecF_f = vecF_c + vecF_g + vecF_N

F_fMax = U_s * magnitude(vecF_N)

F_f = magnitude(vecF_f)

print("angle = ", angle(vecF_f))

if (F_f < F_fMax):
    print("collar stays, F_f = ", F_f)

else:
    F_f = U_k *  magnitude(vecF_N)
    print("collar falls, F_f = ", F_f)

#--------------------------
print("##")
h = 980 * 10**3
M = 4.87*10**24
r_v = 6052 * 10**3

r_a = r_v + h
v_a = sqrt(2*G*M/r_a)
print("v_a = : ", v_a)

v_c = 1/sqrt(2)*v_a
print("delta v", v_c - v_a)
