print("04_Jayprabha Nadar")
import math

increment = 0.1 
startingPoint = [1, 1] 
point1 = [1, 5] 
point2 = [6, 4] 
point3 = [5, 2] 
point4 = [2, 1]

# Function to calculate Euclidean distance between two points
def distance(x1, y1, x2, y2): 
    dist = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))  # Corrected distance calculation
    return dist

# Function to calculate the sum of distances from a given point to all other points
def sumOfDistances(x1, y1, px1, py1, px2, py2, px3, py3, px4, py4): 
    d1 = distance(x1, y1, px1, py1) 
    d2 = distance(x1, y1, px2, py2) 
    d3 = distance(x1, y1, px3, py3) 
    d4 = distance(x1, y1, px4, py4) 
    return d1 + d2 + d3 + d4

# Function to calculate the distance and return it with the point
def newDistance(x1, y1, point1, point2, point3, point4): 
    d1temp = sumOfDistances(x1, y1, point1[0], point1[1], point2[0], point2[1], point3[0], point3[1], point4[0], point4[1])
    return [x1, y1, d1temp]  # Returns point along with sum of distances

# Find the point with the minimum distance
def newPoints(minimum, d1, d2, d3, d4): 
    if d1[2] == minimum: 
        return [d1[0], d1[1]] 
    elif d2[2] == minimum: 
        return [d2[0], d2[1]] 
    elif d3[2] == minimum: 
        return [d3[0], d3[1]] 
    elif d4[2] == minimum: 
        return [d4[0], d4[1]] 

# Calculate initial minimum distance from the starting point
minDistance = sumOfDistances(startingPoint[0], startingPoint[1], point1[0], point1[1], point2[0], point2[1], point3[0], point3[1], point4[0], point4[1])

flag = True 
i = 1

# Begin optimization loop
while flag: 
    # Calculate the distances for new points around the current starting point
    d1 = newDistance(startingPoint[0] + increment, startingPoint[1], point1, point2, point3, point4) 
    d2 = newDistance(startingPoint[0] - increment, startingPoint[1], point1, point2, point3, point4) 
    d3 = newDistance(startingPoint[0], startingPoint[1] + increment, point1, point2, point3, point4) 
    d4 = newDistance(startingPoint[0], startingPoint[1] - increment, point1, point2, point3, point4) 

    print(i, ' ', round(startingPoint[0], 2), round(startingPoint[1], 2))  # Print iteration, and point coordinates

    # Find the minimum distance
    minimum = min(d1[2], d2[2], d3[2], d4[2]) 

    # If the new minimum is smaller than the current minimum distance, update the starting point
    if minimum < minDistance: 
        startingPoint = newPoints(minimum, d1, d2, d3, d4) 
        minDistance = minimum  # Update the minimum distance
        i += 1  # Increment the iteration count
    else: 
        flag = False  # Terminate the loop if no improvement is found
