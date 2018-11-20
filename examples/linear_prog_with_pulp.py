'''Problem:

Suppose you are a magical healer and you goal is to heal
anyone who asks for help. The more you are able to heal
someone, the better. Your secret behind the healing is two
medicines, each of which uses special herbs. 

To create one unit of medicine 1 , you need three units of 
herb A and two units of herb B. 
Similarly, to create one unit of medicine 2, you need four
units of herb A and 1 unit of herb B. 

Medicine 1 can heal a person by 25 unit of health and
medicine 2 by 20 units. To complicate things further, you 
only have twenty-five herbs A and ten herbs B at your 
disposal. 

How many of each medicine will you create to maximize the
health recovery of the next person who walks in?
'''

'''Modeling the problem:

To maximize the health restored we will create x units of
Medicine 1 and y units of Medicine 2, that is
    25 * x + 20 * y
, where to 25 and 20 are the amounts of health restored
with each medicine.

Since we have twenty-five units of herb A and we need three
per unit of Medicine 1 and four per unit of Medicine 4, the
usage of herb A can be represented as
    3 * x + 4 * y <= 25
, since we can't use more than twenty five herb A.

Since we have ten units of herb B and we need two per unit
of Medicine 1 and one per unit of Medicine 2, the usage
of herb B can be represented as
    2 * x + 1 * y <= 10
which is equivalent to
    2 * x + y <= 10
, since we can't use more than ten herb B.

If we tried to solve this problem through graphical
representation, the solution would be the intersection between
the two defined mathematical functions.

In this case, we'll solve this maximization problem using Python
and the PuLP package.

Source of the example: 
https://itnext.io/introduction-to-linear-programming-with-python-1068778600ae
'''


# Package can be used to solve optimization problems using\
# linear programming
# https://pythonhosted.org/PuLP/#pulp-internal-documentation
from pulp import *

# Create the LpProblem object to start a problem
# The first argument specifies the name of the problem, the\
# second specifies this is a maximization problem
prob = LpProblem("The Miracle Worker", LpMaximize)

# Create problem variables
# The first argument is the name of each variable,\
# the second is the minimum possible value, the third\
# argument specifies these variables have discrete\
# values instead of continuous
# We don't include an upper bound because these variables\
# effectively have no upper bound in the context of the\
# problem
x = LpVariable("Medicine_1_units", lowBound=0, cat=LpInteger)
y = LpVariable("Medicine_2_units", lowBound=0, cat=LpInteger)

# Add to the problem the mathematical function that calculates\
# our answer, that is, how much health is restored with the\
# produced Medicine 1 units (x) and the produced Medicine 2\
# units (y), knowing that the former restores 25 and the\
# latter 20. We also pass the name of the function
# Because this is the first function added to the problem, this\
# is considered to be actual problem we are trying to solve.\
# Following functions we'll be interpreted as constraints to the\
# problem
prob += 25*x + 20*y, "Health restored to be maximized"

# The constraints for each herb.
# Herb A uses 3 units to produce one Medicine 1 (x) and four\
# units to produce one Medicine 2 (y). We only have 25 herb A\
# at our disposal
prob += 3*x + 4*y <= 25, "Herb A constraint"
# Herb B uses 2 units to produce one Medicine 1 (x) and one\
# unit to produce one Medicine 2 (y). We only have 10 herb B\
# at our disposal
prob += 2*x + y <= 10, "Herb B constraint"

# Call the .solve() method to get the answer to the problem
prob.solve()

# Check the status of the problem ("Not Solved", "Optimal",\
# "Infeasible", "Unbounded" or "Undefined") in the problem\
# status dictionary using the current status of the problem\
# as key
print("Status:", LpStatus[prob.status])

# Loop through the variables of the problem and print their\
# optimum value
for v in prob.variables():
    print(f'{v.name} = {v.varValue}')

# Print the value of the objective variable
print("Total Health that can be restored =", value(prob.objective))


'''
This problem could then be written to a .lp file using
prob.writeLP("MiracleWorker.lp")

Here are the contents of the .lp file for this problem:

\* The Miracle Worker *\
Maximize
Health_restored_to_be_maximized: 25 Medicine_1_units + 20 Medicine_2_units
Subject To
Herb_A_constraint: 3 Medicine_1_units + 4 Medicine_2_units <= 25
Herb_B_constraint: 2 Medicine_1_units + Medicine_2_units <= 10
Bounds
0 <= Medicine_1_units
0 <= Medicine_2_units
Generals
Medicine_1_units
Medicine_2_units
End
'''