def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    max_length = max(len(a), len(b))
    a = '0' * (max_length - len(a)) + a[2:]
    b = '0' * (max_length - len(b)) + b[2:]
    
    res = ''
    tracker = 0
    for i in range(-1, -len(a)-1, -1):
        bit_sum = int(a[i]) + int(b[i]) + tracker
        tracker = bit_sum // 2
        res = str(bit_sum % 2) + res
    if tracker != 0:
        res = '1' + res    
    while res.startswith('0'):
        res = res[1:]
    return '0b' + res