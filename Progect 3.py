first_number = int(input('Enter the length of the side of the first triangle:'))
second_number = int(input('Enter the length of the side of the second triangle:'))
third_number = int(input('Enter the length of the side of the third triangle:'))
fourth_number = int(input('Enter the length of the side of the fourth triangle:'))
fifth_number = int(input('Enter the length of the side of the fifth triangle:'))

sides = [first_number, second_number, third_number, fourth_number, fifth_number]
squares = [s, s1, s2, s3, s4]
names = ['First square', 'Second square', 'Third square', 'Fourth square','Fifth square']
i = 0
while i < len(sides):
    p = (3*sides[i])/2
    squares[i] = (p * 3 *(p - sides[i]))**(1/2)
    print (names[i], s)
    i = i + 1
print ('Sum',s+s1+s2+s3+s4)
