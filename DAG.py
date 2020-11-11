class Node:
  def __init__(self, key):
    self.key = key
    self.nodes = {}
    #self.color = "white"
    #self.count = 0
#   def changeColor(self, color):
#       self.color = color
  

# class DAG:
    
#     def __int__(self):
#         self.size = 0

#     def add(self, node):

#         if not node in self.nodeList:

#            self.nodeList.append(node)
#         return self


    
def proceed_through(root, n1, n2):
    paths = 0

    if root is None:
        return False, None
    
    

    if root.nodes is not None:
        for node in root.nodes:
            res = proceed_through(node, n1, n2)
            if res[1] is not None:
                return True, res[1]
            elif res[0] is True:
                paths += 1
    	
    if root.key is n1.key or root.key is n2.key:
        paths += 1 
    
    if paths > 1:
        return True, root

    # if paths == 1:
    #     return True, None
    
    return paths > 0, None
    
def lca(root, n1, n2):
    if root is None or n1 is None or n2 is None:
        return None
    finalResult = proceed_through(root, n1, n2)
    if finalResult[1] is not None:
        return finalResult[1]
    return None 
