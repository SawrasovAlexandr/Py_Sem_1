# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

volume = int(input('Введите общее количество журавликов, сделанных детьми: '))
piece = volume // 6
print(f'Из них сделано Сережей: {piece}; Катей: {4 * piece}; Петей: {piece}')
if (lastpiece := volume % 6) != 0:
    print(f'А еще {lastpiece} сделала тетя Оля пока объясняла детям, как делать журавликов :)')
