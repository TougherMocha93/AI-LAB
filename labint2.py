from pyDatalog import pyDatalog

pyDatalog.create_terms('parent,subject,age,prerequisite,A,B,C')

+ parent('Alice','Bob')
+ parent('Bob','Charles')

+ subject('Alice','Maths')

+ age('Alice','21')
+ age('Bob','42')
+ age('Charles','83')

+ prerequisite('Maths','Algebra')

print(parent('Alice',A))
print(age('Charles',B))
print(prerequisite('Maths',C))