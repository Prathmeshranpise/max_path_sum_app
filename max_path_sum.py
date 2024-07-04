class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0

            left_sum = max(helper(node.left), 0)
            right_sum = max(helper(node.right), 0)

            current_sum = node.val + left_sum + right_sum
            max_sum = max(max_sum, current_sum)

            return node.val + max(left_sum, right_sum)

        max_sum = float('-inf')
        helper(root)
        return max_sum

if __name__ == "__main__":
    # Example 1: Binary tree [1, 2, 3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(Solution().maxPathSum(root1))  # Output: 6

    # Example 2: Binary tree [-10, 9, 20, None, None, 15, 7]
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    print(Solution().maxPathSum(root2))  # Output: 42
