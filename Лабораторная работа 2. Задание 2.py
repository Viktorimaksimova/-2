salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Счетчик подушки
for i in range(months):
    ost = salary - spend  # Долг за месяц
    spend = spend * (1 + increase)  # Новые расходы
    money_capital = money_capital + ost
money_capital = 0 - money_capital # Избавление от отрицательности
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
