
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
def mPerSToFtPerS(m):
    ft = m*3.28084
    return(ft)
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

print("#----------------------")
w_hat = unit(array([0, 0.08-0.18, 0.12*2]))
vec_w = 30*w_hat
vec_r_eb = array([0.12, -0.18,0.12])
vec_v = cross(vec_w, vec_r_eb)
print("v = ", vec_v)
vec_a = cross(vec_w, vec_v)
print("a_c = ",vec_a)

print("#----------------------")
t = sy.symbols("t")
theta_0 = 1.2

theta = theta_0*e**(-7*pi*t/6)*sy.sin(4*pi*t)
print("theta = ", theta.evalf(subs={t:0.125}))
print("angular velocity = ", theta.diff(t).evalf(subs={t:0.125}))
print("angular acceleration = ", theta.diff(t, 2).evalf(subs={t:0.125}))

print("#----------------------")
t = sy.symbols("t")
theta_0 = 1.2

theta = theta_0*e**(-7*pi*t/6)*sy.sin(4*pi*t)
print("theta = ", sy.limit(theta, t, inf))
print("angular velocity = ", sy.limit(theta.diff(t), t, inf))
print("angular acceleration = ", sy.limit(theta.diff(t, 2), t, inf))

print("#----------------------")
r_B, r_A  = 0.03, 0.03
r_E = 0.09
w_E = 155
w_A = 215

v_top = w_E*r_E
w_B = sy.symbols("w_B")
eq = v_top + w_B*2*r_B -w_A*r_A
w_B = sy.solve(eq, w_B)[0]
print("w_B = ",w_B)

print("#----------------------")
v_bot = v_top + w_B*2*r_B
v_cm_B = w_B*r_B + v_bot
w_S = v_cm_B*2*r_A

print("w_S = ", w_S)

print("#----------------------")
