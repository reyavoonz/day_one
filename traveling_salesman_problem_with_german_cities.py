from itertools import permutations

#cities chosen
cities = ["Berlin", "Dresden", "Hamburg", "Munich", "Frankfurt"]

#distances (km) are assumed, not reliable
distance_matrix = [
    [0, 100, 200, 500, 400],  # Distances from Berlin
    [100, 0, 300, 400, 300],  # Distances from Dresden
    [200, 300, 0, 700, 400],  # Distances from Hamburg
    [500, 400, 700, 0, 300],  # Distances from Munich
    [400, 300, 400, 300, 0]   # Distances from Frankfurt
]

#Brute force since it's easier for this example
def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    min_path = None
    min_distance = float('inf')
   #used online help here
    for perm in permutations(range(n)):
        current_distance = sum(distance_matrix[perm[i]][perm[i+1]] for i in range(n-1)) + distance_matrix[perm[-1]][perm[0]]
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = perm

    return min_path, min_distance

#solve probelm
optimal_path, optimal_distance = tsp_brute_force(distance_matrix)

#results
print("Optimal Path: ", [cities[i] for i in optimal_path])
print("Optimal Distance: ", optimal_distance, "km")
