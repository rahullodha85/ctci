def is_palindrome_permutation(s):
    d = dict()

    for c in s:
        if d.get(c):
            d[c] = d.get(c) + 1
        else:
            d[c] = 1

    count = 0
    for key in d.keys():
        if d.get(key) % 2 != 0:
            count += 1

    return count <= 1


if __name__ == "__main__":
    print(is_palindrome_permutation("baba"))
