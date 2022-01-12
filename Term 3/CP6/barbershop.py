import random
import os
import heapq # Реализация очереди с приоритетом как минимальной кучи

# Если клиент пришел до закрытия, то его обслужат
# Клиенты не уходят из очереди, сколько бы им не пришлось ждать.

# 4 работника
# 1 заказ = 25 минут
# 1 клиент прибывает каждые 15-25 минут в течении 480 минут.

os.system('cls')

# Работники будут хранится в очереди с приоритетом.
# Клиент идёт к работнику с макс временем безделия
# 1 индекс - 0 = занят. Другое число - время, когда стал занятым
# 2 индекс - время за работой
workers = [[0, 0], [0, 0], [0, 0], [0, 0]]

clientsToday = 0
workday = 480
timeForClient = 25

# Определение кол. клиентов, что придут в день
while workday >= 0:
    # workday -= random.randint(5, 7) # Жёсткий день
    workday -= random.randint(15, 25) # Жёсткий день
    clientsToday += 1

while clientsToday != 0: # Работаем до обслуживания последнего клиента
    workday -= 1 # Каждую итерацию проходит 1 минута

    # Очередь с приоритетом из работников. Вначале те, кто меньше всех работал и незанят
    heapq.heapify(workers)

    # Если парикмахер свободен и работал меньше всех
    if workers[0][0] == 0:
        workers[0][0] = workday # Время, когда стал занят
        workers[0][1] += timeForClient # Поработал

    # Есть ли освободившиеся работники
    for i in range(len(workers)):
        if workers[i][0] == (workday + 25): # Прошло ли 25 минут с момента, когда стал занят
            workers[i][0] = 0 # Освободился
            clientsToday -= 1 # Клиент ушел

print("Часы отработанные каждым работником: ")
print(workers)

print("Коэф. эффективности каждого работника: ")
for i in range(len(workers)):
    workers[i][1] = workers[i][1] / 480
print(workers)

# Условие освобождения работника
# Можно сохранять работнику время, когда он принялся за работу.
# Когда это время будет на 25 минут больше, чем текущее время он освободится