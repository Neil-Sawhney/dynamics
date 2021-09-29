
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
g = 32.2 
theta = 40
F_g = 5.1/16
m = F_g/g
v_0 = 165
h = 2

KE_0 = .5*m*v_0**2
maxHeight = sy.symbols('maxHeight')
eq = v_0**2 * sin(radians(theta))**2 + 2*-g*maxHeight
maxHeight = sy.solve(eq, maxHeight)[0]

KE_f = KE_0 +m*g*h - m*g*maxHeight
print("inital KE = ", KE_0)
print("KE at max height = ", KE_f)
print("max height = ", maxHeight)

#---------------
print("#---------------------")
h = - 30*cos(radians(13))
l = 30
v = sqrt(2*g*(h + l))
print("maximum allowable speed", v)
  
#---------------
print("#---------------------")
v = sy.sqrt(2*(.5*14**2 + 0.4*32.2*cos(radians(15))*20-32.2*20*sin(radians(15))))
print("v = ", v)
#---------------
print("#---------------------")
v = miPerHrToFtPerS(20) 
u_k = 0.35
m = 80000 + 100000 + 80000
D = m*v**2/(2*u_k*g*80000)
print("distance required = ", D)
#---------------

print("#---------------------")
T_AB, T_BC = sy.symbols('T_AB T_BC')
eq1 = (T_AB+u_k*80000)*D-.5*80000/g*v**2
F_AB = sy.solve(eq1, T_AB)
eq2 = (-T_BC)*D-.5*80000/g*v**2
F_BC = sy.solve(eq2, T_BC)
print("AB in kips", F_AB[0]/1000)
print("BC in kips: ", F_BC[0]/1000)

print("#---------------------")
E = 60
m_a = 6/g
m_b = 18/g
D = 2
v = sy.symbols("v")
eq1 = .5*m_b*v**2 - E*D + 4*m_a*g + .5*m_a*(v*2)**2
v = sy.solve(eq1, v)
print("velocity = ", v)

print("#---------------------")
d = sy.symbols('d')
eq1 =  m_a*g*2*D - E*d
d = sy.solve(eq1, d)
print("distance = ",d)


print("#---------------------")
g = 9.81
k = 2000
m = 8
d = .05
v = sy.symbols('v')
eq = .5*m*v**2 + .5*k*(d/2)**2 + .5*k*d**2 - m*g*d
vfinal = sy.solve(eq, v)
print("v = ",vfinal)

print("#---------------------")
d = (m*g)/(2*.5*k)
eq = .5*m*v**2 + .5*k*(d/2)**2 + .5*k*d**2 - m*g*d
vfinal = sy.solve(eq, v)
print("v = ",vfinal)
