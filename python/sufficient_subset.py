from tree_node import TreeNode

class Solution:

    def traverseWithSum(self, parent: TreeNode, node: TreeNode, limit: int, sum: int, isLeft: bool) -> bool:
        left = False
        right = False
        if node.left == None and node.right == None :
            if sum + node.val < limit :
                print("remove({}) : {}".format(node.val, isLeft))
                if isLeft :
                    parent.left = None
                else :
                    parent.right = None
                return False
            else :
                print(sum)
                return True

        if node.left != None :
            left = self.traverseWithSum(node, node.left, limit, sum + node.val, True)
        
        if node.right != None :
            right = self.traverseWithSum(node, node.right, limit, sum + node.val, False)
        
        if not right and not left :
            if parent != None :
                if isLeft :
                    parent.left = None
                else :
                    parent.right = None
            return False

        return True

    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if self.traverseWithSum(None, root, limit, 0, True) :
            return root
        else :
            return None

if __name__ == "__main__":
    sol = Solution()

    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(-99)
    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)
    tree.left.right.left = TreeNode(-99)
    tree.left.right.right = TreeNode(-99)

    tree.right.left = TreeNode(-99)
    tree.right.right = TreeNode(7)
    tree.right.left.left = TreeNode(12)
    tree.right.left.right = TreeNode(13)
    tree.right.right.left = TreeNode(-99)
    tree.right.right.right = TreeNode(14)
    
    # tree.left = TreeNode(2)
    # tree.left.left = TreeNode(-5)
    # tree.right = TreeNode(-3)
    # tree.right.left = TreeNode(4)

    print(sol.sufficientSubset(tree, 1))

