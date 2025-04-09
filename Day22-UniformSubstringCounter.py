def matching_substring(string, k):
    string = list(string)
    match_count = 0
    match_window = []

    for end in range(len(string)):
        match_window.append(string[end])

        if end >= k -1:
            if len(set(match_window)) == 1:
                match_count += 1
            match_window.pop(0)

    print(match_count)

        
matching_substring("cvvvabcttdt", k=3)