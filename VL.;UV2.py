import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуйте угадать!")

    while True:
        try:
            guess = int(input("Введите ваше предположение: "))
            attempts += 1

            if guess < number_to_guess:
                print("Слишком мало, попробуйте еще раз.")
            elif guess > number_to_guess:
                print("Слишком много, попробуйте еще раз.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

guess_number()
