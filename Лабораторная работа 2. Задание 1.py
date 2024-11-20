money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0 # Счетчик месяцев без долгов
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

#print("Количество месяцев, которое можно протянуть без долгов:", ...)
while money_capital > 0 or money_capital == 0:
    money_capital = money_capital + salary  # Все деньги которые есть
    money_capital = money_capital - spend   # Оставшиеся деньги за месяц
    spend = spend * (1+increase)  # Новые расходы
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month-1)
