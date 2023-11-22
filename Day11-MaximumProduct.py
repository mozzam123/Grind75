class Solution:
    def maximumProduct(self, nums):

        nums.sort()
        max_product_case1 = nums[-1] * nums[-2] * nums[-3]

        max_product_case2 = nums[0] * nums[1] * nums[-1]

        return max(max_product_case1, max_product_case2)


obj = Solution()
obj.maximumProduct([-100,-1,-1,2,3,4])
        