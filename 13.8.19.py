sum = round(0, 2)
lot = int(input('Введите количество билетов:\t'))
age = [int(input(f'Введите возраст {i + 1}-го посетителя:\t')) for i in range(lot)]
for i in age:
    if 18 <= i < 25:
        sum = sum + 990
    elif i >= 25:
        sum = sum + 1390
if lot > 3:
    sum = round((sum - sum * 0.1), 2)
    print('Вы дополнительно получаете 10% скидку на полную стоимость заказа')
    print(f'Сумма к оплате: {sum} рублей')
else:
    print(f'Сумма к оплате: {sum} рублей')