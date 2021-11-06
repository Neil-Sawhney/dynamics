
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
theta = radians(60);
w_AB = array([0,0,-950*2*pi/60])
r_B_A = 0.05*array([sin(theta), cos(theta), 0])
v_B = cross(w_AB, r_B_A)
phi = arcsin(sin(theta)/.15*.05)
r_D_B = 0.15*array([-sin(phi), cos(phi), 0])
w_DB ,v_D = sy.symbols("w_DB v_D")
vecv_D=array([0,v_D, 0])
v_D_B = array([-r_D_B[1]*w_DB, r_D_B[0]*w_DB, 0])
eq = v_B+ v_D_B  - vecv_D
print(sy.solve(eq))
v_D = array([0,sy.solve(eq)[v_D], 0])
w_DB = array([0,0, sy.solve(eq)[w_DB]])

alpha_BD ,a_D = sy.symbols("alpha_BD a_D")
a_B = cross(w_AB, v_B)
v_D_B = cross(w_DB, r_D_B) 
eq2 = a_B + array([-alpha_BD*r_D_B[1], alpha_BD*r_D_B[0], 0]) + cross(w_DB, v_D_B) - array([0, a_D, 0])
print("a_D = ", sy.solve(eq2))

print("#----------------------")
vr_A_O = array([-0.6,0,0])
vr_B_A = array([0.6,2,0])
vw_OA = array([0,0,-24*2*pi/60])
vv_A = cross(vr_A_O, vw_OA)
v_B, w_AB, alpha_BCE, a_E = sy.symbols("v_B w_AB alpha_BCE a_E")
vv_B = array([0,v_B,0])
vw_AB = array([0,0,w_AB])
eq1 = vv_A + cross(vw_AB,vr_B_A) + vv_B
s1 = sy.solve(eq1)
print(s1)
v_B = s1[v_B]
vv_B = array([0,v_B,0])
w_AB = s1[w_AB]
vw_AB = array([0,0,w_AB])
w_BCE = -v_B / 3
v_E = w_BCE*3.3
vw_BCE = array([0,0,w_BCE])
valpha_BCE = array([0,0,alpha_BCE])
a_Bx,a_By=sy.symbols("a_Bx a_By")
eq2 = cross(valpha_BCE,array([-3,0,0]))+cross(vw_BCE,vv_B) - array([a_Bx,a_By,0]) #array
alpha_AB, a_Bx, a_By = sy.symbols("alpha_AB a_Bx a_By")
valpha_AB = array([0,0,alpha_AB])
va_B = array([a_Bx, a_By,0])
eq3 = cross(valpha_BCE,array([-3,0,0])) + cross(vw_BCE, vv_B) - va_B
va_A= cross(-vw_OA,vv_A)
eq4 = va_A + cross(valpha_AB,vr_B_A)  - va_B
sol4 = sy.solve([eq3[0], eq3[1], eq4[1], eq4[0]])
print(sol4)
valpha_BCE = array([0,0,sol4[alpha_BCE]])
vv_E = array([0,0,v_E])
va_D = cross(valpha_BCE,array([3.3, 0, 0])) + cross(vw_BCE,vv_E)
print("v_D", vv_E)
print("a_D", va_D)

print("#----------------------")
v_H_K, w_KH, v_H, a_H = sy.symbols("v_H_K w_K_H v_H a_H ")
vv_H = array([0,v_H, 0])
va_H = array([0,a_H, 0])
vw_AK = array([0,0,1.1])
valpha_AK = array([0,0,1.1])
valpha_AK = array([0,0,1])

vr_H_K = array([-14,14,0])
vr_K_A = array([12,12,0])
vv_K = cross(vw_AK, vr_K_A)
vH_Kx, vH_Ky = sy.symbols('vH_Kx vH_Ky')
vv_H_K = array([-2*vv_K[0], vH_Ky, 0])

vw_KH = array([0,0, w_KH])
eq1 = vv_K + array([-14*w_KH,-14*w_KH,0]) - vv_H_K
vw_KH_AK = vw_KH - vw_AK
sol1 = sy.solve([eq1[1], eq1[2]])
print(sol1)

