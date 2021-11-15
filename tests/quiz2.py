from sympy import *

print("----------------------------------")
print("normal = ", 4*9.8+9.8)

print("----------------------------------")
alpha = symbols("alpha")
eq1 = Eq(((9/5)-(1/2))*20 - (9/5)*(9*alpha+20), 17/15*alpha)
alpha = solve(eq1)[0]
print("alpha = ", alpha)

print("----------------------------------")
print("Friction =", 9*alpha+20)


