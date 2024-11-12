def topologicalSortUtil(v, adj, visited, stack):
    visited[v] = True

    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    stack.append(v)

def topologicalSort(adj, V):
    stack = []

    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    print("Topological sorting of the graph:", end=" ")
    while stack:
        print(stack.pop(), end="\t")

if __name__ == "__main__":
    V = 4

    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]

    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])

    topologicalSort(adj, V)