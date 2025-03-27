def not_present_in_array(nums):
    n = len(nums)
    nums = list(set(nums))
    not_present = []
    for i in range(1, n+1):
        if i not in nums:
            not_present.append(i)
            
    print(not_present)





not_present_in_array([2,2,3,3,5,5,6,6])