from shapely.geometry import Point
import osmnx as ox
import networkx as nx
import geopandas as gpd
from engines.Edge import edge
from engines.Vertex import vertex
import warnings
warnings.filterwarnings("ignore")

FILE_PATH = "input/Boston.graphml"

def calc_latlong(Graph, lat, long):
    target_xy = (lat, long)
    target_node = ox.get_nearest_node(Graph, target_xy, method='euclidean')
    return target_node

def build_graph(G, Map, start, end):
    # map = nx.read_graphml(FILE_PATH, node_type=vertex["osmid"])
    # map = ox.io._convert_node_attr_types(map, vertex)
    # map = ox.io._convert_edge_attr_types(map, edge)
    # Gmap = ox.load_graphml(FILE_PATH)
    Gmap = G
    map = Map

    #Test if there is a path between start and end
    start_node = calc_latlong(Gmap,start[0],start[1])
    end_node = calc_latlong(Gmap,end[0],end[1])
    if not nx.algorithms.shortest_paths.generic.has_path(Gmap, start_node, end_node):
        print("There is no path between two points in Boston.")
        exit(1)
    else:
        print("There is a path between two points.")
        print("Calculating the path now....")

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