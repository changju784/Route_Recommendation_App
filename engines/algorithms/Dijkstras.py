import heapq as heapq

def dijkstra(graph,source,target):
    graph_succ, graph_pred = graph.succ, graph.pred
    heap = []
    visited = {}
    distances = {source: 0}
    heapq.heappush(heap, (0, source))
    while heap:
        d, v = heapq.heappop(heap)
        if v in visited:
            continue
        visited[v] = 1
        if v == target:
            break
        for u, e in graph_succ[v].items():
            cost = e[0]['length']
            if not cost:
                continue
            dist = d + cost
            if u not in visited:
                if u in distances:
                    if dist < distances[u]:
                        distances[u] = dist
                        heapq.heappush(heap,(dist,u))
                else:
                   distances[u] = dist
                   heapq.heappush(heap,(dist,u))
    # Compute Path from backwards
    path = []
    v = target
    length = 0
    while True:
        if v == source:
            break
        path.insert(0, v)
        min = float('inf')
        for u, e in graph_pred[v].items():
            if u in distances:
                if min == float('inf'):
                    min = distances.get(u)
                    v = u
                    length += e[0]['length']
                    prev = e[0]['length']
                elif distances.get(u) < min:
                    length += e[0]['length'] - prev
                    prev = e[0]['length']
                    min = distances.get(u)
                    v = u
    path.insert(0, v)
    return path, length
