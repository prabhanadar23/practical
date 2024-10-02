from sympy import symbols, expand

# Define the symbols
a, b, c = symbols('a b c')

# Expression using Distributive Law
expression = a * (b + c)

# Apply the Distributive Law
derived_expression = expand(expression)

# Display the original and derived expressions
print("Original Expression: a * (b + c)")
print("Derived Expression: ", derived_expression)
