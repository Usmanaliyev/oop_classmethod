# class Car:
#     def __init__(self):
#         self.__mileage=0
#
#     def drive(self,km):
#         self.__mileage+=km
#
#     def get_mileage(self):
#         return self.__mileage
#     @classmethod
#     def is_service_needed(cls,mileage):
#         return mileage>1000
#
# car=Car()
# car.drive(5000)
# car.drive(6000)
# print(car.get_mileage())
# print(Car.is_service_needed(11000))




# class Student:
#     __students_count=0
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#         Student.__students_count+=1
#
#     @classmethod
#     def get_students_count(cls):
#         return cls.__students_count
#     def is_adult(self):
#         return self.__age>=18
#
# s1=Student("Ali",19)
# s2=Student("Bobur",17)
# print(Student.get_students_count())
# print(s1.is_adult())
# print(s2.is_adult())

# class Product:
#     __discount=0
#     def __init__(self,price):
#         self.__price=price
#
#     @classmethod
#     def set_discount(cls,percent):
#         cls.__discount=percent
#     def calculate_tax(self,amount):
#         return amount *1.05
#     def get_price(self):
#         return self.__price*(1-Product.__discount/100)
# p1=Product(1000)
# Product.set_discount(10)
# print(p1.get_price())
# print(p1.calculate_tax(900))