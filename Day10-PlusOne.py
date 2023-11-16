class Solution:
    def plusOne(self, digits):
        num_list = []
        single_number = list(str(int(''.join(map(str, digits))) + 1))
        for i in single_number:
            num_list.append(int(i))
        return num_list
        
        
        

obj = Solution()
obj.plusOne([9])
        