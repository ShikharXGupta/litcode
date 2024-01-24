# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
            def is_pseudo_palindrome(freq):
                odd_count = 0
                for count in freq.values():
                    if count % 2 != 0:
                        odd_count += 1
                    if odd_count > 1:
                        return False
                return True

            def dfs(node, freq):
                if not node:
                    return 0

                # Update frequency of the current digit
                freq[node.val] += 1

                # If it's a leaf node, check if the path is pseudo-palindromic
                if not node.left and not node.right:
                    if is_pseudo_palindrome(freq):
                        return 1
                    else:
                        return 0

                # Recursively explore left and right subtrees
                left_paths = dfs(node.left, freq.copy())
                right_paths = dfs(node.right, freq.copy())

                return left_paths + right_paths

            # Initialize frequency dictionary
            initial_freq = {i: 0 for i in range(1, 10)}

            # Start DFS from the root
            return dfs(root, initial_freq)