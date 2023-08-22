# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Чтобы записать байты можно использовать список с числами и функцию bytes


import os
import random
import string


def generate_random_filename(length_min=6, length_max=30):
    length = random.randint(length_min, length_max)
    letters = string.ascii_letters + string.digits
    filename = ''.join(random.choice(letters) for _ in range(length))
    return filename


def generate_random_bytes(min_bytes=256, max_bytes=4096):
    num_bytes = random.randint(min_bytes, max_bytes)
    byte_list = [random.randint(0, 255) for _ in range(num_bytes)]
    return bytes(byte_list)


def create_files_with_extension(extension, num_files=42, **kwargs):
    for _ in range(num_files):
        filename = generate_random_filename(length_min=kwargs.get('length_min', 6),
                                            length_max=kwargs.get('length_max', 30)) + f".{extension}"
        file_size = random.randint(kwargs.get('min_bytes', 256), kwargs.get('max_bytes', 4096))
        file_content = generate_random_bytes(min_bytes=kwargs.get('min_bytes', 256),
                                             max_bytes=kwargs.get('max_bytes', 4096))

        with open(filename, 'wb') as file:
            file.write(file_content)


create_files_with_extension(
    extension='txt',
    length_min=6,
    length_max=30,
    min_bytes=256,
    max_bytes=4096,
    num_files=42
)