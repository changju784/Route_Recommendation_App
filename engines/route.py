import osmnx as ox

def calcRoute(node, Vertex, idx_vt_dict):
    route = []
    way = []
    while node.vertex_type != 1:
        route.append(node.id)
        par = node.parent
        if par == -1:
            print("Error!")
            return None, None
        else:
            bearing = ox.bearing.get_bearing(Vertex[idx_vt_dict.get(par)].coordinate, node.coordinate)
            node.direction.append(deg_dir(bearing))
            node.direction.append(bearing)
            way.append(node.direction)
            node = Vertex[idx_vt_dict.get(par)]
    route.append(node.id)
    route.reverse()
    way.reverse()
    way = conversion(way)
    return route, way


def conversion(way):
    try:
        combine = [way[0]]  # Combines directions on same street
    except:
        print("Error")
        exit(0)

    # Combine directions along same street
    for i in range(1, len(way)):
        idx = len(combine) - 1
        # Check for same street and travel distance along street if street is same
        # if directions[i][0] == combo[idx][0] and directions[i][2] == combo[idx][2]:
        if way[i][0] == combine[idx][0]:
            combine[idx][1] += way[i][1]
        else:
            combine.append(way[i])

    # Generate Strings from condensed directions
    ret = []
    for i in range(0, len(combine)):
        if combine[i][0] is None and i < len(combine)-1:
            # Add turn by turn
            if i > 0:
                turn = turn_dir(combine[i - 1], combine[i])
                ret.append(turn + f"onto {combine[i+1][0]}")
            ret.append(f"Continue {combine[i][2]} onto {combine[i+1][0]} for {int(combine[i][1])} meters")
        else:
            # Add turn by turn
            if i > 0:
                turn = turn_dir(combine[i - 1], combine[i])
                ret.append(turn + f"onto {combine[i][0]}")
            ret.append(f"Travel {combine[i][2]} for {int(combine[i][1])} meters along {combine[i][0]}")

    # Debug -- remove for production
    # sum = 0
    # for item in combo:
    #     sum += item[1]
    # print(sum)
    return ret

# Converts degrees to a cardinal direction
def deg_dir(degrees):
    degrees = int(degrees)

    if degrees == 0:
        return "N"
    elif 0 < degrees < 90:
        return "NE"
    elif degrees == 90:
        return "E"
    elif 90 < degrees < 180:
        return "SE"
    elif degrees == 180:
        return "S"
    elif 180 < degrees < 270:
        return "SW"
    elif degrees == 270:
        return "W"
    elif 270 < degrees < 360:
        return "NW"
    else:
        return "N"


def turn_dir(n1, n2):
    if n1[2] == n2[2]:
        temp = n1[3] - n2[3]
        if temp == 0:
            return "straight "
        elif temp > 0:
            return "sleft "
        else:
            return "sright "

    else:
        temp = n1[3] - n2[3]
        if temp == 0:
            return "straight "
        elif temp > 0:
            return "tleft "
        else:
            return "tright "