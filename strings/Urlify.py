def urlify(s):

    s = list(s)

    space_count = get_space_count(s)

    for i in range(0, space_count*2):
        s.append(" ")

    skip = space_count*2
    j = 0
    for i in range(len(s)-1, -1, -1):
        if j < skip:
            j += 1
        else:
            if s[i] == " ":
                s[i + space_count*2] = "0"
                s[i-1 + space_count*2] = "2"
                s[i-2 + space_count*2] = "%"
                space_count -=1
            else:
                s[i + space_count*2] = s[i]
    return ''.join(s)


def get_space_count(s):
    count = 0
    for char in s:
        if char == ' ':
            count += 1

    return count

print(urlify("Hello world hi!"))
