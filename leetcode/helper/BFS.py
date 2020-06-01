def BFS(V, Adj, s):
    level = {
        's': 0
    }
    parent = {
        's': None
    }

    i = 1
    frontier = [s]
    while frontier:
        next_ = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next_.append(v)
        frontier = next_
        i += 1
