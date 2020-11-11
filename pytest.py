import unittest
from DAG import *

class tests(unittest.TestCase):
    
    def test_NoRoot(self):
        self.assertEqual(None, lca(None, Node(1), Node(2)))
    
    
    def test_noConnectionNoLCA(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        root = Node(0)
        root.nodes = [node1, node2, node3]
        node4.nodes = [node5, node6]
        self.assertEqual(None, lca(root, node2, node6))

    def test_smallTreeTest(self):
        node1 = Node(1)
        node2 = Node(2)
        root = Node(0)
        root.nodes = [node1, node2]
        self.assertEqual(root, lca(root, node1, node2))


    def test_LargeTreeTest(self):
        root = Node(0)
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node5 = Node(5)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node9 = Node(9)
        node10 = Node(10)
        node11 = Node(11)
        node12 = Node(12)
        node13 = Node(13)
        root.nodes = [node1]
        node1.nodes = [node2, node3, node6, node9]
        node3.nodes = [node4, node5]
        node6.nodes = [node5, node7]
        node7.nodes = [node8]
        node9.nodes = [node10, node13]
        node10.nodes = [node11]
        node11.nodes = [node8, node12]
        node13.nodes = [node12]
        
        self.assertEqual(node6, lca(root, node5, node8))







if __name__ == '__main__':
    unittest.main()