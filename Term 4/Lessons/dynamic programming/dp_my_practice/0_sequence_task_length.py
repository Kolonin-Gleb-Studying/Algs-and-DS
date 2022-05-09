# https://youtu.be/GOF4VUi4nGU - видео разбор задачи
# 10:20 - восстановление ответа

# Найти длину наибольшей общей последовательности

def show_step(step, dp):
    print("Шаг = " + str(step))
    print()
    # Красивый вывод матрицы для анализа ответа
    for row in dp:
        print(row)
    print()

# lcs - length common sequence
def lcs(s1, s2):
    n = len(s1) # длина 1 последовательности (= Кол. столбцов - 1)
    print("Длина 1 последовательности = n = " + str(n))
    m = len(s2) # длина 2 последовательности (= Кол. строк - 1)
    print("Длина 2 последовательности = m = " + str(m))
    
    # Инициализация массива размера (n + 1) * (m + 1)
    # Размеры увеличины на 1, чтобы алгоритм работал, т.к. там есть действия типа (i - 1) и (j - 1)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # dp[0][0] = 0 - База и так будет удавлетворяться

    step = 0

    # Перебор элементов последовательностей
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Для просмотра хода расчётов
            # step += 1
            # show_step(step, dp)

            if s1[i - 1] == s2[j - 1]: # Каждый эл. посл. s1 будет сравниваться с всеми эл. посл. s2
                # Регистрируем нахождение ещё 1 общего эл. последовательностей.
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Оставляем максимальную длину уже найденного ранее НОП.
                # Для этого берём либо значение строкой выше либо предыдущее значение в этой строке. Подробнее см. комментарий 1
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Красивый вывод матрицы для анализа ответа
    for row in dp:
        print(row)

    # Возращаем длину НОП
    return dp[n][m]


s1 = "abacaba"
s2 = "abcabc"
print(lcs(s1, s2))


# комментарий 1
'''
В строке матрицы dp появляются значения в соответствии с тем,
сколько ОП (общих последовательностей) обнаружено на этой проверке (сравнение i-ого эл. s1 cо всеми эл. s2).

В каждой следующей строке если совпадения эл. нет, то число всё равно может вырасти на 1, т.к. раньше (выше в этом же столбце)
уже было обнаружено совпадение эл.
'''
