import pandas as pd


df = pd.read_csv('f.csv', sep='|')
df = df.apply(lambda x: x.str.strip() if x.dtype == 'object' else x)

unique_df = df.drop_duplicates()
duplicate_df = df.groupby('id').filter(lambda x: len(x) > 1)

print('Уникальные записи:\n', unique_df, '\n' + '-' * 10)
print('Дубликаты по id:\n', duplicate_df)
