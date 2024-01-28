import random

def get_numbers_ticket(min :int, max :int, quantity :int)-> []:
    gen_list = []
    if ((min < 1) \
        or (max > 1000) \
            or (quantity not in range(min,max)) \
    ): 
        # min - мінімальне можливе число у наборі (не менше 1).
        # max - максимальне можливе число у наборі (не більше 1000).
        # quantity - кількість чисел, які потрібно вибрати (значення між min і max).
        print("Дані введено некоректно")
        return []
    while (len(gen_list) < quantity): #список у циклі наповлюється випадковими унікальними числами
        a=random.randint(min,max)
        if a not in gen_list:
            gen_list.append(a)
    gen_list.sort() # сортуємо
    return gen_list

print("get_numbers_ticket(1,36,6):")
print(get_numbers_ticket(1,36,6))

print("get_numbers_ticket(-1,36,6):")
print(get_numbers_ticket(-1,36,6))

print("get_numbers_ticket(1,1000,6):")
print(get_numbers_ticket(1,1000,6))

print("get_numbers_ticket(1,36,-1):")
print(get_numbers_ticket(1,36,-1))