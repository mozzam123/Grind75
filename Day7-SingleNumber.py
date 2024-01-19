class Solution:

    def singleNumber(self, nums):
        if len(nums) <= 1:
            return nums[0]
        set_num = list(set(nums))
        for i in set_num:
            if i in nums:
                nums.remove(i)

        for i in set_num:
            if i not in nums:
                return i


obj = Solution()
obj.singleNumber([2,2,1])
        