
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
rho = 7850
ybar = 4*0.024/(3*pi)
m1 = rho*0.08*0.16*0.05
m2 = rho*0.08*0.07*0.038
m3 = rho*pi/2*0.024**2*0.04

I_1x = m1*(1/12*(0.05**2 + 0.16**2)+((0.16/2)**2 + (0.05/2)**2))
I_2x = m2*(1/12*(0.038**2 + 0.07**2)+((0.05 + .07/2)**2 + (0.05 -.038/2)**2))
I_3x = m3*(((0.024**2)/4 + (0.04)**2/12 - ybar**2) + ((0.16-.02)**2 + (0.05 - ybar)**2))

I_x = I_1x - I_2x - I_3x
print("I_x = ", I_x)

I_1y =1/12*m1*(.08**2 +0.16**2)  + m1*((0.16/2)**2 + (0.08/2)**2)
I_2y =1/12*m2*(.08**2 +0.07**2)  + m2*((.16 - .04 - .07/2)**2 + (0.08/2)**2)
I_3y =  I_3x

I_y = I_1y - I_2y - I_3y
print("I_y = ", I_y)

I_1z =1/12*m1*(.08**2 +0.05**2)  + m1*((0.05/2)**2 + (0.08/2)**2)
I_2z =1/12*m2*(.08**2 + 0.038**2)  + m2*((.05 - .038/2)**2 + (0.08/2)**2)
I_3z = m3*(0.024)**2/2-m3*(0.024)**2*ybar**2  + m3*((.08/2)**2+(.05 - ybar)**2)

I_z = I_1z - I_2z - I_3z
print("I_z = ", I_z)

print("#----------------------")
theta = sy.symbols("theta")
r_B_A = 0.05*sy.Matrix([sy.sin(theta), sy.cos(theta), 0])
r_D_B = sy.Matrix([0, 0.05*sy.cos(theta)- sy.sqrt(0.15**2 - 0.05**2*sy.Pow(sy.sin(theta),2)) , 0]) - r_B_A
r_D_A = r_B_A + r_D_B
a_D_A = diff(r_D_A, theta, 2)
