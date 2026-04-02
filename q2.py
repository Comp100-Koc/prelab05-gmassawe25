def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1
    return s