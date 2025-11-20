class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def get_time(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"

    def set_time(self, hour=None, minute=None, second=None):
        if hour is not None:
            self.__hour = hour
        if minute is not None:
            self.__minute = minute
        if second is not None:
            self.__second = second

    
    def add(self, hour=0, minute=0, second=0):
        total_seconds = self.__hour * 3600 + self.__minute * 60 + self.__second
        total_seconds += hour * 3600 + minute * 60 + second

        self.__hour = (total_seconds // 3600) % 24
        self.__minute = (total_seconds % 3600) // 60
        self.__second = total_seconds % 60


t = Time(10, 20, 30)
print("Initial time:", t.get_time())

t.set_time(12) 
print("After setting hour:", t.get_time())

t.set_time(12, 45)
print("After setting hour, minute:", t.get_time())

t.add(minute=30)
print("After adding 30 minutes:", t.get_time())

t.add(1, 20, 10)
print("After adding 1:20:10:", t.get_time())
