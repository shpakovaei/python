#2.

num = int(input("Введите число: "))
MAX_NUM = 100000
MIN_NUM = 0
k = 0

if num < MIN_NUM or num > MAX_NUM:
    print("Введено недопустимое число. Допустимы числа от 0 до 100000.")
elif num == 1 or num == 0:
    print("Число не является ни простым, ни составным.")
else:
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k+1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число составное")


# elif: for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Число составное.")
# else:
#     print("Число простое.")
