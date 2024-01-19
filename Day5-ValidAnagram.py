class Solution:
    def isAnagram(self, s, t):
        s = list(s)
        t = list(t)
        return sorted(s) == sorted(t)
        


            


obj = Solution()
obj.isAnagram('rakrota', 'tarrao')
