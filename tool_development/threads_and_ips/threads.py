from threading import Thread
import time

def car(speed, driver):
    path = 0

    while path <= 100:        
        path += speed
        time.sleep(0.5)
        print(f'Piloto: {driver}, Km: {path}')

t_car1 = Thread(target=car, args=[1, 'Leandro'])
t_car2 = Thread(target=car, args=[2, 'Ana'])

t_car1.start()
t_car2.start()
# car1(10)
# car2(20)