import math
import random

# Function to calculate the distance between two points (cities)
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the total distance of a route
def total_distance(route, cities):
    return sum(distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1)) + distance(cities[route[-1]], cities[route[0]])

# Function to perform simulated annealing
def simulated_annealing(cities, temperature, cooling_rate):
    # Start with a random route
    current_route = list(range(len(cities)))
    random.shuffle(current_route)
    
    current_distance = total_distance(current_route, cities)
    
    best_route = current_route[:]
    best_distance = current_distance

    while temperature > 1:
        # Create a new route by swapping two cities
        new_route = current_route[:]
        i, j = random.sample(range(len(cities)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        new_distance = total_distance(new_route, cities)

        # Decide if we should accept the new route
        if (new_distance < current_distance or
                random.uniform(0, 1) < math.exp((current_distance - new_distance) / temperature)):
            current_route = new_route
            current_distance = new_distance
            
            if current_distance < best_distance:
                best_route = current_route[:]
                best_distance = current_distance

        # Cool down the temperature
        temperature *= cooling_rate

    return best_route, best_distance

# Main function to run the TSP solver
def main():
    # Example cities (x, y coordinates)
    cities = [
        (0, 0), (1, 2), (2, 4), (3, 1),
        (4, 3), (5, 5), (6, 2), (7, 0)
    ]

    initial_temperature = 10000
    cooling_rate = 0.995

    best_route, best_distance = simulated_annealing(cities, initial_temperature, cooling_rate)
    
    print("Best route:", best_route)
    print("Best distance:", best_distance)

# Run the program
if __name__ == "__main__":
    main()
