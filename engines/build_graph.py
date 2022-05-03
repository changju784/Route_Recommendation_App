from shapely.geometry import Point
import osmnx as ox
import networkx as nx
import geopandas as gpd
from engines.Edge import edge
from engines.Vertex import vertex
import warnings
warnings.filterwarnings("ignore")


def build_graph(start, end):
    map = nx.read_graphml("dataset/Boston.graphml", node_type=vertex["osmid"])
    map = ox.io._convert_node_attr_types(map, vertex)
    map = ox.io._convert_edge_attr_types(map, edge)

    if "node_default" in map.graph:
        del map.graph["node_default"]
    if "edge_default" in map.graph:
        del map.graph["edge_default"]

    Gp = ox.project_graph(map)
    Gc = ox.consolidate_intersections(Gp, rebuild_graph=True, tolerance=20, dead_ends=False)

    lats = [start[0], end[0]]
    longs = [start[1], end[1]]
    points_list = list()
    for lat, long in zip(lats,longs):
        points_list.append(Point(long,lat))
    points = gpd.GeoSeries(points_list, crs='epsg:4326')
    # Transform all points in all objects
    transformed_points = points.to_crs(Gp.graph['crs'])

    source_node = ox.get_nearest_node(Gc, (transformed_points[0].y, transformed_points[0].x), method = 'euclidean')
    target_node = ox.get_nearest_node(Gc, (transformed_points[1].y, transformed_points[1].x), method = 'euclidean')
    return Gc, source_node, target_node