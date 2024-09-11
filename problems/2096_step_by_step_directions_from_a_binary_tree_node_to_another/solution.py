class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def get_directions(
        root: TreeNode | None,
        start_value: int,
        dest_value: int
    ) -> str:
        def find_path(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            path.append('L')
            if find_path(root.left, value, path):
                return True
            path.pop()

            path.append('R')
            if find_path(root.right, value, path):
                return True
            path.pop()

            return False

        def find_lca(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = find_lca(root.left, p, q)
            right = find_lca(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        start_path = []
        dest_path = []
        find_path(root, start_value, start_path)
        find_path(root, dest_value, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == \
            dest_path[i]:
            i += 1

        lca_to_start = ['U'] * (len(start_path) - i)
        lca_to_dest = dest_path[i:]

        return ''.join(lca_to_start + lca_to_dest)


solution = Solution()

# Example 1 tree nodes:
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

example_1 = solution.get_directions(root, start_value=3, dest_value=6)
print(f'Example 1 output (should be UURL): {example_1}')

# Example 2 tree nodes:
root = TreeNode(2)
root.left = TreeNode(1)

example_2 = solution.get_directions(root, start_value=2, dest_value=1)
print(f'Example 2 output (should be L): {example_2}')
