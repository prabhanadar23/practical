print("04_Jayprabha Nadar")

# Define the tree structure as a nested list
tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0 
pruned = 0 

def children(branch, depth, alpha, beta):
    global tree 
    global root 
    global pruned 
    i = 0 
    for child in branch:
        if isinstance(child, list):  # Check if the child is a list
            (nalpha, nbeta) = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:  # Minimizing player
                beta = min(nalpha, beta)
            else:  # Maximizing player
                alpha = max(nbeta, alpha)
            branch[i] = alpha if depth % 2 == 0 else beta
            i += 1
        else:  # Leaf node
            if depth % 2 == 0 and alpha < child:  # Maximizing player
                alpha = child
            if depth % 2 == 1 and beta > child:  # Minimizing player
                beta = child
            if alpha >= beta:  # Pruning occurs
                pruned += 1
                break
    if depth == root: 
        tree = alpha if root == 0 else beta
    return (alpha, beta)

def alphabeta(in_tree=tree, start=root, upper=-15, lower=15):
    global tree 
    global pruned 
    global root 
    (alpha, beta) = children(tree, start, upper, lower)

    # Print results
    print("(alpha, beta):", (alpha, beta)) 
    print("Result:", tree) 
    print("Times pruned:", pruned) 
    
    return (alpha, beta, tree, pruned)

if __name__ == "__main__": 
    alphabeta()
