##### IMPORT THE REQUIRED LIBRARIES #####
import json
import numpy as np

##### DECLARE THE WIREFRAME OBJECT #####
class Wireframe(object):
    """
        @summary    This constructor takes a JSON file containing the wireframe nodes and
                    connections data. The JSON file is expected to be in a very particular
                    format.

        @param      filename    This is the filepath and filename to the wireframe's JSON
                                file.
    """
    def __init__(self, filename):
        self.filename = filename
        
        # Read the JSON data and get a list of the nodes used by the wireframe.
        with open(filename, "r") as f:
            data = json.loads(f.read())

        nodes = data["nodes"]

        # store the edges using a simple adjacency list.
        self._adj_list = {}

        for edge in data["edges"]:
            start = nodes.index(edge["start"])
            end = nodes.index(edge["end"])
			
            if not str(start) in self._adj_list:
                self._adj_list[str(start)] = [end]
            else:
                self._adj_list[str(start)].append(end)
            if not str(end) in self._adj_list:
                self._adj_list[str(end)] = [start]
            else:
                self._adj_list[str(end)].append(start)

        # create an Nx4 matrix to store the nodes list. This allows the graphics engine
        # to run transformations much faster.
        self.nodes = np.zeros((len(nodes), 4))
        for i in range(len(nodes)):
            self.nodes[i, 0] = nodes[i]["x"]
            self.nodes[i, 1] = nodes[i]["y"]
            self.nodes[i, 2] = nodes[i]["z"]
            self.nodes[i, 3] = 1

        # delete the list of nodes, since it isn't being used anymore.
        del nodes

    """
        @summary    Moves the entire wireframe object over 'd' units in the direction
                    of the specified axis.

        @param      axis        The axis to move the wireframe in the right direction of.
        @param      distance    The number of units to move the object. You can specifiy
                                either positive or negative units.
    """
    def translate(self, axis, distance):
        if axis in ["x", "y", "z"]:
            # Create the transformation matrix for the given operation.
            if axis == 'x':
                matrix = np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, distance, 0, 0, 1]).reshape(4,4)
            elif axis == 'y':
                matrix = np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, distance, 0, 1]).reshape(4,4)
            elif axis == 'z':
                matrix = np.array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, distance, 1]).reshape(4,4)

            # compute the dot product on the nodes matrix.
            self.nodes = np.dot(self.nodes, matrix)
        else:
            raise Exception("Invalid Axis Given.")

    """
        @summary    Scales the entire wireframe by a given factor. This is the same as
                    either zooming in or out.

        @param      factor  This is the amount of zoom in or out by. If the given factor
                            is less than 1.0, then scaling will cause the wireframe to 
                            zoom out. If the factor is greater than 1.0, then scaling
                            will cause the wireframe to zoom in.
    """
    def scale(self, factor):
        # create the transformation matrix and apply it to all the nodes.
        matrix = np.array([factor, 0, 0, 0, 0, factor, 0, 0, 0, 0, factor, 0, 0, 0, 0, 1]).reshape(4, 4)
        self.nodes = np.dot(self.nodes, matrix)

    """
        @summary    Rotate the entire wirefame about the x-axis by a given 
                    amount of radians.

        @param      radians The distance to rotate the wireframe object, given in
                    radians.
    """
    def rotateX(self, radians):
        # compute and create the transformation matrix.
        c = np.cos(radians)
        s = np.sin(radians)
        matrix = np.array([1, 0, 0, 0, 0, c, -s, 0, 0, s, c, 0, 0, 0, 0, 1]).reshape(4, 4)

        # apply the transformation matrix to the nodes.
        self.nodes = np.dot(self.nodes, matrix)

    """
        @summary    Rotate the entire wirefame about the y-axis by a given 
                    amount of radians.

        @param      radians The distance to rotate the wireframe object, given in
                    radians.  
    """
    def rotateY(self, radians):
        # compute and create the transformation matrix.
        c = np.cos(radians)
        s = np.sin(radians)
        matrix = np.array([c, 0, s, 0, 0, 1, 0, 0, -s, 0, c, 0, 0, 0, 0, 1]).reshape(4, 4)

        # apply the transformation matrix to the nodes.
        self.nodes = np.dot(self.nodes, matrix)

    """
        @summary    Rotate the entire wirefame about the z-axis by a given 
                    amount of radians.

        @param      radians The distance to rotate the wireframe object, given in
                    radians.
    """
    def rotateZ(self, radians):
        # compute and create the transformation matrix.
        c = np.cos(radians)
        s = np.sin(radians)
        matrix = np.array([c, -s, 0, 0, s, c, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]).reshape(4, 4)

        # apply the transformation matrix to the nodes.
        self.nodes = np.dot(self.nodes, matrix)

    def __str__(self):
        return "Wireframe {}".foramt(self.filename)