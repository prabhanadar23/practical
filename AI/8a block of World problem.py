class BlocksWorld:
    def __init__(self):
        self.state = {
            'A': 'table',
            'B': 'table',
            'C': 'A',
            'D': 'B'
        }
        self.goal = {
            'A': 'B',
            'B': 'C',
            'C': 'table',
            'D': 'table'
        }

    def is_goal(self):
        return self.state == self.goal

    def move(self, block, target):
        if self.state[block] != 'table':
            # Move block from on top of another block to target
            self.state[self.state[block]] = 'table'  # Clear the block below
        self.state[block] = target  # Move block to the target

    def print_state(self):
        for block, position in self.state.items():
            print(f"Block {block} is on {position}")

    def solve(self):
        # A simple strategy to solve the problem
        if not self.is_goal():
            self.move('D', 'table')  # Move D to table
            self.move('C', 'B')      # Move C on top of B
            self.move('B', 'A')      # Move B on top of A
            self.move('A', 'table')   # Move A to table

        self.print_state()


if __name__ == "__main__":
    problem = BlocksWorld()
    print("Initial State:")
    problem.print_state()
    
    print("\nSolving the Blocks World Problem...")
    problem.solve()
    
    print("\nFinal State:")
    problem.print_state()
