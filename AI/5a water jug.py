print("04_Jayprabha Nadar")

# Capacity of jugs -> (x, y, z)
capacity = (12, 8, 5)
x, y, z = capacity

# To mark visited states
memory = {}

# To store the solution path
solution_path = []

# Function to get all possible states of the jugs
def get_all_states(state):
    a, b, c = state  # Current amounts in jugs A, B, C

    # Check if the goal state is reached
    if a == 6 and b == 6:
        solution_path.append(state)  # Append the successful state
        return True

    # If this state has been visited before, return False
    if (a, b, c) in memory:
        return False

    # Mark the current state as visited
    memory[(a, b, c)] = 1

    # Empty jug A
    if a > 0:
        # Pour A into B
        if a + b <= y:
            if get_all_states((0, a + b, c)):
                solution_path.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                solution_path.append(state)
                return True
        # Pour A into C
        if a + c <= z:
            if get_all_states((0, b, a + c)):
                solution_path.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                solution_path.append(state)
                return True

    # Empty jug B
    if b > 0:
        # Pour B into A
        if a + b <= x:
            if get_all_states((a + b, 0, c)):
                solution_path.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                solution_path.append(state)
                return True
        # Pour B into C
        if b + c <= z:
            if get_all_states((a, 0, b + c)):
                solution_path.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                solution_path.append(state)
                return True

    # Empty jug C
    if c > 0:
        # Pour C into A
        if a + c <= x:
            if get_all_states((a + c, b, 0)):
                solution_path.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                solution_path.append(state)
                return True
        # Pour C into B
        if b + c <= y:
            if get_all_states((a, b + c, 0)):
                solution_path.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                solution_path.append(state)
                return True
    return False

# Initial state: full jug A, empty jugs B and C
initial_state = (12, 0, 0)

print("Starting work...\n")

# Call the function to find all states
get_all_states(initial_state)

# Reverse the solution path to print it in the correct order
solution_path.reverse()

# Print each state in the solution path
for state in solution_path:
    print(state)
