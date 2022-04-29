import collections
from engines import route
import queue

def BellmanFord(Vertex, idx_vt_dict, start, end):
    # q = collections.deque()
    q = queue.Queue()
    visited = [False]*len(Vertex)
    src = Vertex[idx_vt_dict.get(start)]
    visited[idx_vt_dict.get(start)] = True
    src.key = 0
    q.put(src)
    while q:
        node = q.get()
        visited[node.index] = False
        for edge in node.edges:
            print(edge.end, start)
            v = idx_vt_dict[edge.end]
            dv = node.key + edge.weight
            if Vertex[v].key > dv:
                Vertex[v].key = dv
                Vertex[v].parent = node.id
                Vertex[v].direction = [edge.name, edge.weight]
                if not visited[v]:
                    q.put(Vertex[v])
                    visited[v] = True
    node = Vertex[idx_vt_dict.get(end)]
    dist = node.key
    ro, way = route.calcRoute(node, Vertex, idx_vt_dict)  # Computer travel route and human readable directions
    return ro, way, dist




