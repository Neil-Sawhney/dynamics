from sympy import*

print("Insert Theta Initial: ")
theta_0 = int(input())
print("Insert Omega Initial: ")
omega_0 = int(input())

init_printing(use_unicode=True)

t, theta = symbols("t theta")
alpha_w = Function("alpha_w")(t)
alpha_p = Function("alpha_p")(t)

omega_p = Derivative(theta, t)


r = .5
l = 5.5
m_p = 140
m_w = 8
I_p = (1/12)*m_p*l**2
u_k = .7
g = 32.2

#alpha_p=({[r*alpha_w-alpha_p*l*(1/2)*cos(theta)-omega_p**2*l*(1/2)*sin(theta)]*[(-m_p*(l/2)*cos(the)]}+{[(m_p*g)+(m_p*alpha_p*(l/2)]*sin(theta))-(m_p*omega_p**2*(l/2)*cos(theta))]*[(l/2)*sin(theta)]})/(I_p)
#dtheta_p/dt = omega_p
#domega_p/dt = alpha_p 
#alpha_w = {([m_p*alpha_p*l*(1/2)*cos(theta)]+[omega_p**2*l*(1/2)*sin(theta)*m_p])+{(u_k)*[m_p*g+(m_p*alpha_p*(l/2)*sin(theta))-(omega_p**2*(l/2)*cos(theta))+m_w*g]}}/(m_w*r+m_p*r)


#eq1 = Eq(omega(theta), Derivative(omega(theta), theta, theta) + 9*omega(theta))
#eq2 = Eq(alpha(theta), Derivative(alpha(theta), theta, theta) + 9*alpha(theta))
Eq = [
    Eq(alpha_p,(((r*alpha_w-alpha_p*l*(1/2)*cos(theta)-omega_p**2*l*(1/2)*sin(theta))*((-m_p*(l/2)*cos(theta)))+(((m_p*g)+(m_p*alpha_p*(l/2))*sin(theta))-(m_p*omega_p**2*(l/2)*cos(theta)))*((l/2)*sin(theta))))/(I_p) ),
    Eq(alpha_w,(((m_p*alpha_p*l*(1/2)*cos(theta))+(omega_p**2*l*(1/2)*sin(theta)*m_p))+((u_k)*(m_p*g+(m_p*alpha_p*(l/2)*sin(theta))-(omega_p**2*(l/2)*cos(theta))+m_w*g)))/(m_w*r+m_p*r)),
#    Eq(LHS,RHS),
#    Eq(LHS,RHS),
#    Eq(LHS,RHS),
#    Eq(LHS,RHS),
#    Eq(LHS,RHS),
#    Eq(LHS,RHS),
#    Eq(LHS,RHS),
]

ans = dsolve(Eq)

pprint(ans)
