import random
import prompt
from brain_games.game import start_game


def main():
    start_game(brain_prime)


def brain_prime(start=0):
    if start:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                     47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    game_num = random.randint(0, 99)

    print(f"Question: {game_num}")
    answer = prompt.string('Your answer? ')
    correct_answer = 'yes' if game_num in prime_numbers else 'no'
    return answer, correct_answer


if __name__ == '__main__':
    main()
