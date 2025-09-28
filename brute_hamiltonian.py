def permutations(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result

# permutations([1, 2, 3]) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def brute_force_hamiltonian(graph):
    n = len(graph)
    edge = list(range(1, n)) 
    for perm in permutations(edge):
        path = [0] + perm + [0] # [1,2,3] -> [0,1,2,3,0]
        valid = True
        for i in range(n):
            if graph[path[i]][path[i+1]] == 0:
                valid = False
                break
        if valid:
            return path
    return None


# graph = [
#  [0, 1, 1, 0],  # connections of vertex 0
#  [1, 0, 1, 1],  # connections of vertex 1
#  [1, 1, 0, 0],  # connections of vertex 2
#  [0, 1, 0, 0]   # connections of vertex 3
# ]
# path = [0, 1, 2, 3, 0]

if __name__ == "__main__":
    # graph = [
    #     [0, 1, 0, 1],  # 0 connected to 1 and 3
    #     [1, 0, 1, 0],  # 1 connected to 0 and 2
    #     [0, 1, 0, 1],  # 2 connected to 1 and 3
    #     [1, 0, 1, 0]   # 3 connected to 0 and 2
    # ]
    # 0 —— 1
    # |    |
    # |    |
    # 3 —— 2


    graph = [
        [0, 1, 0, 0], # 0 connected to 1
        [1, 0, 1, 0], # 1 connected to 0 and 2
        [0, 1, 0, 1], # 2 connected to 1 and 3
        [0, 0, 1, 0]  # 3 connected to 2
    ]

    # 0 —— 1 —— 2 —— 3

    result = brute_force_hamiltonian(graph)
    if result:
        print("Hamiltonian cycle found:", result)
    else:
        print("No Hamiltonian cycle found.")
