from typing import List

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def traverse(self, root: Node, result: List) :
        if root.children != None :
            for child in root.children :
                self.traverse(child, result)
        result.append(root.val)

    def postorder(self, root: Node) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
