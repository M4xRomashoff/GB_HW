# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 06.03.2022
# version = 1
# ----------------------------------------------------------------------------

# Задание 1 ------------------------------------------------------------------


def div_func(a, b):
    if b != 0:
        print(a/b)
    else: print("Второе чило н может быть нулем !")

def div_func_try(a, b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print( "Второе чило н может быть нулем !" )

a = int(input('Введите делимое : '))
b = int(input('Введите делитель : '))

div_func(a, b)
div_func_try(a, b)

# Задание 2 ------------------------------------------------------------------

def print_info(name, last_name, dob, city, email, phone):
    print(f'name  {name}; last_name {last_name}; dob {dob}; city {city}; email {email}: phone {phone}')

print_info(name = 'Bob', last_name='Jobs', dob='12.12.2012', city='Mexico', email='mymail@g.com', phone=1212121212)

# Задание 3 ------------------------------------------------------------------

def my_func(a, b ,c):
    if (a < b) and (a < c) : return b + c
    if (b < a) and (b < c): return a + c
    if (c < a) and (c < b): return a + b

print(my_func(1, 2, 3))
print(my_func(2, 1, 3))
print(my_func(2, 3, 1))


# Задание 4 ------------------------------------------------------------------

def my_func_stepen(x:float, y:int):
    z=1
    for i in range(1,abs(y)+1):
        z = z *x
    return (1/z)

x = float(input('Введите положительное действительное число : '))
y = int(input('Ведите целое отрицательное число : '))

print(my_func_stepen(x, y))
print(pow(x,y))  #Проверка



# Задание 5 ------------------------------------------------------------------

def sum_func():
    total = 0
    while True:
        list = input("Введите числа через пробел, для выхода введите любую букву :").split()
        for i in list:
            try:
                total = total + int(i)
            except :
                return total
        print('Промежуточное значение : ', total)

print(sum_func(),' - итоговая сумма')


# Задание 6 ------------------------------------------------------------------


def int_func(text):
    return text.title()

print(int_func('abcd'))


# Задание 7 ------------------------------------------------------------------

def text_title(text):
    s = ''
    list = text.split()
    for i in list:
        s = s + int_func(i)+' '
    return s

print(text_title('abc bcd bcv bnh bhj khkhkjhkjk'))
