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

AC = sqrt(2)
