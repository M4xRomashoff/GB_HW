# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 01.03.2022
# version = 1
# ----------------------------------------------------------------------------

# Задание 1 -------------------------------------------------------------------

list1 = [1 ,2 , 3, 'a', 'b', [1, 2], ['a', 'b']]
print(' Список ',list1)

for item in list1:
    print(type(item))



#Задание 2 -------------------------------------------------------------------

print(50*'-')
list2 = input('Введите элементы списка через пробел : ').split()
print(50*'-')
print(list2)
list2_1 = list2[::2]    # предварительный список из нечетных элементов
list2_2 = list2[1::2]   # предвартельный список из четных элементов

print(list2_1, 'предварительный список из нечетных элементов')
print(list2_2, 'предвартельный список из четных элементов')

list2_after = [x for y in zip(list2_2, list2_1) for x in y] # соединяем списки по ранжиру

if len(list2_1) > len(list2_2):                             # добывляем полседний неченый элемент, если нет пвры
  list2_after.append(list2[-1])

print(list2_after, ' результат ')


# Задание 3 --------------------------------------------------------------------

print(50*'-')
d = {'Зима':[1, 2, 3], 'Весна' : [4, 5, 6], 'Лето' : [7, 8, 9], 'Осень' : [10, 11, 12]}
month = int(input('Введите месяц чслом : '))

for key, value in d.items():
    if month in value: print(key)


# Задание 4 --------------------------------------------------------------------

print(50*'-')
list4 = input('Введите строку из нескольких слов через пробел : ').split()
for count, value in enumerate(list4, start=1):
    print(count, value[:10])

# Задание 5 --------------------------------------------------------------------

print( 50 * '-' )
reit = [6, 5, 4, 3, 2]
print( reit, 'Оригинал' )
new_number = int( input( 'Введите число : ' ) )

position = -1
for i in range( len( reit ) ):
    if new_number > reit[i]:
        position = i
        break
if position == -1:
    reit.append( new_number )
else:
    reit.insert( position, new_number )
print( reit, 'измененный' )


# Задание 6 --------------------------------------------------------------------

print( 50 * '-' )
quantity_of_products = int(input('Сколько товаров будете вводить ? '))
list6 = []
for i in range(quantity_of_products):
    name = input('Введите название товара : ')
    price = int(input('Введите цену товара : '))
    quantity = int(input('Введите количество товара : '))
    count_type = input('Введите единиуц измерения товара :')
    product = {'название' : name , 'цена' : price, 'количество': quantity, 'единица измерения': count_type}
    list6.append((i+1,product))

#for item in list6: print(item)

nameStat = []
priceStat =[]
quanyityStat = []
count_typeStat = []

for item in  list6:
    nameStat.append(item[1]['название'])
    priceStat.append(item[1]['цена'])
    quanyityStat.append(item[1]['количество'])
    count_typeStat.append(item[1]['единица измерения'])

statD = {'название' : nameStat , 'цена' : priceStat, 'количество': quanyityStat, 'единица измерения': count_typeStat}


for key, value in statD.items():
    print(key, end='')
    print(value)

