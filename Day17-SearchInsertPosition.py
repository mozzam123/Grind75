class Solution:
    def searchInsert(self,List,target):
        left = 0
        right = len(List) - 1

        while left <= right:
            mid = (left + right) // 2
            if List[mid] == target:
                return mid
            elif List[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If not found, `left` is the insert position
        return left
        
obj = Solution()
obj.searchInsert([1,3,5,6], 2)

        