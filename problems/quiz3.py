from math import radians
from sympy import *
m_h = 830
m_p = 140
h = 1.2
d = 0.110
e = 0 

g = 9.81

v_1 = m_h*g*h 

v_h = symbols("v")
T_2 = .5*m_h*v_h**2

v_h = solve(Eq(v_1,T_2),v_h)[1]
vAfter = (m_h*v_h)/(m_h + m_p)

T_2 = .5*(m_h + m_p)*(vAfter**2) 
F = symbols("F")
U = (m_h + m_p)*g*d - F*d
F = solve(T_2 + U)[0]
print("F in KN: ", F/1000)

print("#-------------------------")

AC = symbols("AC")
AB = BC = 12
AC = solve(Eq(AC**2, AB**2 + BC**2 +2*(AB)*(BC)*cos(radians(120))))[1] #in inches
AC /= 12 #in feet
AD = AC/2

mine = 6.8
alpha = symbols("alpha")
alpha = solve(Eq(4*(0.5) + 4*(1.25)-mine, 2*4/32.2*1/12*alpha + 4/32.2 * (.5)**2*alpha + 4/32.2 * 1.25**2 * alpha + 4/32.2*(.5*sin(radians(120)))**2 *alpha))[0]
print(alpha)

T = symbols("T")
T = solve(Eq(4*(0.25) - T/2, (4/32.2)/12*alpha + 4/32.2*1.25*alpha*0.25 + 4/32.2*0.5*0.866*0.5*sin(radians(120))*alpha))[0]
print(T)

print("#-------------------------")

M = 8
theta_c = 2190.56/M/2/3.1415
print(theta_c)

theta_a = 0.4*2190.56/M

F = symbols("F")
F = solve(Eq(.5*0.361*18.85**2 + F*0.25*theta_a, .5*0.361*75.4**2))[0]
print(F)

print("#-------------------------")
thing = 760
theta = 1 - (3)*(0.0034722)**2*(thing*5280/3600)**2/((32.2)*4)
print(acos(theta)*180/3.1415)

print("#-------------------------")
chickenwing =  42
H_x = 0.08983*chickenwing
H_y = 0 
H_z = -0.0539*chickenwing 

print("{}i + {}j + {}k".format(H_x, H_y, H_z))
Mag = sqrt(H_x**2 + H_y**2 + H_z**2)
mom = H_x*chickenwing
angle = acos(mom/(Mag*chickenwing))*180/3.1415
print(angle)

print("#-------------------------")

applePotato = 54
m = (sqrt(2/3)*1.5*applePotato*1.2*18/5*1/(1.5**2*1.2566)) 
print(m)