'''first_age = int(input('Enter your age: '))
second_age = int(input('Enter your age: '))
third_age = int(input('Enter your age: '))

ages = [first_age,second_age,third_age]

i = 0
while i < len(ages):
    if ages[i] >= 18:
        print(i, 'adult')
    else:
        print(i, 'child')

    i = i + 1
'''

age = int(input('Введіть скільки вам років: '))
if age >= 18:
    print('Повнолітній')
else:
    print('Неповнолітній')
