from datetime import datetime
def get_days_from_today(date):
    try:
        #преобразуем строку в дату
        input_date = datetime.strptime(date,"%Y-%m-%d").date()
        #текущая дата 
        today = datetime.today().date()
        delta = today - input_date
        return delta.days
    except ValueError:
        print ("Неверный формат")
        return None
    
print (get_days_from_today("2021-05-05"))
