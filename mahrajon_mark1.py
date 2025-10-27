import random

def get_valid_number(min_val, max_val):
    while True:
        try:
            num = int(input(f"Вводи че думаешь (от {min_val} до {max_val}): "))
            if min_val <= num <= max_val:
                return num
            print(f"Дурак считать не умеешь чтоли {min_val} до {max_val}!")
        except ValueError:
            print("Писло чеши вводи не перди!")

def mahrajon():
    print("Давай угадай немощный от 1 до 100, не сможешь значит ты лох!")

    secret_number = random.randint(1,100)
    print(secret_number)
    attempts = 0
    low = 1
    high = 100

    while True:
        guess = get_valid_number(low, high)

        attempts += 1

        if guess == secret_number:
            print(f"Капец ты умный угадал {secret_number} за {attempts} попыток!")
            break
        elif guess < secret_number:
            print("Меньше же епта загаданного. Гоу еще.")
            low = guess + 1
        else:
            print("Больше загаданного. Гоу еще раз.")
            high = guess - 1

mahrajon()
