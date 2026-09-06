import random

num1 = random.randint(1, 10)
num2 = random.randint(5, 15)

number = input('Weet jij wat ' + str(num1) + '+' + str(num2) + ' is? ')

try:
    number = int(number)

    if number == num1 + num2:
        print('Dat is juist')
    else:
        print('Nee dat klopt niet')
except ValueError:
    print('Dat is geen nummer!')
