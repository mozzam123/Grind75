def max_sum_of_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    start = 0

    for end in range(len(arr)):
        window_sum += arr[end]

        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[start]
            start += 1

    print(max_sum) 


max_sum_of_subarray([1,2,4,2,5,3], k=3)