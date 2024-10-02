# Define predicates for male and female
male = {'John', 'Michael', 'Chris', 'Tom'}
female = {'Anna', 'Mary', 'Kate', 'Emma'}

# Define parent relationships
parent = {
    'John': {'Chris', 'Emma'},   # John is a parent of Chris and Emma
    'Mary': {'Chris', 'Emma'},   # Mary is a parent of Chris and Emma
    'Michael': {'Kate', 'Tom'},  # Michael is a parent of Kate and Tom
    'Anna': {'Kate', 'Tom'}       # Anna is a parent of Kate and Tom
}

# Define rules for family relationships
def father(child):
    for p in parent:
        if child in parent[p] and p in male:
            return p
    return None

def mother(child):
    for p in parent:
        if child in parent[p] and p in female:
            return p
    return None

def grandfather(grandchild):
    father_name = father(grandchild)
    if father_name:
        return father(father_name)
    return None

def grandmother(grandchild):
    mother_name = mother(grandchild)
    if mother_name:
        return mother(mother_name)
    return None

def brother(sibling):
    father_name = father(sibling)
    siblings = set(parent[father_name]) if father_name else set()
    siblings.discard(sibling)  # Remove self from siblings
    return {s for s in siblings if s in male}

def sister(sibling):
    father_name = father(sibling)
    siblings = set(parent[father_name]) if father_name else set()
    siblings.discard(sibling)  # Remove self from siblings
    return {s for s in siblings if s in female}

def uncle(child):
    father_name = father(child)
    mother_name = mother(child)
    return {p for p in male if p != father_name and p in parent and child in parent[p]}

def aunt(child):
    father_name = father(child)
    mother_name = mother(child)
    return {p for p in female if p != mother_name and p in parent and child in parent[p]}

def nephew(uncle_or_aunt):
    return {p for p in parent if any(s in nephew(uncle_or_aunt) for s in parent[p])}

def niece(uncle_or_aunt):
    return {p for p in parent if any(s in niece(uncle_or_aunt) for s in parent[p])}

def cousin(child):
    parent_name = father(child) or mother(child)
    cousins = set()
    for p in parent:
        if p != parent_name and child in parent[p]:
            cousins.update(parent[p])
    return cousins

# Example Usage
print("Father of Chris:", father('Chris'))
print("Mother of Chris:", mother('Chris'))
print("Grandfather of Emma:", grandfather('Emma'))
print("Grandmother of Emma:", grandmother('Emma'))
print("Brothers of Chris:", brother('Chris'))
print("Sisters of Kate:", sister('Kate'))
print("Uncles of Chris:", uncle('Chris'))
print("Aunts of Chris:", aunt('Chris'))
print("Cousins of Chris:", cousin('Chris'))

