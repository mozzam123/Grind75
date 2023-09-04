class Solution:
    def findTheDifference(self, s, t) :
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        # print(sorted_s)
        # print(sorted_t)

        for i in sorted_s:
            print(sorted_s[i])




obj = Solution()
obj.findTheDifference("abcd", "abcde")