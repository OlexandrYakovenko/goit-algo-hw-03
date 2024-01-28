from datetime import datetime as dtdt

formatted_date = dtdt(2023, 5, 17,0,0,0).strftime("%Y-%m-%d") # форматуємо дату'РРРР-ММ-ДД' (наприклад, '2024-05-17').

# Функція приймає один параметр: date_str — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
def get_days_from_today(date_str: str) -> int :
    days=0 # ініціалізуємо змінну, що міститиме кількість днів між датами, яку поверне функція
    try:
        input_date = dtdt.strptime(date_str, "%Y-%m-%d") #перетворюємо str на date у форматі 'РРРР-ММ-ДД' ("%Y-%m-%d")
        today=dtdt.today() # отримуємо сьогоднішню дату
        today_days = today.toordinal() #отримуємо сьогодні днів з початку ери
        input_date_days = input_date.toordinal() #отримуємо днів з початку ери для введеної дати 
        days = today_days - input_date_days #отримаэмо різницю в днях між днями з початку ери для сьогодні і для введеної дати
    except Exception as e:
        print(f"Error: {e}") # виводимо системну помилку
        print("the procedure accepts a date in the format ""YYYY-MM-DD"" ") # виводимо повідомлення користувачу, у якому вигляді ми бажаємо отримати дату
    return days

days = get_days_from_today(formatted_date)
print(days)