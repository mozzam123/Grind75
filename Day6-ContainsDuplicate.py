class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


obj = Solution()
obj.containsDuplicate([1,5,-2,-4,0])

        