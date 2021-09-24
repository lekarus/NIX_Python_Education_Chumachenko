# машина, самолет, поезд, корабль
from abc import ABC, abstractmethod


class Engine:
    def __init__(self, e_type):
        self.e_type = e_type

    def start(self):
        print(f'{self.e_type} engine started')

    def stop(self):
        print(f'{self.e_type} engine stopped')


class Transport(Engine, ABC):
    transport_list = []

    def __init__(self, s_number, year, e_type):
        self.s_number = s_number
        self.year = year
        super().__init__(e_type)

    @classmethod
    def get_transports(cls):
        print(f'{cls.transport_list}')

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def __init__(self, s_number, year, e_type, color):
        super().__init__(s_number, year, e_type)
        self.color = color
        Transport.transport_list.append(self.info)

    @property
    def info(self):
        return f'{self.color} car, {self.year} year of issue'

    def move(self):
        print(f'{self.s_number} car moving')


class Airplane(Transport):
    def __init__(self, s_number, year, e_type, capacity):
        super().__init__(s_number, year, e_type)
        self.capacity = capacity
        Transport.transport_list.append(self.info)

    @property
    def info(self):
        return f'airplane {self.year} year of issue accommodates {self.capacity} people'

    def move(self):
        print(f'{self.s_number} airplane moving')


class Train(Transport):
    def __init__(self, s_number, year, e_type, t_type):
        super().__init__(s_number, year, e_type)
        self.t_type = t_type
        Transport.transport_list.append(self.info)
        pass

    @property
    def info(self):
        return f'{self.t_type} train {self.year} year of issue'

    def move(self):
        print(f'{self.s_number} train moving')


class Helicopter(Transport):
    def __init__(self, s_number, year, e_type, n_blades):
        super().__init__(s_number, year, e_type)
        self.n_blades = n_blades
        Transport.transport_list.append(self.info)

    @property
    def info(self):
        return f'Helicopter with {self.n_blades} blades {self.year} year of issue'

    def move(self):
        print(f'{self.s_number} train moving')


car = Car(1029, 2008, 'petrol', 'yellow')
airplane = Airplane(1031, 2001, 'kerosene', 130)
train = Train(1001, 1990, 'diesel', 'night')
helicopter = Helicopter(1035, 2000, 'kerosene', 4)

train.move()
print(helicopter.info)
helicopter.year = 2009
print(helicopter.info)
car.color = 'red'
print(car.info)
airplane.start()
airplane.stop()
print(Transport.transport_list)
