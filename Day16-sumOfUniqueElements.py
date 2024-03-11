class Solution:
    def sumOfUnique(self, nums):
        occurences = {}

        for num in nums:
            if num not in occurences:
                occurences[num] = 1
            else:
                occurences[num] += 1

        unique_values = sum([key for key, value in occurences.items() if value == 1])

        return unique_values


obj = Solution()
obj.sumOfUnique([1,2,3,4,5])
        