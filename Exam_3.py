#1
def card(number,cvc,pin):
    a=[]
    for i in number:
        if i.isdigit():    a.append(i)
    if len(cvc)!=3 or cvc.isdigit()==False:    print('Неверный формат cvc')
    elif len(pin)!=4 or pin.isdigit()==False:    print('Неверный формат pin')
    else:
        return ("".join(map(str,a[:4]+list(len(a[4:])*'*')))),\
               str(len(str(cvc))*'#'),str(len(pin[:3])*'&'+pin[3])
print(card(input('Введите номер карты:\n'),
           input('Введите номер cvc:\n'),input('Введите pin код:\n')))
#2
def decor(func):
    def wrapper(a):
        func(a)
        print('Имя функции: ', func.__name__, 'Аргумент: ',a)
    return wrapper
@decor
def palindrom(text):
    my_str=''.join((text).split())
    my_str1=my_str[::-1]
    print(my_str==my_str1)
palindrom('а роза упала на лапу азора')
#3
from abc import ABC
class company(ABC):
    levels = {1:'junior',2:'middle',3:'senior',4:'lead'}

    def __init__(self, index):
        self._index=index
        self._levels=company.levels[self._index]
        self.__privindex=index

    def _level_up(self):
        self._index+=1
        self._levels=company.levels[self.__privindex]

    def is_lead(self):
        if self._levels=='lead':
            print('Вы достигли последней квалификации ')

    def country(self):
        pass

    def __privmeth(self):
        print('Private method')

class programmer(company):
    def __init__(self, name, age, index):
        super().__init__(index)
        self.name=name
        self.age=age

    def work(self):
        print('working...')
        return self._level_up()

    def info(self):
        return [self.name, self.age, self._index]

    @staticmethod
    def knowledge_base():
        return print(help(company))

    def country(self):
        print('Я живу в Беларуси')

b=programmer('Оксана', 31, 1)
print('Имя: ',b.info()[0],'Возраст: ',b.info()[1],'Квалификация: ',company.levels.get(b.info()[2]))
b.work()
print('Имя: ',b.info()[0],'Возраст: ',b.info()[1],'Квалификация: ',company.levels.get(b.info()[2]))
b.country()
try:
    b.__privmeth()
except AttributeError:
    print('Метод приватный')
# 4
class animals():
    animals_count=0
    eat={1:'Травоядный',2:'Плотоядный',3:'Всеядный'}
    def __init__(self, name, food_type):
        animals.animals_count+=1
        self.name=name
        self._food_type=animals.eat[food_type]
    @classmethod
    def total_count(cls):
        print('Всего: ',cls.animals_count,'зверей')
    @staticmethod
    def eating():
        print('Eating...')
    def info(self):
        print(self.name,'-', self._food_type)
class elephants(animals):
    elephants_count=0
    def __init__(self,name,food_type,height,weight):
        super().__init__(name,food_type)
        self._height=int(height)
        self._weight=int(weight)
        elephants.elephants_count+=1
    def __count(self):
        print('Всего слонов: ',elephants.elephants_count)
    def info(self):
        print(self.name,'весит ',self._weight,'кг и ростом',self._height,'м')
el1=elephants('Белый слон',1,2,1000)
el2=elephants('Необычный слон',2,4,2500)
dog=animals('Собака',3)
cow=animals('Корова',1)
el1.info()
el2.info()
dog.info()
cow.info()
animals.total_count()
el1.info()