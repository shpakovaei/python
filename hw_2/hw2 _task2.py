# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.


def to_hex(num):
    hex_numbers = "0123456789abcdef"
    hex_str = ""
    while num > 0:
        hex_str = hex_numbers[num % 16] + hex_str
        num = num // 16
    return hex_str

num = int(input("Введите целое число: "))
print(f"Шестнадцатеричное представление числа {num} - {to_hex(num)}")


h = hex(num)
print(f"Шестнадцатеричное представление числа {num} - {h}")


