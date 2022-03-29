# ----------------------------------------------------------------------------
# Created By  : Ромашов Максим
# Created Date: 28.03.2022
# version = 1
# ---------------------------------------------------------------------------

# Задание 1

import time
from multiprocessing import Process, Queue

q = Queue()
q_stop = Queue()
q_stop.put( False ) # эта очредь для остановки процесса при ошибке. Не важно что в ней стоит


class TrufficLight:
    global q
    global q_stop

    def __init__(self):
        self.__color = 'red'

    def running(self, q, q_stop):
        while True:
            if q_stop.empty():
                break
            self.__color = 'red'
            q.put( self.__color )
            print( 'Светофор в работе. Цвет : ', self.__color )
            time.sleep( 7 )
            self.__color = 'yellow'
            q.put( self.__color )
            print( 'Светофор в работе. Цвет : ', self.__color )
            time.sleep( 2 )
            self.__color = 'green'
            q.put( self.__color )
            print( 'Светофор в работе. Цвет : ', self.__color )
            time.sleep( 5 )


tl = TrufficLight()


def check(q, q_stop):
    good_list = ['red', 'yellow', 'green']
    new_list = []
    while True:
        state = q.get()
        new_list.append( state )
        # print(new_list)
        if len( new_list ) == len( good_list ):
            if new_list != good_list:
                q_stop.get()  # очитить очередь как флаг остановки процессов
                print( 'Обнаружена ошибка, светофор отсановлен !' )
                break
            new_list.clear()
        print( 'Мы видим цвет :', state )


if __name__ == '__main__':
    p1 = Process( target=check, args=(q, q_stop,) )
    p2 = Process( target=tl.running, args=(q, q_stop,) )
    p1.start()
    p2.start()
