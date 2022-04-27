'''
====================================
 :mod:`const_path` {constant values}
====================================
'''

import os
cur_path = os.path.dirname(os.path.abspath(__file__))

path = {
    "graph_path" : os.path.join(cur_path, "../dataset/Boston.graphml")
}