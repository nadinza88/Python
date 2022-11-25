# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

chetvert = int(input('Введите номер четверти'))
if chetvert == 1:
     print('x>0 и y>0')
else:
    if chetvert == 2:
        print('x<0 и y>0')
    else:
        if chetvert == 3:
            print('x<0 и y<0')
        else:
            print('x>0 и y<0') 





   
    



