import random

def mahrajon():
    print("Давай угадай немощный от 1 до 100, не сможешь значит ты лох!")

    secret_number = random.randint(1,100)
    print(secret_number)
    attempts = 0
    low = 1
    high = 100

    while True:
        guess = int(input(f"Вводи че думаешь (от {low} до {high}): "))
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
