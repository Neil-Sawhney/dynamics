
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

#----------------------
T1 = 550
T2 = 3000
T3 = -4000
g = -32.2
F = 2*T1 + T2 + T3
m = T3/g
vf = 4

t = m*vf/F 

print("t = : ", t)

print('#----------------------')
g = -9.81
m = 0.07
I = .5*(0.2)*13+.5*(0.1*8)+0.1*5+0.5*5 + m*g * 0.8
v = I/m
print('v = : ', v)
t = -v/g + .8
print('t = : ', t)

print('#----------------------')
g = -32.2
m = 5.5/16/g
vb = -89*5280/60/60
vHat = -30
deltaX = -6/12

P0 = m*vb
deltaT = deltaX/vHat
F = -P0/deltaT

print("F = : ", F)

print('#----------------------')
m, v0, vf, vHat, deltaX = 0.029, 660, 500, 600, 0.05
vecAB = array([cos(radians(20)), -sin(radians(20))])
vecCD = array([cos(radians(10)), sin(radians(10))])

deltaT = deltaX/vHat
deltaP = m*vf*vecCD - m*v0*vecAB
vecF = deltaP/deltaT
F = magnitude(vecF)
angle = angle(vecF)
print("F in kn = : ", F/1000)
print("angle = : ", angle)

print('#----------------------')
m_A, m_B = 1500, 1200
vecA = array([cos(radians(30)), sin(radians(30))])
vecB = array([0, -1])
vecF = array([cos(radians(10)), sin(radians(10))])
v_A, v_B, v_F = sy.symbols('v_A, v_B, v_F')

deltaP = (m_A*vecF*v_F + m_B*vecF*v_F) - (m_A*vecA*v_A + m_B*vecB*v_B) 

print(sy.solve([deltaP[0],deltaP[1]] , [v_A, v_B]))

print('#----------------------')
v_B = kmPerHrToMPerS(50)
deltaP = (m_A*vecF*v_F + m_B*vecF*v_F) - (m_A*vecA*v_A + m_B*vecB*v_B) 
sol = sy.solve([deltaP[0],deltaP[1]] , [v_A, v_F])
print(mPerSToKmPerH(sol[v_A]))

