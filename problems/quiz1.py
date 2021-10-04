
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

g,m,y,x,t = 9.81, 0.087, 0.21, 0.57, 0.87
theta = arctan(y/x)

us, uk = sy.symbols('us mk')
eq = us*m*g*cos(theta) - m*g*sin(theta)
us = sy.solve(eq, us)
print('us = : ', us)

a = 2*-sqrt(x**2+y**2)/t**2
print('a = : ', a)

eq=uk*m*g*cos(theta)-m*g*sin(theta)-m*a
uk = sy.solve(eq, uk)
print('uk = : ', uk)

print("#-------------------------------")
m,theta,k,deltax,g = 0.01, radians(6.5), 1.2, 0.15, 9.81
v = sy.symbols('v')
eq = m*g*(0.5+0.15)*sin(theta)+.5*m*v**2 - .5*k*deltax**2
v = sy.solve(eq, v)
print('v = : ', v)
a,v0,deltax = -g*sin(theta),v[0],-0.5
t = sy.symbols('t')
eq = -deltax + v0*t+.5*a*t**2
t = sy.solve(eq, t)
print('t = : ', t)
r,deltax = 0.25,-0.15
v = sy.symbols('v')
eq = m*g*(0.5+0.15+0.25)*sin(theta)+.5*m*v**2 - .5*k*deltax**2
v = sy.solve(eq, v)[0]
fc = m*v**2/r
N = fc - m*g*sin(theta)
print('N = : ', N)
