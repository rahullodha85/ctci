"""palindrom permutation"""


def is_palindrome_permutation(s):
    """checks if a string or one its permutation results into a palindrome string"""
    d = {}

    for c in s:
        if d.get(c):
            d[c] = d.get(c) + 1
        else:
            d[c] = 1

    count = 0
    for key in d:
        if d.get(key) % 2 != 0:
            count += 1

    return count <= 1


if __name__ == "__main__":
    print(is_palindrome_permutation("baba"))
