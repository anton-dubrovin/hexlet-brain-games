import random
import prompt
from brain_games.game import start_game


def main():
    start_game(brain_progression)


def brain_progression(start=0):
    if start:
        print('What number is missing in the progression?')
    progression_len = random.randint(10, 15)
    progression_step = random.randint(1, 10)
    progression_start = random.randint(0, 99)

    progression = []
    for i in range(progression_len):
        progression.append(progression_start + progression_step * i)

    hidden_index = random.randint(0, progression_len - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'

    print(f"Question: {' '.join(map(str, progression))}")
    answer = prompt.string('Your answer? ')

    return answer, correct_answer


if __name__ == '__main__':
    main()
