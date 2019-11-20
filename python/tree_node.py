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