import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import heapq as heapq
import math

def heuristics_diagonal(x1, x2, y1, y2):
    dx = abs(y2 - y1)
    dy = abs(x2 - x1)
    return (dx+dy) + ((math.sqrt(2) - 2)*min(dx, dy))


def heuristics_great_circle(x1, x2, y1, y2):
    radius = 3958.8
    gc_d = radius*math.acos((math.cos(x1)*math.cos(x2)*math.cos(y1-y2))+(math.sin(x1)*math.sin(x2)))
    return gc_d

def aStar(graph,source,target, h):
    heap = []
    distances = {source:0}
    visited = {}
    heapq.heappush(heap,(0,source))
    x2 = graph.nodes[target]['x']
    y2 = graph.nodes[target]['y']
    while heap:
        (h_d,v) = heapq.heappop(heap)
        d = distances[v]
        if v in visited:
            continue
        visited[v] = 1
        if v == target:
            break
        for u, e in graph.succ[v].items():
            cost = e[0]['length']
            x1 = graph.nodes[u]['x']
            y1 = graph.nodes[u]['y']
            heur_d = 0.0
            if h == 0:
                heur_d = heuristics_diagonal(x1, x2, y1, y2)
            else:
                heur_d = heuristics_great_circle(x1, x2, y1, y2)
            if(cost == None):
                continue
            dist = d + cost
            if u in visited:
                continue
            if u in distances:
                if dist < distances[u]:
                    distances[u] = dist
                    heapq.heappush(heap,(dist + heur_d,u))
            else:
               distances[u] = dist
               heapq.heappush(heap,(dist + heur_d,u))
    return distances

def asPath(graph,source,target, h):
    distances = aStar(graph, source, target, h)
    path = []
    v = target
    length = 0
    while v != source:
        path.insert(0,v)
        least = None
        for u, e in graph.pred[v].items():
            if u in distances:
                if least == None:
                    least = distances.get(u)
                    v = u
                    length = length + e[0]['length']
                    previous = e[0]['length']
                elif least > distances.get(u):
                    length = length + e[0]['length'] - previous
                    previous = e[0]['length']
                    least = distances.get(u)
                    v = u
    path.insert(0,v)
    return (path, length)