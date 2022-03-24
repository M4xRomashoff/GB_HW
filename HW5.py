# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 23.03.2022
# version = 1
# ---------------------------------------------------------------------------

# Задание 1




try:
    with open(r'data\text.txt', 'w', encoding='utf-8') as f:
        while True:
            text = input('Введите текст для записи в файл, для окончания введите пустую строку : \n')
            if text == '': break
            f.write(text)
            f.write('\n')

except IOError:
    print("Произошла ошибка ввода-вывода!")



# Задание 2

try:
    with open( r'data\text2.txt', 'r', encoding='utf-8' ) as f:
        line_counter = 0
        word_counter = 0
        dict1 = {}
        for line in f:
            line_counter += 1
            list = line.split()
            word_counter = len( list )
            dict1.update( {line_counter: word_counter} )
        print( 'Номер строки и количество слов в этой строке :' )
        total = 0
        for key, value in dict1.items():
            print( key, '  ', value )
            total += value
        print( 'Всего строк в документе : ', line_counter )
        print( 'Всего слов в документе :', total )


except IOError:
    print( "Произошла ошибка ввода-вывода!" )

# Задание 3


try:
    with open( r'data\text3.txt', 'r', encoding='utf-8' ) as f:
        dict2 = {}
        line_counter = 0
        sum = 0
        for line in f:
            pair = line.split()
            dict2.update( {pair[0]: float( pair[1] )} )
            line_counter += 1
            sum += float( pair[1] )
        print( 'Список сотрудников получающих менее 20 т.р.' )
        for key, value in dict2.items():
            if value < 20000: print( key, ' ', value )

        print( 'Всего сотрудников : ', line_counter )
        print( 'Средняя зарплата сотрудника : {:.2f}'.format( sum / line_counter ) )

except IOError:
    print( "Произошла ошибка ввода-вывода!" )

# Задание 4

dict5 = {'One':   'Один',
         'Two':   'Два',
         'Three': 'Три',
         'Four':  'Четыре',
         'Five':  'Пять',
         'Six':   'Шесть',
         'Seven': 'Семь',
         'Eight': 'Восемь',
         'Nine':  'Девять',
         'Ten':   'Десять',
         }

try:
    with open( r'data\text4.txt', 'r', encoding='utf-8' ) as f, open(r'data\text4W.txt', 'w', encoding='utf-8' ) as fw:

        for line in f:
            list = line.split()
            new_line = dict5.get(list[0])+' '+list[1]+' '+list[2]+'\n'
            fw.write(new_line)

except IOError:
    print( "Произошла ошибка ввода-вывода!" )

# Задание 5

from random import randint

try:  # создаем файл с числами
    with open( r'data\text5.txt', 'w', encoding='utf-8' ) as f:

       for i in  range(20):
           num = randint(0, 100)
           f.write(str(num))
           f.write(' ')

except IOError:
    print( "Произошла ошибка ввода-вывода!" )

try:  # читаем и считаем
    with open( r'data\text5.txt', 'r', encoding='utf-8' ) as f:
        st = (f.read()).split()
        print('Числа : ',st)
        sum = 0
        for i in st: sum += int(i)
        print('Сумма чисел : ', sum)

except IOError:
    print( "Произошла ошибка ввода-вывода!" )


# задание 6

def get_number(s: str):
    new_str = ''
    for item in s:
        if item.isnumeric():
            new_str = new_str + item
    if new_str.isnumeric():
        return int( new_str )
    else:
        return 0

def get_name(list1: list):
    new_str = list1[0]
    new_str = new_str[:-1]
    return new_str


def get_hrs(list1: list):
    sum = 0
    for item in range( 1, len( list1 ) ):
        sum += get_number( list1[item] )
    return sum


dict_hrs = {}
try:
    with open( r'data\text6.txt', 'r', encoding='utf-8' ) as f:

        for item in f:
            list1 = item.split()
            t = get_hrs( list1 )
            dict_hrs.update( {get_name( list1 ): get_hrs( list1 )} )

except IOError:
    print( "Произошла ошибка ввода-вывода!" )

for key, value in dict_hrs.items():
    print( key, ' ', value, ' часов' )

# Задание 7
import json

dict_profits = {}
dict_loss = {}
try:
    with open( r'data\text7.txt', 'r', encoding='utf-8' ) as f:

        for item in f:
            list1 = item.split()
            name = list1[0]
            income = int( list1[2] )
            expense = int( list1[3] )
            if (income - expense) > 0:
                dict_profits.update( {name: (income - expense)} )
            else:
                dict_loss.update( {name: (income - expense)} )

except IOError:
    print( "Произошла ошибка ввода-вывода!" )
except TypeError:
    print( "Произошла ошибка преобразования данных!" )

print( '' )
print( 'Словарь компаний с прибылью :' )
for key, value in dict_profits.items():
    print( key, '  ', value )

print( '' )
sum_profits = 0
for key, value in dict_profits.items():
    sum_profits += value

avg_profits = sum_profits / len( dict_profits )
print( 'Средняя прибыль : {:.2f}'.format( avg_profits ) )
dict_avg_profits = {'average_profits': avg_profits}

print( '' )
print( 'Словарь компаний с убытком :' )
for key, value in dict_loss.items():
    print( key, '  ', value )

list7 = [dict_profits, dict_loss, dict_avg_profits]
print( list7 )

try:
    with open( r'data\text7.json', 'w', encoding='utf-8' ) as f:

        json.dump( list7, f )

except IOError:
    print( "Произошла ошибка ввода-вывода!" )

# Проверяем правильно ли записали

print( '' )
try:
    with open( r'data\text7.json', 'r', encoding='utf-8' ) as f:

        data = json.load( f )
        print( type( data ) )
        for item in data:
            print( item )

except IOError:
    print( "Произошла ошибка ввода-вывода!" )
