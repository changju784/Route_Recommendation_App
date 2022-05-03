from engines import Vertex, Edge, build_graph
import osmnx as ox
from engines.algorithms import Dijkstras
import warnings
warnings.filterwarnings("ignore")


def getShortestPath(Gc, source_node, target_node):
    d_path, d_len = Dijkstras.dijkstra(Gc, source_node, target_node)
    fig, ax = ox.plot_graph_route(Gc, d_path)

if __name__ == '__main__':
    start = (42.3570104, -71.0710964)
    end = (42.3568701, -71.0682476)
    Gc, src, target = build_graph.build_graph(start, end)
    print('==== Graph Loaded ====')
    getShortestPath(Gc, src, target)
    print('==== Complete ====')