class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # Start from the next index after i
                summed = nums[i] + nums[j]
                if summed == target:
                    return [i, j]
                


obj = Solution()
obj.twoSum([2,7,11,15], 9)