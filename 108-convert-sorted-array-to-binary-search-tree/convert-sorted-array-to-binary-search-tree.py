class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            # Pick the middle element to ensure height balance
            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            # Recursively build left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(nums) - 1)