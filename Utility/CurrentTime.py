from datetime import datetime


# Функция выводит текущую дату и время
def curr_time():
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date
