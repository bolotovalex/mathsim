from random import randint

def get_digit_dictionary(difficult, action: int):
    dict_answer = {}
    if difficult == 0:
        if action == '+':
            dict_answer['first_digit'] = randint(2, 10)
            dict_answer['sec_digit'] = randint(2, 10)
            dict_answer['right_answer'] = dict_answer['first_digit'] + dict_answer['sec_digit']

        elif action == '-':
            dict_answer['first_digit'] = randint(3, 20)
            while True:
                if dict_answer['first_digit'] == 3:
                    dict_answer['sec_digit'] = randint(1, dict_answer['first_digit'])
                else:
                    dict_answer['sec_digit'] = randint(2, dict_answer['first_digit'])
                if dict_answer['sec_digit'] >= dict_answer['first_digit'] - 1:
                    continue
                else:
                    break
            dict_answer['right_answer'] = dict_answer['first_digit'] - dict_answer['sec_digit']

        elif action == '*':
            dict_answer['first_digit'] = randint(2, 10)
            dict_answer['sec_digit'] = randint(2, 10)
            dict_answer['right_answer'] = dict_answer['first_digit'] * dict_answer['sec_digit']

        elif action == '/':
            dict_answer['sec_digit'] = randint(2, 10)
            dict_answer['first_digit'] = randint(2, 10) * dict_answer['sec_digit']
            dict_answer['right_answer'] = int(dict_answer['first_digit'] / dict_answer['sec_digit'])


    elif difficult == 1:
        if action == '+':
            dict_answer['first_digit'] = randint(11, 25)
            dict_answer['sec_digit'] = randint(6, 25)
            dict_answer['right_answer'] = dict_answer['first_digit'] + dict_answer['sec_digit']

        elif action == '-':
            dict_answer['first_digit'] = randint(21, 50)
            while True:
                dict_answer['sec_digit'] = randint(4, dict_answer['first_digit'])
                if dict_answer['sec_digit'] >= dict_answer['first_digit'] - 4:
                    continue
                else:
                    break
            dict_answer['right_answer'] = dict_answer['first_digit'] - dict_answer['sec_digit']

        elif action == '*':
            dict_answer['first_digit'] = randint(6, 15)
            dict_answer['sec_digit'] = randint(2, 10)
            dict_answer['right_answer'] = dict_answer['first_digit'] * dict_answer['sec_digit']

        elif action == '/':
            dict_answer['sec_digit'] = randint(2, 9)
            dict_answer['first_digit'] = randint(5, 12) * dict_answer['sec_digit']
            dict_answer['right_answer'] = int(dict_answer['first_digit'] / dict_answer['sec_digit'])

    elif difficult == 2:
        if action == '+':
            dict_answer['first_digit'] = randint(20, 50)
            dict_answer['sec_digit'] = randint(20, 50)
            dict_answer['right_answer'] = dict_answer['first_digit'] + dict_answer['sec_digit']

        elif action == '-':
            dict_answer['first_digit'] = randint(51, 99)
            while True:
                dict_answer['sec_digit'] = randint(6, dict_answer['first_digit'])
                if dict_answer['sec_digit'] >= dict_answer['first_digit'] - 6:
                    continue
                else:
                    break
            dict_answer['right_answer'] = dict_answer['first_digit'] - dict_answer['sec_digit']

        elif action == '*':
            dict_answer['first_digit'] = randint(11, 30)
            dict_answer['sec_digit'] = randint(3, 9)
            dict_answer['right_answer'] = dict_answer['first_digit'] * dict_answer['sec_digit']

        elif action == '/':
            dict_answer['sec_digit'] = randint(2, 9)
            dict_answer['first_digit'] = randint(11, 17) * dict_answer['sec_digit']
            dict_answer['right_answer'] = int(dict_answer['first_digit'] / dict_answer['sec_digit'])
    return dict_answer

if __name__ == '__main__':
    print('Easy difficult:')
    print(get_digit_dictionary(0, '+'))
    print(get_digit_dictionary(0, '-'))
    print(get_digit_dictionary(0, '*'))
    print(get_digit_dictionary(0, '/'))
    print()
    print('Normal difficult:')
    print(get_digit_dictionary(1, '+'))
    print(get_digit_dictionary(1, '-'))
    print(get_digit_dictionary(1, '*'))
    print(get_digit_dictionary(1, '/'))
    print()
    print('Hard difficult:')
    print(get_digit_dictionary(2, '+'))
    print(get_digit_dictionary(2, '-'))
    print(get_digit_dictionary(2, '*'))
    print(get_digit_dictionary(2, '/'))

