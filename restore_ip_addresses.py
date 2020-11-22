s = "25525511135"


def put_dots(s):
    len_sting = len(s)
    if len_sting > 12:
        return []
    new_string = s
    res = []
    for dot_1 in range(1, len_sting - 2):
        for dot_2 in range(dot_1 + 1, len_sting - 1):
            for dot_3 in range(dot_2 + 1, len_sting):
                new_string = new_string[:dot_3] + "." + new_string[dot_3:]
                new_string = new_string[:dot_2] + "." + new_string[dot_2:]
                new_string = new_string[:dot_1] + "." + new_string[dot_1:]
                if check_valid(new_string):
                    res.append(new_string)
                new_string = s
    return res


def check_valid(new_string):
    new_string = new_string.split(".")
    for i in new_string:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True


print(put_dots(s))
