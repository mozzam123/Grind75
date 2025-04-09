def countGoodSubstrings(arr):
    arr = list(arr)
    count = 0
    k = 3
    window = []

    for right in range(len(arr)):
        window.append(arr[right])

        if right >= k - 1:
            if len(set(window)) == k:
                count += 1

            window.pop(0)
    
    print(count)

    
        



countGoodSubstrings("aababcabc")



