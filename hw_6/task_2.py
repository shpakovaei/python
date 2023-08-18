# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

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

def main():
    date_str = input("Введите дату в формате DD.MM.YYYY: ")
    if DateValidator.is_valid_date(date_str):
        print(f"{date_str} - корректная дата")
    else:
        print(f"{date_str} - некорректная дата")

if __name__ == "__main__":
    main()