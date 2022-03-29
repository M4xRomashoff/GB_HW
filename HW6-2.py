# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 29.03.2022
# version = 1
# ---------------------------------------------------------------------------

# Задание 2

class Road:
    dencity = 1500  # плотость асфальта кг на метр в кубе

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_amount(self):
        return self._length * self._width * 0.01 * self.dencity


r1 = Road( 10, 10 )
print( 'для этой дороги необходмо ', r1.get_amount(), ' кг асфальта' )


# Задание 3

class Worker:
    salary = {'рабочий': {"wage": 10, "bonus": 20},
              'бригадир': {"wage": 12, "bonus": 30},
              'директор': {"wage": 30, "bonus": 40},
              'бухгалтер': {"wage": 20, "bonus": 50},
              'водитель': {"wage": 15, "bonus": 60},
              '': {"wage": 0, "bonus": 0},
              }

    def __init__(self):
        self.name = ''
        self.surname = ''
        self.position = ''
        self._income = self.salary.get( self.position )

    def update(self):
        self._income = self.salary.get( self.position )


class Position( Worker ):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get( 'wage' ) * 40 + self._income.get( 'bonus' )


p1 = Position()
p1.name = 'Толик'
p1.surname = 'Сидоров'
p1.position = 'рабочий'

p2 = Position()
p2.name = 'Вова'
p2.surname = 'Петров'
p2.position = 'бригадир'

p1.update()  # обновить данные о зарплате согласно занимаемой позиции
p2.update()

print( p1.get_full_name() )
print( p1.get_total_income() )
print( p2.get_full_name() )
print( p2.get_total_income() )


# Задание 4

class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'none'
        self.name = 'none'
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print( self.name, '  ', self.color, 'цвета едет со скоростью ', self.speed )

    def stop(self):
        self.speed = 0
        print( self.name, 'стоит' )

    def turn(self, direction):
        print( self.name, 'поввернула на ', direction )

    def show_speed(self):
        print( self.name, ' едет со скоростью ', self.speed )


class TownCar( Car ):
    def show_speed(self):
        print( self.name, ' едет со скоростью ', self.speed )
        if self.speed > 60: print( self.name, ' едет с Превышением скорости !' )


class WorkCar( Car ):
    def show_speed(self):
        print( self.name, ' едет со скоростью ', self.speed )
        if self.speed > 40: print( self.name, ' едет с Превышением скорости !' )


class PoliceCar( Car ):
    pass


class SportsCar( Car ):
    pass


tc = TownCar()
tc.name = 'Городской автомобиль'
tc.color = 'белый'

wc = WorkCar()
wc.name = 'рабочая машина'
wc.color = 'грязная'

cops = PoliceCar()
cops.name = 'полицейская машина'
cops.color = 'синяя'

bolid = SportsCar()
bolid.name = 'молния'
bolid.color = 'красная'

tc.go( 30 )
tc.stop()
tc.go( 80 )
tc.turn( 'лево' )
tc.turn( 'право' )
tc.show_speed()

print( '-' * 50 )

wc.go( 30 )
wc.stop()
wc.go( 60 )
wc.turn( 'лево' )
wc.turn( 'право' )
wc.show_speed()

print( '-' * 50 )

cops.go( 30 )
cops.stop()
cops.go( 90 )
cops.turn( 'лево' )
cops.turn( 'право' )
cops.show_speed()

print( '-' * 50 )

bolid.go( 30 )
bolid.stop()
bolid.go( 50 )
bolid.turn( 'лево' )
bolid.turn( 'право' )
bolid.show_speed()


# Задание 5

class Stationary:
    title = ''

    def draw(self):
        print( 'Запуск отрисовки ', self.title )


class Pen( Stationary ):
    def draw(self):
        print( 'Запуск отрисовки ручкой ', self.title )


class Pencil( Stationary ):
    def draw(self):
        print( 'Запуск отрисовки карандашом ', self.title )


class Handle( Stationary ):
    def draw(self):
        print( 'Запуск отрисовки маркером ', self.title )


s = Stationary()
s.title = 'что-то'

pn = Pen()
pn.title = 'Ручка-Штучка'

pcl = Pencil()
pcl.title = 'карандаш-марандаш'

mrk = Handle()
mrk.title = 'Marker'

s.draw()
pn.draw()
pcl.draw()
mrk.draw()
