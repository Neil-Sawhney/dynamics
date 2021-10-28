
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
w_E = -155
w_A = -215


v_top = w_E*r_E
w_B = sy.symbols("w_B")
eq = -v_top + w_B*2*r_B +w_A*r_A
w_B = sy.solve(eq, w_B)[0]
print("w_B = ",w_B)

print("#----------------------")
v_cm_B = w_A*r_A + w_B*r_B 
w_S = v_cm_B/(2*r_A)

print("w_S = ", w_S)

print("#----------------------")
vecv_D = array([8,0,0])
vecr_A_D = array([0,5,0])
r_D = 6

vecw_D = array([0,0,-magnitude(vecv_D/r_D)])
vecv_A = vecv_D + cross(vecw_D, vecr_A_D)

vecr_B_A = array([sqrt(14**2 - 5**2),-5,0])
vecr_B_Q = array([-4,6,0])
vecv_Q = array([0,0,0])

w_E, w_AB = sy.symbols("w_E w_AB")
vecw_E = array([0,0,w_E]) #this assumes clockwise
vecw_AB = array([0,0,w_AB]) #this assumes clockwise

eq1 = vecv_A + cross(vecw_AB, vecr_B_A)
eq2 = vecv_Q + cross(vecw_E, vecr_B_Q)
eq = eq1 - eq2 
solution = sy.solve(eq)

vecw_AB = array([0,0,solution[w_AB]])
vecw_E = array([0,0,solution[w_E]])

vecr_E_Q = array([0,6,0])
vecv_E = vecv_Q + cross(vecw_E,vecr_E_Q)
print(solution)
print("v_E =", vecv_E)

print("#----------------------")
theta = radians(25)
g = 32.2
m = 5500/g

a = (3040 - 5500*cos(theta))/m
print("a = ", a)
F = m*a
vecF = sy.Matrix([0,-F,0])
vecF_G = 5500*sy.Matrix([-sin(theta), -cos(theta), 0])
vecT=sy.Matrix([0,3040,0])
RA, RB = sy.symbols("RA RB")
vecRA = sy.Matrix([RA, 0 ,0])
vecRB = sy.Matrix([RB, 0 ,0])

M_a = sy.Matrix([30/12, 25/12, 0]).cross(vecF_G) + sy.Matrix([0, 50/12, 0]).cross(vecRB) + sy.Matrix([24/12, 50/12, 0]).cross(vecT) - sy.Matrix([30/12, 25/12, 0/12]).cross(vecF) 

RB = sy.solve(M_a)[RB]

print("RB= ", RB)
vecRB = sy.Matrix([-RB, 0 ,0])
eq = vecRB + vecRA + vecF_G + vecT - vecF
RA = sy.solve(eq[0])
print("RA= ",  RA)

print("#----------------------")
g = 9.81
l = 1.14 
m = 5.2
p = 75
F = -m*g
I_G = 1/12*m*l**2
r = sy.symbols("r")
r = sy.solve(p/(m*r) - p*l/(2*I_G))
print("r = ", r)
print("alpha = ", p*l/(2*I_G))

print("#----------------------")
w=12
alpha = 37
m_d = 3
m_r = 4
g = 9.8
L = 0.48
r = 0.12
I_RA = (m_r*L**2)/12 + m_r*0.12**2
I_D = 1/2*m_d*r**2
I_T = I_D + I_RA
P = (I_T*alpha + 0.12*4*g)/0.12
print("P = ", P)
m = m_d+m_r
com = (m_r*0.12)/m
F_c = m*com*w**2
R_x = -F_c
F_y = -I_T*alpha/com
R_y = P + 3*g + 4*g + m_r*r*alpha

print("R_x = ",R_x )
print("R_y = ",R_y )
