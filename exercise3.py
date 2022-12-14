roman_digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def to_roman(number):
    result = ''
    while number > 0:
        for digit, roman in roman_digits:
            while number >= digit:
                result += roman
                number -= digit
    return result

if __name__ == '__main__':
    number_examples = [1945, 2022, 1249, 4949]

    for number in number_examples:
        print(to_roman(number))
else:
    to_roman(input('Введите слово или фразу для проверки, является ли она палиндромом.').lower())