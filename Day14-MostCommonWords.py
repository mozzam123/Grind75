def mostCommonWord(paragraph, banned):
    # Replace non-alphabetic characters with space and split
    words = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in paragraph).split()

    occurrence = {}

    for word in words:
        # Remove any non-alphabetic characters from the word
        word = ''.join(char for char in word if char.isalpha())

        if word and word not in banned:
            occurrence[word] = occurrence.get(word, 0) + 1

    # Find the word with the maximum occurrence
    max_occurred_word = max(occurrence, key=occurrence.get)

    print(max_occurred_word)

# Example usage:
mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"])
