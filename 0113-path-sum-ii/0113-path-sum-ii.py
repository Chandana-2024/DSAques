class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []
        path = []

        def dfs(node, remaining):

            if node is None:
                return

            # Choose
            path.append(node.val)
            remaining -= node.val

            # Check leaf
            if node.left is None and node.right is None:
                if remaining == 0:
                    ans.append(path[:])

                # Undo
                path.pop()
                return

            # Explore
            dfs(node.left, remaining)
            dfs(node.right, remaining)

            # Undo
            path.pop()

        dfs(root, targetSum)

        return ans