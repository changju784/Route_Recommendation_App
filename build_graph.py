import osmnx as ox
import networkx as nx
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from Vertex import Vertex
from Edge import Edge
import warnings
warnings.filterwarnings("ignore")

'''
https://automating-gis-processes.github.io/site/notebooks/L6/network-analysis.html
'''

def build_graph(source,destination):

	place_name = "Boston, Massachusetts, USA"
	try:
		graph = ox.graph_from_place(place_name, network_type='drive')
		print('Loaded Boston Map Successfully')
	except:
		print('Map Loading Failed')
		print('Please check your internet connection')

	# Get source and destination vertexes
	src_vt = ox.get_nearest_node(graph, source, method='euclidean')
	dst_vt = ox.get_nearest_node(graph, destination, method='euclidean')
	dst_coordinate = (graph.nodes()[dst_vt]['x'], graph.nodes()[dst_vt]['y'])

	# Extract vertexes from the graph
	raw_vertexes = list(graph.nodes)
	vts = list()
	idx_vt_dict = dict()

	for idx, vt in enumerate(raw_vertexes):
		vertex = Vertex(idx, vt)
		vertex.coordinate = (graph.nodes()[vt]['x'], graph.nodes()[vt]['y'])

		# Check whether current vertex is a source or destination
		# Source = 1, Destination = 2
		if vt == src_vt:
			vertex.vertex_type = 1
		elif vt == dst_vt:
			vertex.vertex_type = 2

		# Calculate distance from current vertex
		if vertex.vertex_type == 2:
			vertex.distance = 0
		else:
			vertex.distance = ox.distance.euclidean_dist_vec(vertex.coordinate[0], vertex.coordinate[1],
														 dst_coordinate[0], dst_coordinate[1])
		raw_edges = graph.adj[vt]
		edges = list(graph.adj[vt])
		for edge in edges:
			myEdge = Edge(name=raw_edges[edge][0].get("name"), start=vt, end=edge,
						  weight=raw_edges[edge][0].get("length"))
			vertex.edges.append(myEdge)
			idx_vt_dict[vertex] = idx
			vts.append(vertex)
	return graph, vts, idx_vt_dict, src_vt, dst_vt

if __name__=='__main__':
	build_graph((42.383807,-71.116494 ),(42.253763,-71.017757))







