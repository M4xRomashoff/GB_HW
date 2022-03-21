# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 03.21.2022
# version = 1
# ---------------------------------------------------------------------------


# Задание 1

from sys import argv

try:
    rate = float( argv[1] )
    hrs = float( argv[2] )
    bonus = float( argv[3] )
    print( 'Ставка : ', rate )
    print( 'Количество часов', hrs )
    print( 'Премия', bonus )

    print( 'Сумма у выдаче : ', rate * hrs + bonus )

except ValueError:
    print( 'Не верно введены параметры' )


# Задание 2

list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list[item] for item in range( 1, len( list ) ) if list[item] > list[item - 1]]
print( new_list )

# Задание 3

list1 = [item for item in range( 20, 241) if item % 20 == 0]
print('числа кратные 20 : ', list1 )

list2 = [item for item in range( 20, 241) if item % 21 == 0]
print('числа кратные 21 : ', list2 )


# Задание 4

list3 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list3 = [item for item in list3 if list3.count(item) < 2]
print(new_list3)

# Задание 5

from decimal import Decimal  # для работы с большим числом

list4 = [item for item in range(100, 1001) if item%2 == 0]

print(list4[0]) # первый элемент
print(list4[-1]) # последний элемент
print(len(list4)) # всего элементов

test_list = [2,3,4]

from functools import reduce

def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev * el

result = reduce(reducer_func, test_list)
print('тестируем с простым списком : ', result)


result = reduce(reducer_func, list4)
print(f'результат приведен к научному формату {Decimal(result):.2E}')


# Задание 6

from itertools import count, cycle

start = int( input( 'Введите целое число меньше 25 : ' ) )
number = count( start, 1 )
while True:
    res = next( number )
    if res > 25:
        break
    else:
        print( res )

list6 = [1, 2, 3, 4, 5]

cycler = cycle( list6 )
sum = 0

while True:
    number = next( cycler )
    sum += number
    print( 'значение : ', number, ' сумма :', sum )
    if sum > 100: break

# Задание 7

def fuct(n: int):
    mylist = range( 1, n + 1 )
    sum = 1
    for i in mylist:
        sum = sum * i
        yield sum


num = fuct( 7 )
print( num )
for i in num: print( i )
