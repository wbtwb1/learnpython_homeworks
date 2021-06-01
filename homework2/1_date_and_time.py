from datetime import datetime, date , time, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    # dt_now = datetime.now ()
    # delta1=timedelta (days=1)
    # dt_yesterday = dt_now - delta1
    # delta2 = timedelta (days=30)
    # dt_30days_ago = dt_now - delta2
    # print (dt_yesterday,'\n',dt_now,'\n',dt_30days_ago)





def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = '01/01/20 12:10:03.234567'
    date_obj = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print (date_obj.strftime("%d/%m/%y %H:%M:%S.%f"))


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
