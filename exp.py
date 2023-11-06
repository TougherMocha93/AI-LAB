from sympy import symbols,And,Or,Not,Implies,Equivalent,pprint

p,q,r = symbols('p q r')

pandq = And(p,q)

Truth_values = {p : True , q : False , r : False}

print(pandq.subs(Truth_values))

print(Not(And(p,q)))