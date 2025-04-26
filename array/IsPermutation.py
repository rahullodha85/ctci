def is_permutation(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in t:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        else:
            return False

    return True

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("abc", "cba"),
        ("hello", "world"),
        ("123", "321"),
        ("aabbcc", "abcabc"),
        ("abcd", "abcde")
    ]

    for s, t in test_cases:
        result = is_permutation(s, t)
        print(f"Is '{s}' a permutation of '{t}'? {result}")