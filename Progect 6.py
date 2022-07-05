from random import randint
numbers = {'a' : [], 'b' : [], 'c' : [], 'd' : []}

for i in list(numbers.keys()):
    numbers[i] = [randint(-100, 100) for x in range(3)]
sum_values = {k:[sum(numbers[k])] for k in numbers.keys()}
max_value = [max(numbers, key=numbers.get), max(sum_values.values())]
print(numbers)
print(sum_values)
print("Max Key: " + str(max_value[0]) + " Max Value: " + str(max_value[1]))
    
