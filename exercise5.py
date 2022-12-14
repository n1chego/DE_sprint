def binary_multiplier(number1, number2):
    multiple = int(number1, 2) * int(number2, 2)
    return bin(multiple)[2:]


if __name__ == '__main__':
    examples = [
        ('111', '101'), # 100011
        ('1111', '1'), # 1
        ('100', '100'), # 10000
        ('11111', '0'), # 0
    ]

    for number1, number2 in examples:
        print(binary_multiplier(number1, number2))
else:
    print(binary_multiplier(
        number1=str(input('Введите бинарное число')),
        number2=str(input('и еще одно'))
    ))