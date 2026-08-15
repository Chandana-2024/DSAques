class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if root is None:
            return []
        
        ans = []
        
        stack = [(root, targetSum, [root.val])]
        
        while stack:
            node, current_sum, path = stack.pop()
            
            # Check leaf
            if not node.left and not node.right:
                if current_sum == node.val:
                    ans.append(path)
                continue
            
            # Right child
            if node.right:
                stack.append((
                    node.right,
                    current_sum - node.val,
                    path + [node.right.val]
                ))
            
            # Left child
            if node.left:
                stack.append((
                    node.left,
                    current_sum - node.val,
                    path + [node.left.val]
                ))
        
        return ans