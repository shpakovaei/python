# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

list = [1, 2, 3, 1, 2, 4, 5]
new_list = []

for num in list:
    if list.count(num) > 1 and num not in new_list:
        new_list.append(num)

print(new_list)