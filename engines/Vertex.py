'''
Vertex Class
: Contains information of a vertex in a map
'''

class Vertex:
	def __init__(self, index, ID):
		self.index = index #vertex index from vertex list
		self.id = ID #vertex id
		self.coordinate = (None, None) # Longitude, Latitude
		self.distance = -1
		self.vertex_type = 0 #1 = source, #2 = destination
		self.edges = list() #connected edges
		self.key = 100000
		self.parent = -1
		self.direction = [None, None, None] # name, length, bearing from parents to the node

