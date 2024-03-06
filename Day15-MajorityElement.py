class Solution:
    def majorityElement(self, nums):
        occurence ={}
        for num in nums:
            if num not in occurence:
                occurence[num] =1
            else:
                occurence[num] += 1

        # Find the word with the maximum occurrence
        max_occurred_word = max(occurence, key=occurence.get)

        return max_occurred_word



obj = Solution()
obj.majorityElement([3,3,2])
        