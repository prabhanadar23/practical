# Importing required functions from future and simpleai
from __future__ import print_function
from simpleai.search import CspProblem, backtrack, min_conflicts
from simpleai.search import MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE
print("04_Jayprabha Nadar")
# Define the variables (States of Australia)
variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')

# Define the domains (Colors that each state can take)
domains = {v: ['red', 'green', 'blue'] for v in variables}

# Define the constraint function (Neighbors must have different colors)
def const_different(variables, values):
    return values[0] != values[1]

# Define the constraints (Neighbors must have different colors)
constraints = [
    (('WA', 'NT'), const_different),
    (('WA', 'SA'), const_different),
    (('SA', 'NT'), const_different),
    (('SA', 'Q'), const_different),
    (('NT', 'Q'), const_different),
    (('SA', 'NSW'), const_different),
    (('Q', 'NSW'), const_different),
    (('SA', 'V'), const_different),
    (('NSW', 'V'), const_different),
]

# Initialize the problem
my_problem = CspProblem(variables, domains, constraints)

# Solving the problem using different heuristics
# 1. Basic backtracking
print("Solution using basic backtracking:")
print(backtrack(my_problem))

# 2. Backtracking with the Most Constrained Variable heuristic
print("\nSolution using Most Constrained Variable:")
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE))

# 3. Backtracking with the Highest Degree Variable heuristic
print("\nSolution using Highest Degree Variable:")
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE))

# 4. Backtracking with the Least Constraining Value heuristic
print("\nSolution using Least Constraining Value:")
print(backtrack(my_problem, value_heuristic=LEAST_CONSTRAINING_VALUE))

# 5. Backtracking with both Most Constrained Variable and Least Constraining Value heuristics
print("\nSolution using Most Constrained Variable and Least Constraining Value:")
print(backtrack(my_problem, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))

# 6. Backtracking with both Highest Degree Variable and Least Constraining Value heuristics
print("\nSolution using Highest Degree Variable and Least Constraining Value:")
print(backtrack(my_problem, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))

# 7. Solution using Min Conflicts algorithm
print("\nSolution using Min Conflicts algorithm:")
print(min_conflicts(my_problem))
