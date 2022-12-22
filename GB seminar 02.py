# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
import random
print('Сколько монеток? ')
coin = int(input())
coins = []
for c in range(coin):
    coins.append(random.randint(0, 1))
coins_w = []
for i in coins:
    if i == 0:
        coins_w.append('Орёл.')
    elif i == 1:
        coins_w.append('Решка.')
print('Выпало: ', coins_w)
up = sum(coins)
down = coin - up
if up == down:
    print('Нужно перевернуть ', up, ' монеток') 
elif up == 0 or down == 0:
    print('Не нужно переворачивать!')
elif up < down:
    print('Нужно перевернуть', up, 'монеток')
elif down < up:
    print('Нужно перевернуть', down)
