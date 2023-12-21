import heapq
import random
import time

class State:
    def __init__(self, num_cities, parent=None):
        # Initialize the state with the number of cities and an optional parent
        self.visited = [False] * num_cities  # Track visited cities
        self.num_visited = 0  # Count of visited cities
        self.current_id = 0  # Current city ID
        self.parent = parent  # Add the parent attribute

    def __lt__(self, other):
        # Comparison method for state objects based on the number of visited cities
        return self.num_visited < other.num_visited

def cost(i, j):
    # Generate a random cost between cities i and j
    return random.randint(1, 100)

def min_out_heuristic(state, graph):
    # Calculate the min-out heuristic for a state and graph
    current_city = state.current_id
    remaining_cities = [city for city in range(len(graph)) if not state.visited[city]]

    if not remaining_cities:
        return 0  # No remaining cities, heuristic is 0

    return min(graph[current_city][neighbor] for neighbor in remaining_cities)

def h_zero(state, graph):
    # Trivial heuristic always returning 0
    return 0

def is_goal(state, num_cities):
    # Check if the state is a goal state
    return state.num_visited == num_cities and state.current_id == 0

def successors(state, graph):
    # Generate successor states and their step costs for a given state and graph
    successors = []
    for next_city in range(len(graph)):
        if not state.visited[next_city]:
            new_state = State(len(graph))
            new_state.visited = state.visited.copy()
            new_state.visited[next_city] = True
            new_state.num_visited = state.num_visited + 1
            new_state.current_id = next_city
            successors.append((new_state, graph[state.current_id][next_city]))
    return successors

def ida_star(state, graph, heuristic, cost_limit):
    # IDA* algorithm for solving the traveling salesperson problem
    global generated_nodes, expanded_nodes
    generated_nodes = 0
    expanded_nodes = 0

    start_time = time.perf_counter() 

    def search(node, g, f_limit, path):
        # Recursive search function for IDA*
        global generated_nodes, expanded_nodes
        generated_nodes += 1

        h = heuristic(node, graph)
        f = g + h
        if f > f_limit:
            return f, path
        if is_goal(node, len(graph)):
            return -1, path + [node.current_id]  # Goal found
        min_cost = float('inf')
        expanded_nodes += 1

        for successor, step_cost in successors(node, graph):
            result, result_path = search(successor, g + step_cost, f_limit, path + [node.current_id])
            if result == -1:
                return -1, result_path  # Goal found
            if result < min_cost:
                min_cost = result

        return min_cost, path

    limit = heuristic(state, graph)
    while True:
        result, optimal_path = search(state, 0, limit, [])
        if result == -1:
            elapsed_time = time.perf_counter()  - start_time
            #print("IDA* Goal found. Limit:", limit, "Elapsed time:", elapsed_time)  # Debugging print
            return limit, expanded_nodes, generated_nodes, elapsed_time, optimal_path  # Goal found
        if result == float('inf'):
            elapsed_time = time.perf_counter()  - start_time
            print("IDA* No solution. Limit:", limit, "Elapsed time:", elapsed_time)  # Debugging print
            return None, expanded_nodes, generated_nodes, elapsed_time, None  # No solution
        limit = result

def a_star(state, graph, heuristic):
    # A* algorithm for solving the traveling salesperson problem
    global generated_nodes, expanded_nodes
    generated_nodes = 0
    expanded_nodes = 0
    reached = {}
    priority_queue = [(0, state)]

    start_time = time.perf_counter() 

    while priority_queue:
        f, current_state = heapq.heappop(priority_queue)
        if is_goal(current_state, len(graph)):
            elapsed_time = time.perf_counter()  - start_time
            #print("A* Goal found. Cost:", f, "Elapsed time:", elapsed_time)  # Debugging print
            optimal_path = []
            while current_state:
                optimal_path.insert(0, current_state.current_id)
                current_state = current_state.parent  # Traverse back to the root
            return f, expanded_nodes, generated_nodes, elapsed_time, optimal_path  # Goal found

        current_hash = current_state.current_id * (2 ** len(graph))
        for i, visited in enumerate(current_state.visited):
            if visited:
                current_hash += 2 ** i

        if current_hash in reached and reached[current_hash] <= f:
            continue

        reached[current_hash] = f
        expanded_nodes += 1

        for successor, step_cost in successors(current_state, graph):
            h = heuristic(successor, graph)
            g = f - h + step_cost
            successor.parent = current_state  # Link to the parent state
            heapq.heappush(priority_queue, (g + h, successor))
            generated_nodes += 1

    elapsed_time = time.perf_counter()  - start_time
    print("A* No solution. Elapsed time:", elapsed_time)  # Debugging print
    return None, expanded_nodes, generated_nodes, elapsed_time, None  # No solution

def display_distance_matrix(graph):
    # Display the distance matrix for the given graph
    print("Distance Matrix:")
    for row in graph:
        print(row)
    print()

def main():
    # Main function to execute the algorithms and compare their performance
    random_seed = int(input("Enter a random seed: "))
    random.seed(random_seed)

    num_cities = int(input("Enter the number of cities: "))
    cities = list(range(num_cities))

    # Generate a complete graph with random distances
    graph = [[cost(i, j) for j in range(num_cities)] for i in range(num_cities)]

    display_distance_matrix(graph)

    start_state = State(num_cities)

    # Perform the algorithms and compare performance
    ida_star_result, ida_expanded_nodes, ida_generated_nodes, ida_elapsed_time, ida_optimal_path = ida_star(start_state, graph, h_zero, float('inf'))
    print("IDA* with h(n)=0 result:", ida_star_result)
    print("Expanded nodes:", ida_expanded_nodes)
    print("Generated nodes:", ida_generated_nodes)
    print("Elapsed time:", ida_elapsed_time)
    print("Optimal path:", ida_optimal_path)

    ida_star_min_out_result, ida_min_out_expanded_nodes, ida_min_out_generated_nodes, ida_min_out_elapsed_time, ida_min_out_optimal_path = ida_star(start_state, graph, min_out_heuristic, float('inf'))
    print("IDA* with min-out heuristic result:", ida_star_min_out_result)
    print("Expanded nodes:", ida_min_out_expanded_nodes)
    print("Generated nodes:", ida_min_out_generated_nodes)
    print("Elapsed time:", ida_min_out_elapsed_time)
    print("Optimal path:", ida_min_out_optimal_path)

    a_star_result, a_star_expanded_nodes, a_star_generated_nodes, a_star_elapsed_time, a_star_optimal_path = a_star(start_state, graph, h_zero)
    print("A* with h(n)=0 result:", a_star_result)
    print("Expanded nodes:", a_star_expanded_nodes)
    print("Generated nodes:", a_star_generated_nodes)
    print("Elapsed time:", a_star_elapsed_time)
    print("Optimal path:", a_star_optimal_path)

    a_star_min_out_result, a_star_min_out_expanded_nodes, a_star_min_out_generated_nodes, a_star_min_out_elapsed_time, a_star_min_out_optimal_path = a_star(start_state, graph, min_out_heuristic)
    print("A* with min-out heuristic result:", a_star_min_out_result)
    print("Expanded nodes:", a_star_min_out_expanded_nodes)
    print("Generated nodes:", a_star_min_out_generated_nodes)
    print("Elapsed time:", a_star_min_out_elapsed_time)
    print("Optimal path:", a_star_min_out_optimal_path)

if __name__ == "__main__":
    main()
