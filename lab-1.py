import copy


class Unit:
    # конструктор
    def __init__(self, types, manufacturer='', lifetime=''):
        self.type = types
        self.manufacturer = manufacturer
        self.lifetime = lifetime
        print("Создание объекта Unit " + self.type)
    # метод для просмотра полей данных
    def display_info(self):
        print(f"Type: {self.type} Manufacturer: {self.manufacturer}  Lifetime: {self.lifetime}")
    def compare_lifetime(_a, _b):
        a = _a.lifetime
        b = _b.lifetime
        print (a,b)
        print(_a.type if a > b else _b.type)
    # деструктор
    def __del__(self):
        print('Вызван деструктор для '+ self.type) 
        print('Объект ' + self.type + ' удален') 
        
router = Unit("Router")      # Определение объекта Маршрутизатор / вызов конструктора, который возвращает объект класса Unit
gateway = Unit("Gateway")    # Определение объекта Шлюз / вызов конструктора, который возвращает объект класса Unit
switch = Unit("Switch")      # Определение объекта Коммутатор / вызов конструктора, который возвращает объект класса Unit

router.manufacturer = "Cisco"
router.lifetime = "8"
router.display_info()

gateway.manufacturer = "Континент"
gateway.lifetime = "5"
gateway.display_info()

switch.manufacturer = "Allied Telesys"
switch.lifetime = "6"
switch.display_info()

xcopy = copy.copy(router)       # Используем модуль копирования вместо конструктора копирования
xcopy.display_info()
# xcopy = copy.deepcopy(router)

xcopy.compare_lifetime(gateway)

del router
del gateway
del switch

