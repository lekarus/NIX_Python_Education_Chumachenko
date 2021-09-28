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

    def __getitem__(self, item):
        return Transport.transport_list[item]

    def __len__(self):
        return len(Transport.transport_list)

    def __sub__(self, other):
        Transport.transport_list.remove(other.info)

    def __add__(self, other):
        Transport.transport_list.append(other.info)

    def __reversed__(self):
        Transport.transport_list = Transport.transport_list[::-1]


class Car(Transport):
    def __init__(self, s_number, year, e_type):
        super().__init__(s_number, year, e_type)
        Transport.transport_list.append(self.info)

    @property
    def info(self):
        return f'Car {self.year} year of issue'

    def move(self):
        print(f'{self.s_number} car is moving')
        super().move()


class Airplane(Transport):
    def __init__(self, s_number, year, e_type,):
        super().__init__(s_number, year, e_type)
        Transport.transport_list.append(self.info)

    @property
    def info(self):
        return f'airplane {self.year} year of issue'

    def move(self):
        print(f'{self.s_number} airplane is moving')


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
        print(f'{self.s_number} train is moving')


class Helicopter(Transport):
    def __init__(self, s_number, year, e_type, n_blades):
        super().__init__(s_number, year, e_type)
        self.n_blades = n_blades
        Transport.transport_list.append(self.info)

    @property
    def info(self):
        return f'Helicopter with {self.n_blades} blades {self.year} year of issue'

    def move(self):
        print(f'{self.s_number} helicopter is moving')


class Hybrid(Car, Airplane):
    def __init__(self, s_number, year, e_type):
        super().__init__(s_number, year, e_type)

    def move(self):
        super().move()


car = Car(1029, 2008, 'petrol')
airplane = Airplane(1031, 2001, 'kerosene')
train = Train(1001, 1990, 'diesel', 'night')
helicopter = Helicopter(1035, 2000, 'kerosene', 4)

train.move()
print(helicopter.info)
helicopter.year = 2009
print(helicopter.info)
print(car.info)
airplane.start()
airplane.stop()

airplane - airplane
airplane + airplane

reversed(airplane)

for i in airplane:
    print(i)

hybrid = Hybrid(1041, 2020, 'diesel')
hybrid.move()
