class Solution:
    def search(self, nums, target) :
        low,high = 0,len(nums) - 1
        while low <= high:
            mid = int((low + high)/2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid -1
            else:
                low = mid + 1

        return -1
        




    
obj = Solution()
obj.search([-1,0,3,5,9,12], 2)

        