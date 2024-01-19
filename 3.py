a = [[1, 2, 3], [4, 5, 6]]

b = [dict(zip([f'k{j}' for j in range(1, len(x) + 1)], x)) for x in a]

print(b)
