
# 1-masala
class  Vihicle:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

class Car(Vihicle):
    def honk(self):
        return "Bip-Bip"

class Bicycle(Vihicle):
    def pedal(self):
        return "aylantir"

class Truck(Vihicle):
    def load_cargo(self):
        return "cargo loaded"

car=Car("BMW",200)
print(car.honk())
bike=Bicycle("ONIX",30)
print(bike.pedal())
truck=Truck("MERS",150)
print(truck.load_cargo())


# 2-masala
class Animal:
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return "Roar"

class Eagle(Animal):
    def make_sound(self):
        return "Screech"

class Shark(Animal):
    def make_sound(self):
        return "Splash"


lion=Lion()
print(lion.make_sound())
eagle=Eagle()
print(eagle.make_sound())
shark=Shark()
print(shark.make_sound())



# 3-masala

class Employee:
    def get_salary(self):
        pass

class Manager(Employee):
    def __init__(self,fixed_salary):
        self.fixed_salary=fixed_salary

    def get_salary(self):
        return self.fixed_salary


class Developer(Employee):
    def __init__(self,hourly_rate,hours_worked):
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def get_salary(self):
        return self.hourly_rate*self.hours_worked

class Designer(Employee):
    def __init__(self,loyiha_soni,har_bir_loyiha_narxi):
        self.loyiha_soni=loyiha_soni
        self.har_bir_loyiha_narxi=har_bir_loyiha_narxi

    def get_salary(self):
        return self.loyiha_soni*self.har_bir_loyiha_narxi

manager=Manager(3000)
print(manager.get_salary())
developer=Developer(10,120)
print(developer.get_salary())
disigner=Designer(5,200)
print(disigner.get_salary())

# 4-masala
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Electronics(Product):
    def apply_discount(self):
        return self.price*0.9


class Clothing(Product):
    def apply_discount(self):
        return self.price*0.8


class Food(Product):
    def __init__(self,name,price,expiry_days):
        super().__init__(name,price)
        self.expiry_days=expiry_days

    def check_expiry(self):
        if self.expiry_days>0:
            return "Fresh"
        else:
            return "Expired"

phone=Electronics("Iphone",1000)
print(phone.apply_discount())
shim=Clothing("shim",50)
print(shim.apply_discount())
sut=Food("sut",10,3)
print(sut.check_expiry())