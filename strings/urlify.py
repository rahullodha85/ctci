"""urlify: replaces and space in a string with %20"""


def urlify(s):
    """urlify: replaces and space in a string with %20"""
    s = list(s)

    space_count = get_space_count(s)

    for i in range(0, space_count * 2):
        s.append(" ")

    skip = space_count * 2
    j = 0
    for i in range(len(s) - 1, -1, -1):
        if j < skip:
            j += 1
        else:
            if s[i] == " ":
                s[i + space_count * 2] = "0"
                s[i - 1 + space_count * 2] = "2"
                s[i - 2 + space_count * 2] = "%"
                space_count -= 1
            else:
                if space_count > 0:
                    s[i + space_count * 2] = s[i]
                else:
                    break
    return ''.join(s)


def get_space_count(s):
    """get total space count in a string"""
    count = 0
    for char in s:
        if char == ' ':
            count += 1

    return count


if __name__ == "__main__":
    # Test cases
    test_strings = [
        "Mr John Smith",
        "Hello World",
        "Multiple   spaces"
    ]

    for test in test_strings:
        result = urlify(test)
        print(f"Original: '{test}'")
        print(f"URLified: '{result}'")
