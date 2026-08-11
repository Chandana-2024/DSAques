class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def m(l,r):
            if l is None and r is None:
                return True
            
            if l is None or r is None:
                return False
            
            if  l.val != r.val:
                return False
            
            return (m(l.left,r.right) and m(l.right,r.left) )
        
        return m(root.left,root.right)


            

            