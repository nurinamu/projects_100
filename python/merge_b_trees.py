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
    
    def next(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t2 != None :
            if t1 != None :                    
                t1.val += t2.val
                if t2.left != None:
                    if t1.left != None:
                        t1.left = self.next(t1.left, t2.left)
                    else :
                        t1.left = t2.left
                if t2.right != None:
                    if t1.right != None:
                        t1.right = self.next(t1.right, t2.right)
                    else:
                        t1.right = t2.right
            else :
                t1 = TreeNode(t2.val)
                t1.left = t2.left
                t1.right = t2.right
        return t1    

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.next(t1, t2)

if __name__ == "__main__":
    solution = Solution()

    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.left.right = TreeNode(4)
    t2.right = TreeNode(3)
    t2.right.right = TreeNode(7)

    print(solution.mergeTrees(t1, t2))
    print(solution.mergeTrees(TreeNode(1),None))
    print(solution.mergeTrees(None, TreeNode(1)))
    print(solution.mergeTrees(None,None))