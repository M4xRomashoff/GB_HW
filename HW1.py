# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 2.23.2022
# version = 1
# ---------------------------------------------------------------------
name = ''
age = 0
birthday = ''

print('Задание 1 \n')
print('-'*100)
print(f'имя: {name}, возраст: {age}, дата рождения:{birthday} ')
print('-'*100)

name1 = input('Введите ваше имя олностью ')
age1 = int(input('Введите ваш возраст '))
birthday1 = input('Введите дату вашего рождения')
print(f'Введенные данные \n имя: {name1} \n возраст: {age1}  \n дата рожденияЖ {birthday1} ')

print('Задание 2 \n')
print('-'*100)

time_sec = int(input( 'Введите время в секундах:' ))
time_hr = time_sec // 3600  # находим часы
time_min = (time_sec - (time_hr * 3600)) // 60  # находим минуты в том, что осталось
time_sec_left = time_sec - ((time_hr * 3600) + (time_min * 60))
print(f'{time_hr}:{time_min}:{time_sec_left}')

print('Задание 3 \n')
print('-'*100)
number = int(input('Введите число:'))
num2 = int(str(number)+str(number))
num3 = int(str(number)+str(number)+str(number))
new_number = number + num2+num3
print('Ответ:', new_number)

print('Задание 4 \n')
print('-'*100)

number_str = input('Введите целое положительное число:')

digit = 0
i = 0

while i != len(str(number_str)):
      if int(number_str[i]) > digit:
         digit = int(number_str[i])
         print('цифра',digit)
      i +=1
print('Самае большая цифра:',digit)

print( 'Задание 5 \n' )
print( '-' * 100 )

income = int( input( 'Введите сумму прихода:' ) )
spandings = int( input( 'Введите расходы:' ) )

if income > spandings:
    print( 'Ваше предприятие получило прибыль !' )
    print( 'Рентабельность вашей выручики: %.2f' %(income / spandings ))
    employees = int( input( 'Введите колчество сотрудников:' ) )
    print( 'Прибыль редприятия на одного сотрудника:', (income - spandings) / employees )
else:
    print( 'Ваше предприятие убыточно !' )

print( 'Задание 6 \n' )
print( '-' * 100 )

km1 = int(input('Введите сколько километов спортсмен пробежал в первый день :'))
km_fin = int(input('Введите сколько километров спортсмен должен пробежать за день( требуемый результат) :'))

km_day = km1
day = 0

while km_fin > km_day:
    day +=1

    km_day = km_day+(km_day*0.1)
    print(f'{day}-й день : {km_day:.2f}')
print(f'Ответ: требуемый результат спортсмен достигнет на {day} -й день')