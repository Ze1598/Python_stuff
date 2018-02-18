#Create a class with getter and setter and deleter methods, using property() and @property

#Using property()
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

a = C()
a.x = 2
print('a.x:',a.x)
print()

#Using @property
class C_:
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

b = C_()
b.x = 3
print('b.x:',b.x)
print('-------------------------------------\n')
'''-------------------------------------------------------------------------------'''

#Using property()
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
    
    temperature = property(get_temperature, set_temperature)


c = Celsius(37)
print('c.temperature:',c.temperature)
print('c.to_fahrenheit:',c.to_fahrenheit())
print()

#Using @property
class Celsius_:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

d = Celsius_(40)
print('d.temperature:',d.temperature)
print('d.to_fahrenheit:',d.to_fahrenheit())