from flask import Flask, request, send_file
from flask_cors import CORS
from engines import build_graph
from engines.Edge import edge
from engines.Vertex import vertex
import osmnx as ox
import networkx as nx
import main

FILE_PATH = "input/Boston.graphml"

# load graph at the beginning to save time for requests
app = Flask(__name__)
CORS(app)
map = nx.read_graphml(FILE_PATH, node_type=vertex["osmid"])
map = ox.io._convert_node_attr_types(map, vertex)
map = ox.io._convert_edge_attr_types(map, edge)
Gmap = ox.load_graphml(FILE_PATH)
print("==== Graph loaded ====")

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=['POST'])
def recommend_route():
    src_lng = float(request.form.get('src_lng'))
    src_lat = float(request.form.get('src_lat'))
    dest_lng = float(request.form.get('dest_lng'))
    dest_lat = float(request.form.get('dest_lat'))

    start = (src_lat, src_lng)
    end = (dest_lat, dest_lng)
    print("Start: ", start)
    print("End: ", end)
    Gc, src, target = build_graph.build_graph(Gmap, map, start, end)
    main.getShortestPath(Gc, src, target)
    print('==== Complete ====')

    return send_file("result.png")

if __name__ == '__main__':
    app.debug = False
    app.run(host="0.0.0.0")