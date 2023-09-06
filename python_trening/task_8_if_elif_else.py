num_float = 3.4
if num_float > 0:
    print('Число положительное')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

#if - or and

num = 7
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')
#-----
x = int(input())

if x >=1 and x <= 4:
    print('Бакалавр')
elif 5 < x < 6:
#range(5, 7)
#elif x in (5, 6):
    print('Магистр')
else  x in (8, 9):
    print('Аспирант')
# -----
x = int(input())
if x > 100  or x < -100:
    print('-')
elif:
    print('+')