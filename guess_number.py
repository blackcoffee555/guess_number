from random import randint

number = randint (1, 100)
print('Угадайте число от 1 до 100')


while True:
    inp_num = int(input('Введите число: '))
    if (inp_num > 100) or (inp_num < 0):
        print ('Число не входит в угадываемый диапазон! Попробуйте снова: ')
        continue
    else:
        if (inp_num > number):
            print ('Ваше число больше того, что загадано')
            continue
        elif (inp_num < number):
            print ('Ваше число меньше того, что загадано')
            continue
        else:
            print ('Отличная интуиция! Вы угадали число :)')
            break
