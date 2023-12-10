"""is unique"""


def is_unique(s):
    """checks if characters in string are unique"""

    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True
