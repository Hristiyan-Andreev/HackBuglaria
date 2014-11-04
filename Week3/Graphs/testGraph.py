from Graph import Node
from Graph import Edge
from Graph import Graph
import unittest

class TestGraph(unittest.TestCase):

    def test_Edge_init(self):
        edge1 = Edge("A", "B")
        self.assertEqual(edge1.froms, "A")
        self.assertEqual(edge1.to, "B")

    def test_Node_init(self):
        node1 = Node("A")
        self.assertEqual(node1.name, "A")

    def test_Graph_init(self):
        graph1 = Graph("Graphec")
        self.assertEqual(graph1.name, "Graphec")
        self.assertEqual(graph1.Nodes, {})
        self.assertEqual(graph1.Edges, [])

    def test_add_edge(self):
        graph1 = Graph("Graphec")
        graph1.add_edge("A", "B")
        self.assertEqual(graph1.Nodes["A"].name, "A")
        self.assertEqual(graph1.Nodes["B"].name, "B")
        self.assertEqual(graph1.Edges[0].froms, graph1.Nodes["A"])
        self.assertEqual(graph1.Edges[0].to, graph1.Nodes["B"])

    def test_get_neighbours(self):
        graph1 = Graph("Graphec")
        graph1.add_edge("A", "B")
        graph1.add_edge("A", "C")
        neighbours = ["B", "C"]
        self.assertEqual(graph1.get_neighbours("A"), neighbours)

    def test_path_between(self):
        graph1 = Graph("Graphec")
        graph1.add_edge("A", "B")
        graph1.add_edge("A", "C")
        graph1.add_edge("C", "D")
        graph1.add_edge("D", "E")
        graph1.add_edge("D", "F")
        graph1.add_edge("P", "O")
        self.assertFalse(graph1.path_between("A", "O"))
if __name__ == '__main__':
    unittest.main()
