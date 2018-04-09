def longest_substring_without_repeating_characters(s):
    character = dict()
    i = j = 0
    max_len = 0
    while i < len(s):
        if s[i] in character:
            j = character[s[i]]
        max_len = max(max_len, i - j)
        character[s[i]] = i
        i += 1
    return max_len


if __name__ == '__main__':
    print longest_substring_without_repeating_characters('abcabcbb')
    print longest_substring_without_repeating_characters('bbbbb')
    print longest_substring_without_repeating_characters('pwwkew')
