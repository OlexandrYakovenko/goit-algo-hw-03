import re
# приклад1 даних із задачі
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

# приклад2 даних із задачі
dirty_phones=["    +38(050)123-32-34",
"     503451+234",
"     0503451+235",
"(050)8889++900",
"38050-111-22-22",
"38050 111 22 11   "]

# функція для нормалізації номерів телефонів, отримує str, повертає нормалізований телефон str 
def normalize_phone(phone_number):
    p1=r"\+{0,1}[\d]+"   # шукаємо + і цифри
    phone_number=''.join(re.findall(p1,phone_number))
    phone_number=phone_number.replace('+','') # заміняємо всі + на пусте значення (для виключення ситуації + всередині телефону)
    if len(phone_number)==10:
        phone_number='+38'+phone_number # доповнюємо номер '+38' на початку
    elif len(phone_number)==9:
        phone_number='+380'+phone_number # доповнюємо номер '+380' на початку
    elif len(phone_number)==12:
        phone_number='+'+phone_number # доповлююємо номер + на початку
    return phone_number

sanitized_numbers1 = [ normalize_phone(num) for num in dirty_phones]
print("Нормалізовані номери телефонів для SMS-розсилки (sanitized_numbers1):", sanitized_numbers1)
    
sanitized_numbers2 = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки (sanitized_numbers2):", sanitized_numbers2)    