from engines.algorithms import BellmanFord
from engines import Vertex, Edge, build_graph
import osmnx as ox
import networkx as nx

def getShortestPath(src_lon, src_lat, dest_lon, dest_lat):
    src = (src_lon, src_lat)
    dest = (dest_lon, dest_lat)
    graph, vts, idx_vt_dict, src_vt, dst_vt = build_graph.build_graph(src, dest)
    route, directions, sum = BellmanFord.BellmanFord(vts, idx_vt_dict, src_vt, dst_vt)
    nc = (0.976, 0.411, 0.411, 1.0)
    background = (1.0, 1.0, 1.0, 0.0)
    graph_proj = ox.project_graph(graph)
    fig, ax = ox.plot_graph_route(graph_proj, route, node_color='w', node_size=0, edge_linewidth=0.5, route_color=nc,
                                  bgcolor=background, show=False, save=True, filepath="map.png")
    fig.savefig('result.png')


if __name__ == '__main__':
    getShortestPath(42.383807, -71.116494, 42.253763, -71.017757)