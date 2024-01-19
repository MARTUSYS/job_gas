m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

total_count = sum(len(x) for x in m)

total_sum = sum(sum(x) for x in m)

mean = total_sum / total_count

t = tuple(m)

print('Общее количество чисел:', total_count)
print('Общая сумма чисел:', total_sum)
print('Среднее значение:', mean)
print('Кортеж из множеств:', t)
