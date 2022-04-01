# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 30.03.2022
# version = 1
# ---------------------------------------------------------------------------

# Задание 1

class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        # находим максимальнцю длину числа в матрице
        max_l = 0
        for item in self.list:
            for item2 in item:
                if len( str( item2 ) ) > max_l:
                    max_l = len( str( item2 ) )

        for item in self.list:
            for item2 in item:
                len_item = len( str( item2 ) )
                s = (' ' * (max_l - len_item))  # вычисляем отступ
                print( f'{s}{item2} ', end='' )
            print( '' )
        return ''

    def __add__(self, other):
        result = []
        res2 = []
        for item, item_o in zip( self.list, other.list ):
            res2.clear()
            for item2, item2_o in zip( item, item_o ):
                res2.append( item2 + item2_o )
            result.append( res2.copy() )
        return Matrix( result )


m1 = Matrix( [[1, 2, 3], [4, 5, 6], [7, 8, 9]] )
m2 = Matrix( [[1, 1, 1], [1, 1, 1], [1, 1, 1]] )
m3 = Matrix( [[1, 22, 33], [44, 55, 6], [7, 58, 19]] )
m4 = Matrix( [[112, 2231, 133], [44, 55, 116], [7, 1158, 1119]] )

print( m1 )
print( m2 )
print( m3 )
print( m4 )
print( m1 + m2)
print( m1 + m2 + m3 )
print( m3 + m4 )


# Задание 2

from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def material(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        super(Coat, self).__init__(self)

    def material(self):
        return f'{self.name} расход материала: {self.size/6.5 + 0.5}'

class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        super(Suit, self).__init__(self)

    @property
    def material(self):
        return f'{self.name}  расход материала: {self.height*2 + 0.3}'

c1 = Coat(12)
c2 = Suit(23)
c1.name = 'Пальто'
c2.name = 'Костюм'

print(c1.material())
print(c2.material)


# Задание 3

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return Cell( self.quantity + other.quantity )

    def __sub__(self, other):
        if self.quantity > other.quantity:
            return Cell( self.quantity - other.quantity )
        else:
            print( 'нельзя из меньшего вычитать большее' )

    def __mul__(self, other):
        return Cell( self.quantity * other.quantity )

    def __truediv__(self, other):
        if self.quantity > other.quantity:
            return Cell( self.quantity // other.quantity )
        else:
            print( 'Нельзя делить не делимое' )

    def make_order(self, members):
        s = ''
        counter = 0
        for i in range( self.quantity ):
            s += '*'
            counter += 1
            if counter == members:
                s += '\n'
                counter = 0
        return s


c1 = Cell( 5 )
c2 = Cell( 6 )
c3 = Cell( 21 )

print( (c1 + c2).quantity, ' сложение' )
c = c1 - c2
print( (c2 - c1).quantity, ' вычитание' )
print( (c1 * c2).quantity, ' умножение' )
print( (c3 / c1).quantity, ' деление' )
print( c1.make_order( 3 ) )
print( '' )
print( c1.make_order( 2 ) )
print( '' )
print( c3.make_order( 5 ) )
print( '' )
