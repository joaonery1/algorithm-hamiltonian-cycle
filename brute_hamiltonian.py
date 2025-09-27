def permutations(lst):
    if len(lst) == 0:
        return [[]]
    result = []
    for i in range(len(lst)): # create a permutation list
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result


def brute_force_hamiltonian(graph):
    n = len(graph) # number of vertices
    vertices = list(range(1, n)) # vertices excluding the starting vertex 0
    for perm in permutations(vertices):
        path = [0] + perm + [0]
        valid = True
        for i in range(n):
            if graph[path[i]][path[i+1]] == 0:
                valid = False
                break
        if valid:
            return path
    return None


if __name__ == "__main__":
    # graph = [
    #     [0, 1, 1, 1],
    #     [1, 0, 1, 1],
    #     [1, 1, 0, 1],
    #     [1, 1, 1, 0]
    # ]

    graph = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]


    # graph = [
    #     [0, 1, 1, 0, 0],
    #     [1, 0, 1, 1, 0],
    #     [1, 1, 0, 0, 1],
    #     [0, 1, 0, 0, 1],
    #     [0, 0, 1, 1, 0]
    # ]

    result = brute_force_hamiltonian(graph)
    if result:
        print("Hamiltonian cycle found:", result)
    else:
        print("No Hamiltonian cycle found.")
