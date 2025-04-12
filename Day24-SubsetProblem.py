def subsets(nums):
    result = []

    def backtrack(index, current):
        if index == len(nums):
            result.append(current[:])
            print(result)
            return

        # Choice 1: Include
        current.append(nums[index])
        backtrack(index + 1, current)
        print('index: ', index)
        print('current: ', current)

    #     # Backtrack
    #     current.pop()

    #     # Choice 2: Don't include
    #     backtrack(index + 1, current)

    backtrack(0, [])
    # print(result) 


subsets([1,2,3])