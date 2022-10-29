per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите сумму депозита: '))
values = list(per_cent.values())
deposit = (values[0]*money/100), (values[1]*money/100), (values[2]*money/100), (values[3]*money/100)
deposit = list(map(round, deposit))
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit))