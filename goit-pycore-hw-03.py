import datetime
def get_days_from_today(date):
    try:
        #преобразуем строку в обьект даты
        d = datetime.strptime(date, "%Y-%m-%d").date()

        #вычисляем разницу между сегодняшним днем и заданной датой
        return (datetime.today().date()- d).days
    except:
        return None
        
    