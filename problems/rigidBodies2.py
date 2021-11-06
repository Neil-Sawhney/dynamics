
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
v_H_K, w_KH, v_H, a_H = sy.symbols("v_H_K w_KH v_H a_H ")
vv_H = array([0,v_H, 0])
va_H = array([0,a_H, 0])
vw_AK = array([0,0,1.1])
valpha_AK = array([0,0,1])

vr_H_K = array([-14,14,0])
vr_K_A = array([12,12,0])

vw_HK = array([0,0,w_KH])
vv_K = cross(vw_AK, vr_K_A)
eq1 = cross(vw_HK, -vr_H_K) +vv_H- vv_K
sol1 = sy.solve([eq1[0], eq1[2],eq1[2]])
vw_KH = array([0,0,sol1[w_KH]])

vw_KH_AK = vw_KH - vw_AK 
print("w_KH/AK= ", vw_KH_AK)
# accel
alpha_KH= sy.symbols("alpha_KH")
valpha_KH = array([0,0,alpha_KH])
va_K = cross(valpha_AK, vr_K_A) + cross(vw_AK,vv_K)
eq2 =  cross(valpha_KH, -vr_H_K) + cross(vw_KH, -cross(vw_KH, vr_H_K)) + va_H - va_K
sol2 = sy.solve(eq2)
valpha_KH = array([0,0,sol2[alpha_KH]])
valpha_KH_AK = valpha_KH - valpha_AK
print("valpha_KH_AK =", valpha_KH_AK)

print("#----------------------")
R_1, R_2, h = sy.symbols("R_1 R_2 h")
g = 9.8
m = 20
N = 110
va = array([N/m,0,0])
vR_1 = array([0,R_1,0])
vR_2 = array([0,R_2,0])
vF_g = array([0,-m*g,0])
vN = array([N,0,0])
print("a = ", va)
eq1 = array([0,0,-N*h]) + cross(array([0.3,0,0]),vF_g)- N*0.9
eq2 = array([0,0,-N*h]) + cross(array([-0.3,0,0]),vF_g)- N*0.9
eq3 = array([0,0,-.3*R_1]) + array([0,0,.3*R_2]) + array([0,0, N*(.9-h)])
sol1 = -sy.solve(eq1[2])[0]
sol2 = -sy.solve(eq2[2])[0]
print("h is inbetween {} and {}".format(sol1, sol2))


print("#----------------------")
m=10
g = 9.8
theta = radians(30)
Ay, Bx, By, Cx, Cy, Dx, Dy, Ey, F = sy.symbols("Ay Bx By Cx Cy Dx Dy Ey F")
vr_DB = 0.6*sy.Matrix([cos(theta),sin(theta),0])
vr_EA = 0.6*sy.Matrix([-cos(theta),sin(theta),0])
vA = sy.Matrix([0,Ay,0])
vB = sy.Matrix([Bx,By,0])
vC = sy.Matrix([Cx,Cy,0])
vD = sy.Matrix([Dx,Dy,0])
vE = sy.Matrix([0,Ey,0])
vF = F*sy.Matrix([vr_DB[1],-vr_DB[0],0])
vG = sy.Matrix([0,-m*g,0])

M_D = vr_DB.cross(vE) + vr_DB.cross(vB)
M_C = (.5*vr_EA).cross(vA) - (.5*vr_EA).cross(vB)
M_B = (sy.Matrix([-.15,0,0])).cross(vG) - (vr_DB).cross(vA)
eq1 = -vA - vB + vG - vF
solx = sy.solve([M_D[0],M_C[0],eq1[0],M_B[0]]) 
soly = sy.solve([M_D[1],M_C[1],eq1[1],M_B[1]]) 
solz = sy.solve([M_D[2],M_C[2],eq1[2],M_B[2]]) 

print("#----------------------")
theta = radians(60)
T_DE,F_N,T_BC,F_f,F_p,F_by,F_bx,a_By,a_py= sy.symbols("T_DE F_N T_BC F_f F_p F_by F_bx a_By a_py")
mu_k,m_B,m_p,g = 0.4,36,5,32.2

eq1 = sy.Eq(18/12*T_DE*sin(theta)-m_p*g*(9/12)+F_N*(9/12),0)#Moment about b
eq2 = sy.Eq(-18/12*T_BC*sin(theta)+m_p*g*(9/12)-F_N*(9/12),0)#moment about d
eq3 = sy.Eq(T_BC*cos(theta)+T_DE*cos(theta) - F_f, F_p*sin(theta))#forces in x for p
eq4 = sy.Eq(T_BC*sin(theta)+T_DE*sin(theta) - m_p*g + F_N, F_p*cos(theta)) #forces in y for p
eq5 = sy.Eq(F_f,mu_k*F_N) #force of friction
eq6 = sy.Eq(F_f, F_bx) #forces in x for b
eq7 = sy.Eq(-m_B*g  - F_N, F_by) #forces in y for b
eq8 = sy.Eq(a_By, a_py)  #accel y
eq9 = sy.Eq(F_by, m_B*a_By)  #f = ma block
eq10 = sy.Eq(F_p*cos(theta), m_p*a_py)  #f=ma plat

print(sy.solve([eq3,eq4,eq5,eq6,eq7]))
