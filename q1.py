def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest_substr = ''
    for i in range(len(s)):
        for j in range(len(s) - i):
            substr = s[i:j+i+1]
            if substr == substr[::-1] and len(substr) > len(longest_substr):
                longest_substr = substr
    if len(longest_substr) >= 2:
        return longest_substr
    else:
        return ''