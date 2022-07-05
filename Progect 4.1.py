import random
numbers = []
for number in range(10):
    numbers.append(random.randint(-100, 100))
print(numbers)

summ_positive = 0
summ_negative = 0
for number in numbers:
    if number > 0:
     summ_positive = summ_positive + number
    else:
     summ_negative = summ_negative + number
print('Сумма додатніх чисел - ', summ_positive)
print('Сумма від*ємних чисел - ', summ_negative)

import math

if math.fabs(summ_positive) > math.fabs(summ_negative):
    print('Модуль суми додатніх чисел більший за модуль від*ємних')
elif math.fabs(summ_positive) < math.fabs(summ_negative):
    print('Модуль суми додатніх чисел менший за модуль від*ємних')
else:
    print ('Модулі сумм однакові')



