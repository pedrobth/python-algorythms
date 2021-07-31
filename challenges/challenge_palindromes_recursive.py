def is_palindrome_recursive(word, low_index, high_index):
    if not word:
        print('not word')
        return False
    if len(word) >= 2:
        if word[0] != word[-1]:
            return False
        word_trimmed = word[1:-1]
        return is_palindrome_recursive(
            word_trimmed, 0, len(word_trimmed) - 1
        )
    else:
        return True
