def lengthOfLongestSubstring(s):
    s = len(s)
    max_count = 0
    window = []

    for right in range(len(s)):
        
        while s[right] in window:
            window.pop(0)
        
        window.append(s[right])
        max_count = max(max_count, len(window))

    return max_count




lengthOfLongestSubstring("abcabcbb")