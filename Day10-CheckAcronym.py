class Solution:
    def isAcronym(self, words ,s):
        acr = ''
        for i in words:
            acr += i[0]

        if acr == s:
            print( 'true')
        else:
            print( 'false')
        

obj = Solution()
obj.isAcronym(["an","apple"], 'a')