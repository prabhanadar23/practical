print("04_Jayprabha Nadar")
from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    
    def actions(self, state):
        # Return possible actions: add any character or space until the goal is reached
        if len(state) < len(GOAL):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        # Append the chosen action (character) to the current state
        return state + action

    def is_goal(self, state):
        # Check if the current state matches the goal
        return state == GOAL

    def heuristic(self, state):
        # Calculate heuristic: count the number of wrong characters and how many are missing
        wrong = sum(1 for i in range(len(state)) if state[i] != GOAL[i])
        missing = len(GOAL) - len(state)
        return wrong + missing

# Create an instance of the HelloProblem with an empty initial state
problem = HelloProblem(initial_state='')

# Use A* algorithm to solve the problem
result = astar(problem)

# Print the final state (goal) and the sequence of actions taken
print("Final State:", result.state)
print("Path to Solution:", result.path())
