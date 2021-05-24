from datetime import datetime

def curr_time():
    date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return date
