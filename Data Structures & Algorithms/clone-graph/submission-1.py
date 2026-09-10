"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {} # Creates a new graph to track copied nodes

        # Depth First Search for new nodes in the original graph
        def dfs(node):
            # If the current node already exists in the copy graph, we return the copied node
            if node in oldToNew:
                return oldToNew[node]

            # Create the copy of the current node and add that to our copy graph
            copy = Node(node.val)
            oldToNew[node] = copy

            # If there are any neighbors for the current node, we append the neighbors to the current node in the copied graph
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            # We return the copied node
            return copy
        
        # We start the Depth First Search process if a graph exists, otherwise we return None
        return dfs(node) if node else None
            
