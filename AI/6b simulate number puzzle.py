from __future__ import print_function
from simpleai.search import astar, SearchProblem

print("04_Jayprabha Nadar")

GOAL = '''1-2-3
4-5-6
7-8-e'''

INITIAL = '''4-1-2
7-e-3
8-5-6'''

# Utility functions for conversions
def list_to_string(list_):
    '''Converts list representation of the puzzle to string representation.'''
    return '\n'.join(['-'.join(row) for row in list_])

def string_to_list(string_):
    '''Converts string representation of the puzzle to list representation.'''
    return [row.split('-') for row in string_.split('\n')]

def find_location(rows, element_to_find):
    '''Find the location of a piece in the puzzle. Returns a tuple: row, column.'''
    for ir, row in enumerate(rows):
        for ic, element in enumerate(row):
            if element == element_to_find:
                return ir, ic

# Cache the goal position of each piece
goal_positions = {}
rows_goal = string_to_list(GOAL)
for number in '12345678e':
    goal_positions[number] = find_location(rows_goal, number)

class EightPuzzleProblem(SearchProblem):
    '''Defines the 8-puzzle problem for A* search.'''

    def actions(self, state):
        '''Returns a list of the pieces we can move to the empty space.'''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')  # find the empty space
        actions = []

        # Check possible moves
        if row_e > 0:  # Can move the piece from above
            actions.append(rows[row_e - 1][col_e])
        if row_e < 2:  # Can move the piece from below
            actions.append(rows[row_e + 1][col_e])
        if col_e > 0:  # Can move the piece from the left
            actions.append(rows[row_e][col_e - 1])
        if col_e < 2:  # Can move the piece from the right
            actions.append(rows[row_e][col_e + 1])

        return actions

    def result(self, state, action):
        '''Return the resulting state after moving a piece to the empty space.'''
        rows = string_to_list(state)
        row_e, col_e = find_location(rows, 'e')  # Find the empty space
        row_n, col_n = find_location(rows, action)  # Find the position of the piece to move

        # Swap the empty space with the chosen piece
        rows[row_e][col_e], rows[row_n][col_n] = rows[row_n][col_n], rows[row_e][col_e]

        # Return the new state as a string
        return list_to_string(rows)

    def is_goal(self, state):
        '''Returns True if the current state matches the goal state.'''
        return state == GOAL

    def cost(self, state1, action, state2):
        '''Returns the cost of performing an action (fixed cost of 1 per move).'''
        return 1

    def heuristic(self, state):
        '''Returns an estimation of the distance from the current state to the goal state.
        This uses the Manhattan distance heuristic.
        '''
        rows = string_to_list(state)
        distance = 0
        for number in '12345678e':
            row_n, col_n = find_location(rows, number)
            row_n_goal, col_n_goal = goal_positions[number]
            distance += abs(row_n - row_n_goal) + abs(col_n - col_n_goal)
        return distance

# Solve the problem using A* search
result = astar(EightPuzzleProblem(INITIAL))

# Print the solution path
for action, state in result.path():
    print('Move piece', action)
    print(state)
