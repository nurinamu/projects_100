# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __str__(self):
        result = "({})".format(self.val)
        if self.left != None :
            result += "-L[{}]".format(self.left)
        if self.right != None :
            result += "-R[{}]".format(self.right)
        return result

class Solution:
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val :
            return root
        if root.left != None :
            result = self.searchBST(root.left, val)
            if result != None :
                return result
        if root.right != None :
            result = self.searchBST(root.right, val)
            if result != None :
                return result
        return None

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(18)
    
    root.left = TreeNode(2)
    root.right = TreeNode(22)
    root.right.right = TreeNode(63)
    root.right.right.right = TreeNode(84)

    # [18,2,22,null,null,null,63,null,84,null,null]

    print(sol.searchBST(root, 63))