class Helicopter:
    # Опис вертольота
        def __init__(self, passengers=9, name="fIGHT", max_speed=269):
        #Властивості вертольота
            self.__passengers = passengers
            self.__name = name
            self.__max_speed = max_speed
    
        #Метод доступу до приватних полів
        # def get_passengers(self):
        #     return self.__passengers
    
        # def set_passengers(self, passengers):
        #     self.__passengers = passengers
        @property
        def passengers(self):
            return self.__passengers
        
        def passengers (self, passengers):
            self.__passengers = passengers

        def get_name(self):
            return self.__name

        def set_name(self, name):
            self.__name = name

        def get_max_speed(self):
            return self.__max_speed

        def set_max_speed(self, max_speed):
            self.__max_speed = max_speed
    #Перевизнкачення методу
        def __str__(self):
            return(f"Helicopter: Назва: {self.__name}, Кількість пасажирів: {self.__passengers}, Максимальна швидкість: {self.__max_speed}")
        def __repr__(self):
            return(f"Helicopter: Назва: {self.__name}, Кількість пасажирів: {self.__passengers}, Максимальна швидкість: {self.__max_speed}")
    #Видалення (деструктор)
        def __del__(self):
            print(f"Об'єкт: {self.__name} Видалено")
    # Інціалізація Helicopter
def main():
    helicopter1 = Helicopter(10, "Rafik", 290)
    helicopter2 = Helicopter(6, "Bobr", 300)
    helicopter3 = Helicopter(20, "Bobik", 315)
    helicopter4 = Helicopter()
    #Виведення    
    print(helicopter1)
    print(helicopter2)
    print(helicopter3)
    print(helicopter4)

    print(repr(helicopter1))
main()    