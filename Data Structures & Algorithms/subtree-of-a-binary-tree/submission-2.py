# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False

        def checkSub(p, q) -> bool:
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if  p.val != q.val:
                return False 


       
            return checkSub(p.left, q.left) and checkSub(p.right,q.right)

        
        return checkSub(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    