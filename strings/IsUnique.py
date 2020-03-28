def is_unique(s):

    char_set = set()
    for char in s:
        if char in char_set:
            return False
        else:
            char_set.add(char)
    return True
