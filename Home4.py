import datetime as dt
from datetime import datetime as dtdt
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Іван Петров", "birthday": "2001.01.29"},
     {"name": "Сидор Голохвастов", "birthday": "2001.01.28"}
]
# функція отримує словник імен користувачів та їх дати народження, повертаэ словник майбутніх днів народження
def get_upcoming_birthdays(users=None):
    today_date=dtdt.today().date() # беремо сьогоднішню дату
    birthdays_list=[] # створюємо список для майбутніх днів народження
    for user in users: # перебираємо словник користувачів
        birthday_date=user["birthday"] # отримуємо дату народження зі списку у вигляді рядка
        birthday_date=str(today_date.year)+birthday_date[4:] # Замінюємо рік на поточний 
        birthday_date=dtdt.strptime(birthday_date, "%Y.%m.%d").date() # перетворюємо дату народження в об’єкт date з формату РРРР-ММ-ДД
        week_day=birthday_date.isoweekday() # Отримуємо день тижня (1-7)
        days_between=(birthday_date-today_date).days # рахуємо різницю між зараз і днем народження цьогоріч у днях
        if 0<=days_between<7: # якщо день народження протягом 7 днів від сьогодні включаючи поточний день
            if week_day<6: #  якщо пн-пт (1-5)
                birthdays_list.append({'name':user['name'], 'birthday':birthday_date.strftime("%Y.%m.%d")}) 
                # Додаємо запис у список.
            else:
                if (birthday_date+dt.timedelta(days=1)).weekday()==0:# якщо неділя (понеділок - 0-й день для weekday(), 1 день до понеділка - це неділя)
                    birthdays_list.append({'name':user['name'], 'birthday':(birthday_date+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
                elif (birthday_date+dt.timedelta(days=2)).weekday()==0: #якщо субота (понеділок - 0-й день для weekday(), 2 дня до понеділка - це субота)
                    birthdays_list.append({'name':user['name'], 'birthday':(birthday_date+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
                    #Переносимо на понеділок. Додаємо запис у список.
    return birthdays_list

print(get_upcoming_birthdays(users))