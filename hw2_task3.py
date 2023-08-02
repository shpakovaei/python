# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
import fractions

f1 = fractions.Fraction(5, 7)
f2 = fractions.Fraction(2, 3)

print(f"{f1} + {f2} = {f1 + f2}")
print(f"{f1} * {f2} = {f1 * f2}")

fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

numerator1, denominator1 = map(int, fraction1.split("/"))
numerator2, denominator2 = map(int, fraction2.split("/"))

sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2

product_numerator = numerator1 * numerator2
product_denominator = denominator1 * denominator2

print("Сумма дробей:", sum_numerator, "/", sum_denominator)
print("Произведение дробей:", product_numerator, "/", product_denominator)
