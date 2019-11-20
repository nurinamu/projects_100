from tree_node import TreeNode

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        result = True 
        if root.left != None :
            if root.left.val == root.val :
                result &= self.isUnivalTree(root.left)
            else :
                return False

        if root.right != None :
            if root.right.val == root.val :
                result &= self.isUnivalTree(root.right)
            else :
                return False

        return result
