OPEN_BRACKETS = ['(', '{', '[']
CLOSE_BRACKETS = [')', '}', ']']


def check_brackets_closed(brackets_text):
    result = []
    if not brackets_text:
        return True
    elif brackets_text[0] in CLOSE_BRACKETS:
        return False
    for bracket in brackets_text:
        if bracket in OPEN_BRACKETS:
            result.append(OPEN_BRACKETS.index(bracket))
        elif bracket in CLOSE_BRACKETS:
            if len(result) != 0 and result[-1] == CLOSE_BRACKETS.index(bracket):
                result.pop()
            else:
                return False
    return len(result) == 0


if __name__ == '__main__':
    examples = [
        '[{}({})]', # True
        '{]', # False
        '{', # False
        '{[(]}', # False
        '[]][', # False
        '', # True
        ')()' # False
    ]

    for example in examples:
        print(check_brackets_closed(example))
else:
    check_brackets_closed(input('Введите последовательность скобок'))