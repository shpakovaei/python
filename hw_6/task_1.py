# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает истину, если дата может существовать
# или ложь, если такая дата невозможна. Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует григорианский
# календарь. Проверку года на високосность вынести в отдельную защищённую функцию.

class DateValidator:
    @staticmethod
    def is_leap_year(year):
        """
        Проверяет, является ли год високосным.
        """
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def is_valid_date(date_str):
        """
        Проверяет, является ли дата корректной.
        """
        try:
            day, month, year = map(int, date_str.split('.'))
            if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
                days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                if DateValidator.is_leap_year(year):
                    days_in_month[2] = 29

                return day <= days_in_month[month]
            return False
        except ValueError:
            return False


date_str = "29.02.2028"
if DateValidator.is_valid_date(date_str):
    print(f"{date_str} - корректная дата")
else:
    print(f"{date_str} - некорректная дата")