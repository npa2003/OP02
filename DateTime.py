import datetime

# Получаем текущее время
current_time = datetime.datetime.now()

# Форматируем и выводим дату и время
print(current_time)
print("Текущая дата и время:", current_time.strftime("%Y-%m-%d %H:%M:%S"))