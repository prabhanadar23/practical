def associative_addition(a, b, c):
    left_side = (a + b) + c
    right_side = a + (b + c)
    return left_side, right_side

def associative_multiplication(a, b, c):
    left_side = (a * b) * c
    right_side = a * (b * c)
    return left_side, right_side

# Input values
a = 2
b = 3
c = 4

# Deriving expressions for addition
add_results = associative_addition(a, b, c)
print(f"Addition: (a + b) + c = {add_results[0]} and a + (b + c) = {add_results[1]}")
print("Addition is associative:", add_results[0] == add_results[1])

# Deriving expressions for multiplication
mult_results = associative_multiplication(a, b, c)
print(f"Multiplication: (a * b) * c = {mult_results[0]} and a * (b * c) = {mult_results[1]}")
print("Multiplication is associative:", mult_results[0] == mult_results[1])
