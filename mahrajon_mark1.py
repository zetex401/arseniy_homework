import random

def get_valid_number(min_val, max_val):
    while True:
        try:
            num = int(input(f"Введи число от {min_val} до {max_val}: "))
            if min_val <= num <= max_val:
                return num
            print(f"Эй, границы {min_val}..{max_val}, не придумывай!")
        except ValueError:
            print("Это не число. Давай нормально 🙄")

def mahrajon():
    print("Игра: угадай число от 1 до 100. Если не угадаешь — сам знаешь кто 😏")

    secret_number = random.randint(1, 100)
    attempts = 0
    low = 1
    high = 100

    while True:
        guess = get_valid_number(low, high)
        attempts += 1

        if guess == secret_number:
            print(f"Уважуха. Ты угадал {secret_number} за {attempts} попыток.")
            break
        elif guess < secret_number:
            print("Маловато, надо больше ↑")
            low = guess + 1
        else:
            print("Перебор, попробуй меньше ↓")
            high = guess - 1

if __name__ == "__main__":
    mahrajon()
