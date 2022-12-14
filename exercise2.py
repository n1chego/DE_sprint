def is_palindrom(text):
    text_without_spaces = text.replace(' ', '')
    reversed_text = "".join(reversed(text_without_spaces))
    if text_without_spaces == reversed_text:
        print('Ого, да это палиндром!')
        return True
    else:
        print('Не палиндром, попробуйте другую фразу.')
        return False


if __name__ == '__main__':
    text_examples = ['taco cat', 'Rotator', 'black cat', 'удавы рвали лавры в аду']

    for example in text_examples:
        is_palindrom(example)
else:
    is_palindrom(input('Введите слово или фразу для проверки, является ли она палиндромом.').lower())