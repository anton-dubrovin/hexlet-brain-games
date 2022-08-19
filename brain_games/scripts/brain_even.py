import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        game_num = random.randint(0, 99)
        print(f'Question: {game_num}')
        answer = prompt.string('Your answer? ')

        correct_answer = 'yes' if game_num % 2 == 0 else 'no'
        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
            continue
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}! ")
            return

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
