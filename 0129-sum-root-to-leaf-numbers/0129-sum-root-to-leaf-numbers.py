# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans= []

        def dfs(node,total_sum):
            
            if node.left  is None and node.right is None:
                total_sum += str(node.val)
                ans.append(int(total_sum))
                return 
            
            total_sum +=str(node.val)
            
            if node.left:
                dfs(node.left,total_sum)

            if node.right:
                dfs(node.right,total_sum)
                
        dfs(root,"")
        return sum(ans)
