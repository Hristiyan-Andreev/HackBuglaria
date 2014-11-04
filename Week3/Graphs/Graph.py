class Edge:

    def __init__(self, froms, to):
        self.froms = froms
        self.to = to

class Node:

    def __init__(self, name):
        self.name = name
        self.follows = []

class Graph:

    def __init__(self, name):
        self.name = name
        self.Nodes = {}
        self.Edges = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.Nodes:
            self.Nodes[node_a] = Node(node_a)
        if node_b not in self.Nodes:
            self.Nodes[node_b] = Node(node_b)

        self.Nodes[node_a].follows.append(self.Nodes[node_b])

        edge = Edge(self.Nodes[node_a], self.Nodes[node_b])
        self.Edges.append(edge)

    def get_neighbours(self, node):
        neighbours = []
        for node in self.Nodes[node].follows:
            neighbours.append(node.name)
        return neighbours

    def path_between(self, node_a, node_b):

        if self.Nodes[node_a].follows == []:
            return False
        for node in self.Nodes[node_a].follows:
            if node.name == node_b:
                return True
        for node in self.Nodes[node_a].follows:
            if self.path_between(node.name, node_b) is True:
                return True
        return False



