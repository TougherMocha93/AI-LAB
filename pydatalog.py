from pyDatalog import pyDatalog

# Initializing PyDatalog
pyDatalog.create_terms('parent, grandparent, age, citizen, enrolled, prerequisite')

# Define the domain of individuals
+ citizen('Alice')
+ citizen('Bob')
+ citizen('Charlie')

# Define some facts for parent and grandparent
+ parent('Alice', 'Bob')
+ parent('Bob', 'Charlie')

# Define some facts for age
+ age('Alice', 30)
+ age('Bob', 40)
+ age('Charlie', 10)

# Define some facts for enrollment and prerequisites
+ enrolled('Alice', 'Physics')
+ enrolled('Bob', 'Math')
+ prerequisite('Math', 'Physics')

print(age)