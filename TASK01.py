# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
i=random.randint(1,2)
print(i)
candle=2021

if i==1:
    print('Ходит первый игрок')
else:
    print('Ходит второй игрок')
cand1=0
cand2=0
while candle>0:
    if i==1:
        cand=int(input(f'Осталось {candle} конфет. Сколько конфет берет первый игрок(не более 28)? '))
        i=2
        if cand>28: 
            print("Ай-ай! Вы хотите забрать слишком много конфет!")
            cand=0
            i=1
        candle-=cand
        cand1+=cand
    else:
        cand=int(input(f'Осталось {candle} конфет. Сколько конфет берет второй игрок(не более 28)? '))
        i=1
        if cand>28: 
            print("Ай-ай! Вы хотите забрать слишком много конфет!")
            cand=0
            i=2
        candle-=cand
        cand2+=cand
if i==1:
    print(f'Поздравляем! Выиграл второй игрок.Ему достается {cand1} конфет первого игрока!')
else:
    print(f'Поздравляем! Выиграл первый игрок.Ему достается {cand2} конфет второго игрока!')
