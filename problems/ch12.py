
import math as m
import sympy as s
from numpy import *

#constants
g = 9.80665
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


#----------------------
w = 5480
T = 5000
alpha = 25
m = w/mToFt(g)
t = 20

a = (-T + w*cos(radians(25)))/m
print('a:', a)
D = .5*a*t**2
print('D:', D)
vf = -sqrt(2*a*D)
#string breaks
v0 = 0
T = 0
a = (-T + w*cos(radians(25)))/m
t = s.symbols('t')
D = -D
eq = v0*t + .5*a*t**2 - D
print('t:', s.solve(eq,t))

#-------------------
print("both-wheel")
v0= 0 
D = 74
m = s.symbols('m')
w = m*g

u_s = 0.8
N_front = 0.6*w
N_rear = 0.4*w

F_friction_front = -u_s * N_front
F_friction_rear = -u_s * N_rear

a = F_friction_front/m
vf = s.symbols('vf')
eq = .5*m*vf**2 + F_friction_front*D + F_friction_rear*D

maxSpeed = s.solve(eq, vf)
print('max speed:' , mPerSToKmPerH(maxSpeed[1]))
#---------------------
print("front-wheel")
v0= 0 
D = 74
m = s.symbols('m')
w = m*g

u_s = 0.8
N_front = 0.6*w
N_rear = 0.4*w

F_friction_front = -u_s * N_front
F_friction_rear = -u_s * N_rear

a = F_friction_front/m
vf = s.symbols('vf')
eq = .5*m*vf**2 + F_friction_front*D

maxSpeed = s.solve(eq, vf)
print('max speed:' , mPerSToKmPerH(maxSpeed[1]))
#---------------------
print("rear-wheel")
v0= 0 
D = 74
m = s.symbols('m')
w = m*g

u_s = 0.8
N_front = 0.6*w
N_rear = 0.4*w

F_friction_front = -u_s * N_front
F_friction_rear = -u_s * N_rear

a = F_friction_front/m
vf = s.symbols('vf')
eq = .5*m*vf**2 + F_friction_rear*D

maxSpeed = s.solve(eq, vf)
print('max speed:' , mPerSToKmPerH(maxSpeed[1]))
#--------------------
r = 0.155
m = 0.5

v = s.symbols('v')
T1 = 75
T2 = 75
T1x = T1*sin(radians(20))
T2x = T2*sin(radians(30))
Fc = T1x+T2x
eq = v**2/r*m - Fc
vmax = s.solve(eq, v)
print('max v', vmax[1])
T2 = 75
T1 = s.symbols('T1')
eq = T1*cos(radians(20)) - T2*cos(degrees(30))-m*g
T1Solve = s.solve(eq, T1)
print('T2 is maxed, T1 =', T1Solve)
T1 = 75
T2 = s.symbols('T2')
eq = T1*cos(radians(20)) - T2*cos(degrees(30))-m*g
T2Solve = s.solve(eq, T2)
print('T1 is maxed, T2 =', T2Solve)
T2 = T2Solve[0]
T1 = 75
T1x = T1*sin(radians(20))
T2x = T2*sin(radians(30))
Fc = T1x+T2x
T2 = 0
T1 = m/cos(radians(20))
eq = g*r/m*T1*sin(radians(20)) - v**2
vmin = s.solve(eq, v)
print('min v', vmin[1])
#------------------------
m = 60
r = 1200
v0 = kmPerHrToMPerS(550)
vf = 0
wf = 0
w0 = v0/r

a = s.symbols('a')
alpha= a/r
theta = pi


eq = -wf**2 + w0**2 + 2*alpha*theta
a = s.solve(eq, a)
print('acceleration', a)

