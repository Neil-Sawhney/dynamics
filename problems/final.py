from sympy import*

print("Insert Theta Initial: ")
theta_0 = int(input())
print("Insert Omega Initial: ")
omega_0 = int(input())

init_printing(use_unicode=True)

omega = Function('omega')
theta = symbols("theta")

eqs = [
Eq(Derivative(omega(theta), theta, theta) + 9*omega(theta), omega(theta)),
]
ans = dsolve(eqs)

pretty_print(ans)
