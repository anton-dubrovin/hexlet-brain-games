import random
import prompt
from brain_games.game import start_game


def main():
    start_game(brain_even)


def brain_even(start=0):
    if start == 0:
        print(f'Answer "yes" if the number is even, otherwise answer "no".')
    game_num = random.randint(0, 99)
    print(f'Question: {game_num}')
    answer = prompt.string('Your answer? ')
    correct_answer = 'yes' if game_num % 2 == 0 else 'no'
    return answer, correct_answer


if __name__ == '__main__':
    main()
