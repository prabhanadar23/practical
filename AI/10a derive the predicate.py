class PredicateLogic:
    def __init__(self):
        # Dictionary to store relationships
        self.relationships = {}

    def add_relationship(self, subject, predicate):
        if subject in self.relationships:
            self.relationships[subject].add(predicate)
        else:
            self.relationships[subject] = {predicate}

    def derive(self, subject):
        derived_predicates = set()
        if subject in self.relationships:
            for predicate in self.relationships[subject]:
                derived_predicates.add(predicate)
                derived_predicates.update(self.derive(predicate))  # Recursive derivation
        return derived_predicates

# Create an instance of PredicateLogic
logic = PredicateLogic()

# Add relationships
logic.add_relationship('Sachin', 'Batsman')
logic.add_relationship('Batsman', 'Cricketer')

# Derive predicates for Sachin
result = logic.derive('Sachin')

# Display results
for predicate in result:
    print(f'Sachin is {predicate}')
