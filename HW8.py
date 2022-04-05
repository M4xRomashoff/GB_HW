# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 05.04.2022
# version = 1
# ---------------------------------------------------------------------------

class Date:
    date = []

    def __init__(self, date):
        self.date = date

    @classmethod
    def convert(cls, date):
        try:
            date_c = date.split( '-' )
            cls.date.clear()
            for i in date_c:
                cls.date.append( int( i ) )
            print( cls.date )
            return cls( cls.date )
        except:
            print( 'что-то не так с датой' )

    @staticmethod
    def validate(date):
        month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            if date[2] <= 0:
                print( 'Год может быть только положительным' )
            elif (date[1] < 1) or (date[1] > 12):
                print( 'Невено введен месяц' )
            elif (date[0] < 1) or (date[0] > month.get( date[1] )):
                print( 'неверно введен день' )
            else:
                print( 'дата записана верно' )
                print( date[0] )
                print( date[1] )
                print( date[2] )

        except:
            print( 'что-то по пошло не так' )


d = Date.convert( '30-12-1233' )
d.validate( d.date )
print( '-' * 30 )
d1 = Date.convert( '0-12-1233' )
d1.validate( d.date )
print( '-' * 30 )
d2 = Date.convert( '11-31-1233' )
d2.validate( d.date )
print( '-' * 30 )
d3 = Date.convert( '30-12-0' )
d3.validate( d.date )
print( '-' * 30 )


class ZeroDev( Exception ):
    def __init__(self, text):
        self.text = text


try:
    a = int( input( 'Введите делимое : ' ) )
    b = int( input( 'Введите делитель :' ) )
    if b == 0: raise ZeroDev( 'Онаружено деление на ноль !' )

except (ValueError, ZeroDev) as err:
    print( err )

else:
    print( a / b )
finally:
    print( 'программа отработала ' )


# Задание 3

class Digit( Exception ):
    def __init__(self, text):
        self.text = text


list1 = []
while True:
    try:
        a = input( 'Введите число, для остановки введите "stop" : ' )
        if a == 'stop': break
        if a.isnumeric():
            list1.append( int( a ) )
        else:
            raise Digit( 'это не число' )
    except Digit as err:
        print( err )

print( list1 )


# Задание 4, 5, 6

class Digit( Exception ):
    def __init__(self, text):
        self.text = text


class Warehouse:
    instock = 0

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info_name(self):
        print( f"Name: {self.__name} " )

    def add_item(self):
        self.instock += 1

    def add_items(self, num: int):
        self.instock += num

    def remove_item(self):
        if self.instock > 0:
            self.instock -= 1

    def remove_items(self, num: int):
        if (self.instock - num) > 0:
            self.instock -= num
        else:
            self.instock = 0


class Equipment( Warehouse ):
    def __init__(self, name, type1):
        super().__init__( name )
        self.__type = type1

    @property
    def type(self):
        return self.type

    def display_info_type(self):
        print( f"Type: {self.__type} " )


class Printer( Equipment ):
    def __init__(self, name, type1, id, ink_type):
        super().__init__( name, type1 )
        self.__id = id
        self.ink_type = ink_type

    def display_info_ink_type(self):
        print( f"ink type : {self.ink_type} " )

    def display_info_id(self):
        print( f"Id: {self.__id} " )

    def display_info(self):
        self.display_info_name()
        self.display_info_type()
        self.display_info_id()
        self.display_info_ink_type()


class Scaner( Equipment ):
    def __init__(self, name, type1, id, size):
        super().__init__( name, type1 )
        self.__id = id
        self.size = size

    def display_info_size(self):
        print( f"Size : {self.size} " )

    def display_info_id(self):
        print( f"Id: {self.__id} " )

    def display_info(self):
        self.display_info_name()
        self.display_info_type()
        self.display_info_id()
        self.display_info_size()


class Copyer( Equipment ):
    def __init__(self, name, type1, id, quality):
        super().__init__( name, type1 )
        self.__id = id
        self.quality = quality

    def display_info_quality(self):
        print( f"Quality : {self.quality} " )

    def display_info_id(self):
        print( f"Id: {self.__id} " )

    def display_info(self):
        self.display_info_name()
        self.display_info_type()
        self.display_info_id()
        self.display_info_quality()


p1 = Printer( 'HP', 'printer', 'HP123', 'color' )
p2 = Printer( 'Epson', 'type2', 'EPSON234', 'B&W' )

s1 = Scaner( 'HP_scaner', 'Scaner', 'Hp_scan567', 'A4' )
s2 = Scaner( 'DELL_scaner', 'Scaner', 'DELL_scan567', 'A3' )

c1 = Copyer( 'Espon_copy', 'Copyer', '3267Cop', '300 dpi' )
c2 = Copyer( 'Dell_copy', 'Copyer', 'Del3267Cop', '600 dpi' )

p1.add_item()
p1.add_items( 5 )
p2.add_items( 12 )

s1.add_items( 6 )
s2.add_items( 13 )

c1.add_items( 13 )
c2.add_items( 12 )

warehouse = [p1, p2, s1, s2, c1, c2]


def checkInt(str):
    try:
        int( str )
        return True
    except ValueError:
        return False


def show_warehouse():
    for item in warehouse:
        print( 'in stock :', item.instock )
        item.display_info()
        print( '--' * 50 )


# show_warehouse()

p1.remove_item()
p2.remove_items( 2 )
s1.remove_item()
s2.remove_items( 2 )
c1.remove_item()
c2.remove_items( 2 )

# show_warehouse()


# работа с данными

while True:
    names_list = []
    for item in warehouse:
        names_list.append( item.name )
    print( names_list )

    item_enterd = input( 'Введите наминование товара (пустая строка для выхода) : ' )
    if item_enterd == '': break
    quan = input( 'Введите количество товара добавить (с минусом чтобы убавить ) : ' )
    try:
        if checkInt( quan ):
            quant = int( quan )

            if item_enterd in names_list:
                for i in range( len( warehouse ) ):
                    if item_enterd == warehouse[i].name:
                        if quant > 0:
                            warehouse[i].add_items( quant )
                        else:
                            warehouse[i].remove_items( abs( quant ) )
                        show_warehouse()
            else:
                print( 'товар не найден' )
        else:
            raise Digit( 'количество должно быть целое число !' )
    except Digit as err:
        print( err )


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex( self.real + other.imag, self.real + other.imag )

    def __mul__(self, other):
        return Complex( (self.real * other.real) - (self.imag * other.imag),
                        (self.imag * other.real) + (self.real * other.imag) )

    def __str__(self):
        return (f'{self.real} + {self.imag}i')


a = Complex( 2, 2 )
b = Complex( 3, 3 )
с = Complex( 5, 12 )

print( 'число 1 : ', a )
print( 'число 2 : ', b )
print( 'число 3 : ', с )

print( f'сложение  : ({a}) + ({b}) =  ({a + b})' )
print( f'умножение : ({a}) * ({b}) =  ({a * b})' )

print( f'сложение  : ({a}) + ({с}) =  ({a + с})' )
print( f'умножение : ({a}) * ({с}) =  ({a * с})' )
