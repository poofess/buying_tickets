num_tickets = int(input("Сколько билетов вам нужно? "))

total_cost = 0

for ticket in range(1, num_tickets + 1):
    age = int(input(f"Сколько лет посетителю №{ticket}? "))

    # Вычисление стоимости в зависимости от возраста
    if age < 18:
        cost = 0
    elif 18 <= age < 25:
        cost = 990
    else:
        cost = 1390

    # Добавление стоимости билета к общей стоимости
    total_cost += cost

# Применение скидки при покупке более трех билетов
if num_tickets > 3:
    total_cost *= 0.9  # Скидка 10%

# Вывод общей суммы к оплате
print(f"К оплате: {total_cost} руб.")
