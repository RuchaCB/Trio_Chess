
def centroid(vertexes):
     _x_list = [vertex [0] for vertex in vertexes]
     _y_list = [vertex [1] for vertex in vertexes]
     _len = len(vertexes)
     _x = sum(_x_list) / _len
     _y = sum(_y_list) / _len
     return(_x, _y)

""" polygon_data = ((0, 0), (4, 0), (4, 4), (0, 4))
print(centroid(polygon_data)) """