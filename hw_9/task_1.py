# Создать декоратор для использования кэша. Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами, которые уже
# записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию. Кэш лучше хранить в json.

import json
import functools


def cache_decorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_key = json.dumps(args) + json.dumps(kwargs)

        if arg_key in cache:
            return cache[arg_key]

        result = func(*args, **kwargs)
        cache[arg_key] = result

        with open('cache.json', 'w') as cache_file:
            json.dump(cache, cache_file, indent=4)

        return result

    return wrapper


@cache_decorator
def example_function(x, y):
    return x + y


print(example_function(2, 3))
print(example_function(2, 3))

print(example_function(4, 5))
print(example_function(2, 3))