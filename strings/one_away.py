"""one away"""


def one_away(s1, s2):
    """checks if two strings are one variation away from each other or not"""

    m = len(s1)
    n = len(s2)

    if abs(m - n) > 1:
        return False
    i = 0
    j = 0
    count = 0
    while i < m and j < n:

        if s1[i] != s2[j]:
            if count == 1:
                return False

            if m > n:
                j += 1
            elif n > m:
                i += 1
            else:
                i += 1
                j += 1
            count += 1
        else:
            i += 1
            j += 1

    if i < m or j < n:
        count += 1

    return count == 1


print(one_away("abc", "abcd"))
