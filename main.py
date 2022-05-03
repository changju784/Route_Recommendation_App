from engines import Vertex, Edge, build_graph
import osmnx as ox
from engines.algorithms import Dijkstras, Astar
import time
import warnings
warnings.filterwarnings("ignore")


def getShortestPath(Gc, source_node, target_node):
    # dijkstra
    td = time.time()
    d_path, d_len = Dijkstras.dijkstra(Gc, source_node, target_node)
    fig, ax = ox.plot_graph_route(Gc, d_path)
    td1 = time.time()
    print("time for dijkstra: ", (td1-td)/100)

    #A* diagonal
    tad = time.time()
    dp, dl = Astar.asPath(Gc, source_node, target_node, 0)
    fig1, ax1 = ox.plot_graph_route(Gc, dp)
    tad1 = time.time()
    print("time for A* diagonal distance heuristic function: ", (tad1-tad)/100)

    #A* great circle
    tagc = time.time()
    dp2, dl2 = Astar.asPath(Gc, source_node, target_node, 1)
    fig2, ax2 = ox.plot_graph_route(Gc, dp)
    tagc2 = time.time()
    print("time for A* Great Circle Distance heuristic function: ", (tagc2-tagc)/100)

if __name__ == '__main__':
    start = (42.3570104, -71.0710964)
    end = (42.3568701, -71.0682476)
    Gc, src, target = build_graph.build_graph(start, end)
    print('==== Graph Loaded ====')
    getShortestPath(Gc, src, target)
    print('==== Complete ====')