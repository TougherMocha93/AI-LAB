from sympy import symbols, Not, And, Or, Implies, Equivalent,simplify
from sympy import pprint

p, q, r = symbols('p q r')

not_p = Not(p)
p_and_q = And(p, q)
p_or_q = Or(p, q)
p_implies_q = Implies(p, q)
p_biimplies_q = Equivalent(p,q)

truth_values = {p: False, q: False, r:True}
pandq = p_and_q.subs(truth_values)
porq = p_or_q.subs(truth_values)
notp = not_p.subs(truth_values)
pimpliesq = p_implies_q.subs(truth_values)
pbiimpliesq = p_biimplies_q.subs(truth_values)

print("negation", notp) 
print("Conjunction", pandq)
print("Disjunction", porq)
print("Implication", pimpliesq)
print("BIImplication", pbiimpliesq)

print(Not(And(p,q)),Not(And(p,q)).subs(truth_values))

pprint(p_or_q, use_unicode=True)
pprint(p_and_q, use_unicode=True)
pprint(not_p, use_unicode=True)
pprint(p_biimplies_q, use_unicode=True)