from engines import Vertex, Edge, build_graph
import osmnx as ox
from engines.algorithms import Dijkstras, Astar
import time
import warnings
import sys
sys.stdin=open('input/input.txt','r')
warnings.filterwarnings("ignore")


def getShortestPath(Gc, source_node, target_node):
    # dijkstra
    td = time.time()
    d_path, d_len = Dijkstras.dijkstra(Gc, source_node, target_node)
    # fig, ax = ox.plot_graph_route(Gc, d_path)
    td1 = time.time()
    print('Total distance between ({0:.2f},{1:.2f}) and ({2:.2f},{3:.2f}) is {4:.2f}km.'.format(start[0], start[1], end[0], end[1], (d_len/1000.0)))
    print("Time for dijkstra: ", (td1-td), "\n")

    #A* diagonal
    tad = time.time()
    dp, dl = Astar.asPath(Gc, source_node, target_node, 0)
    # fig1, ax1 = ox.plot_graph_route(Gc, dp)
    tad1 = time.time()
    print('Total distance between ({0:.2f},{1:.2f}) and ({2:.2f},{3:.2f}) is {4:.2f}km.'.format(start[0], start[1], end[0], end[1], (dl/1000.0)))
    print("Time for A* diagonal distance heuristic function: ", (tad1-tad), "\n")

    #A* great circle
    tagc = time.time()
    dp2, dl2 = Astar.asPath(Gc, source_node, target_node, 1)
    # fig2, ax2 = ox.plot_graph_route(Gc, dp)
    tagc2 = time.time()
    print('Total distance between ({0:.2f},{1:.2f}) and ({2:.2f},{3:.2f}) is {4:.2f}km.'.format(start[0], start[1], end[0], end[1], (dl2/1000.0)))
    print("Time for A* Great Circle Distance heuristic function: ", (tagc2-tagc), "\n")
    fig_fin, ax_fin = ox.plot_graph_routes(Gc, [d_path, dp, dp2], route_colors = ["red", "green", "blue"])

if __name__ == '__main__':
    # start = (42.3570104, -71.0710964)
    # end = (42.3568701, -71.0682476)
    location = []
    for _ in range(2):
        lat, lon = map(float, input().split())
        location.append((lat,lon))
    start = (location[0][0],location[0][1])
    end = (location[1][0],location[1][1])
    Gc, src, target = build_graph.build_graph(start, end)
    print('==== Graph Loaded ====')
    getShortestPath(Gc, src, target)
    print('==== Complete ====')