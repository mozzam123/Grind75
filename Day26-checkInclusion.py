from collections import Counter

def checkInclusion(s1, s2):
    k = len(s1)
    s1_count = Counter(s1)  # frequency of s1
    window_count = Counter()

    for right in range(len(s2)):
        window_count[s2[right]] += 1  # add the current char to window

        # shrink window if it's bigger than k
        if right >= k:
            left_char = s2[right - k]
            if window_count[left_char] == 1:
                del window_count[left_char]  # clean it up
            else:
                window_count[left_char] -= 1

        # check if frequencies match
        if window_count == s1_count:
            return True

    return False

# test it
print(checkInclusion(s1="ab", s2="eidbaooo"))  # Output: True
