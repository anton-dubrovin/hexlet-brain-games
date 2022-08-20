import random
import prompt
from brain_games.game import start_game


def main():
    start_game(brain_calc)


def brain_calc(start=0):
    if start:
        print('What is the result of the expression?')
    calc_num1 = random.randint(0, 99)
    calc_num2 = random.randint(0, 99)
    calc_operation = ['+', '-', '*'][random.randint(0, 2)]

    print(f'Question: {calc_num1} {calc_operation} {calc_num2}')
    answer = prompt.string('Your answer? ')

    if calc_operation == '+':
        correct_answer = str(calc_num1 + calc_num2)
    elif calc_operation == '-':
        correct_answer = str(calc_num1 - calc_num2)
    elif calc_operation == '*':
        correct_answer = str(calc_num1 * calc_num2)
    else:
        correct_answer = ''

    return answer, correct_answer


if __name__ == '__main__':
    main()
