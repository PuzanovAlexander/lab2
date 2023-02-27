#Угадайка
import random 
#Обозначение обласли чисел
random_number = random.randint(1, 5)
user_number = input('Угадай число (от 1 до 5):')
#Условия проверки, вывод результата
if user_number == random_number:
    print ('Вы угадали число!')
    print (f'Число было {random_number}')
else:
    print ('Вы НЕ угадали :(')
    print (f'Было число {random_number}')