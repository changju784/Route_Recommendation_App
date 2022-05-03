from shapely.geometry import Point
import osmnx as ox
import networkx as nx
import geopandas as gpd
from engines.Edge import edge
from engines.Vertex import vertex
import warnings
warnings.filterwarnings("ignore")


def build_graph(start, end):
    # start = (42.0,-71.0)
    # end = (42.4,-71.4)
    G = nx.read_graphml("dataset/bigBoston.graphml", node_type=vertex["osmid"])
    G = ox.io._convert_node_attr_types(G, vertex)
    G = ox.io._convert_edge_attr_types(G, edge)

    if "node_default" in G.graph:
        del G.graph["node_default"]
    if "edge_default" in G.graph:
        del G.graph["edge_default"]

    Gp = ox.project_graph(G)
    Gc = ox.consolidate_intersections(Gp, rebuild_graph=True, tolerance=20, dead_ends=False)

    lats = [start[0], end[0]]
    lngs = [start[1], end[1]]
    points_list = [Point((lng, lat)) for lat, lng in zip(lats, lngs)]
    points = gpd.GeoSeries(points_list, crs='epsg:4326')
    points_proj = points.to_crs(Gp.graph['crs'])

    source_node = ox.get_nearest_node(Gc, (points_proj[0].y, points_proj[0].x), method = 'euclidean')
    target_node = ox.get_nearest_node(Gc, (points_proj[1].y, points_proj[1].x), method = 'euclidean')
    return Gc, source_node, target_node