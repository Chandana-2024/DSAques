class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def mirror(l,r):

            if l is None and r is None:
                return True
            
            if l is None  or r is None:
                return False

            if l.val != r.val:
                return False

            return (mirror(l.left , r.right) and mirror(l.right, r.left))

        return mirror(root.left, root.right)

            