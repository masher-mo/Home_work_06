# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# n = int (input("Введите число: "))
# def Sumnumber(num):
    # tot=0
    # while(num>0):
        # dig = num % 10
        # tot = tot + dig
        # num = num // 10
    # return tot
# print (Sumnumber(n))

n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)