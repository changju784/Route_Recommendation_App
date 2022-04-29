import collections


def BellmanFord(Vertex, idx_vt_dict, start, end):
    q = collections.deque()
    visited = [False]*len(Vertex)
    src = Vertex[idx_vt_dict.get(start)]
    visited[idx_vt_dict.get(start)] = True
    src.key = 0
    q.append(src)
    while q:
        node = q.popleft()
        visited[node.index] = False
        for edge in node.edges:
            v = idx_vt_dict[edge.end]
            dv = node.key + edge.weight
            if Vertex[v].key > dv:
                Vertex[v].key = dv
                Vertex[v].parent = node.id
                Vertex[v].direction = [edge.name, edge.weight]
                if not visited[v]:
                    q.append(Vertex[v])
                    visited[v] = True
    node = Vertex[idx_vt_dict.get(end)]
    dist = node.key
    route, directions = Routes.getRoute(node, Nodes, Map)  # Computer travel route and human readable directions
    return route, directions, dist




