import os
import datetime


folder = 'folder'

# Задаем количество дней, после которых файлы нужно удалить
N_days = 10

today = datetime.date.today()

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)

    mtime = os.path.getmtime(filepath)
    mdate = datetime.date.fromtimestamp(mtime)
    delta = today - mdate
    # print(delta.days, today, mdate, filename)

    if delta.days >= N_days:
        os.remove(filepath)
