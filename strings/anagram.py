"""is anagram and its supporting functions"""


def is_anagram(s1, s2):
    """main is_anagram function"""
    if len(s1) != len(s2):
        return False

    d1 = get_char_freq(s1)
    d2 = get_char_freq(s2)

    return d1 == d2


def get_char_freq(s):
    """gets frequency of character as k-v pair dictionary"""
    d = {}
    for char in s:
        if char in d:
            d.update({char: d[char] + 1})
        else:
            d.update({char: 1})

    return d


print(is_anagram("abc", "bac"))
print(is_anagram("", "bac"))
