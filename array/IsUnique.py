def is_unique(s: str) -> bool:
    """
    Check if all characters in the string are unique.

    :param s: Input string
    :return: True if all characters are unique, False otherwise
    """
    char_set = set()
    for char in s:
        if ord(char) in char_set:
            return False
        char_set.add(ord(char))

    return True

if __name__ == "__main__":
    # Test cases
    test_strings = ["abcdefg", "hello", "world", "unique"]
    for test in test_strings:
        result = is_unique(test)
        print(f"Is '{test}' unique? {result}")