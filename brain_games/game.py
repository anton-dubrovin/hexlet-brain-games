import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    correct_answers = 0
    while correct_answers < 3:
        first_game = 1 if correct_answers else 0
        answer, correct_answer = game(first_game)

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
            continue
        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\nLet's try again, {name}! ")
            return

    print(f'Congratulations, {name}!')
