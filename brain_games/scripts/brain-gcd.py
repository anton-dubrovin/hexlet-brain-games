import random
import prompt
import math
from brain_games.game import start_game


def main():
    start_game(brain_gcd)


def brain_gcd(start=0):
    if start:
        print('Find the greatest common divisor of given numbers.')
    game_num1 = random.randint(0, 99)
    game_num2 = random.randint(0, 99)

    print(f'Question: {game_num1} {game_num2}')
    answer = prompt.string('Your answer? ')

    correct_answer = str(math.gcd(game_num1, game_num2))

    return answer, correct_answer


if __name__ == '__main__':
    main()
