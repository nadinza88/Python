# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

num_N = int(input('Введите число'))

for i in range(-num_N, num_N+1):
    print(i, end=' ')
