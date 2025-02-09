# with open("transport.pyy", "r") as file:
#     for line in file:
#         print(line, end="")

# with open("transport.pyy", "r") as file:
#     str1 = file.readline()
#     print(str1, end="")
#     str2 = file.readline()
#     print(str2, end="")

# import shelve

# FILENAME = "hello.txt"

# with shelve.open(FILENAME) as states:
#     states["london"] = "Great Britain"
#     states["Paris"] = "France"
#     states["Yerevan"] = "Armenia"

# with shelve.open(FILENAME) as states:
#     for city in states.keys():
#         print(city, end=" ")
#     print()
#     for country in states.values():
#         print(country, end=" ")
#     print()

import csv
import pickle

FILENAME = "user.csv"

# name = "Tom"
# age = 19

# with open(FILENAME, "wb") as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)

# with open(FILENAME, "rb") as file:
#     name  = pickle.load(file)
#     age = pickle.load(file)
#     print("Name: ", name, "Age: ", age)

# users = [
#     {"name":"Tom", "age": 38},
#     {"name": "Lilit", "age": 21}
# ]

# with open(FILENAME, "w", newline="") as file:
#     header = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()

#     writer.writerows(users)

#     another_user = {"name": "Lucy", "age": 35}
#     writer.writerow(another_user)

# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], "-", row["age"])



# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)

# with open(FILENAME, "rb") as file:
#     my_load = pickle.load(file)
#     for l in my_load:
#         print(f"Name: {l[0]} \t Age: {l[1]}")

# countries = (
#     ("Germany", 80.2, (("Hamburg", 1.7), ("Berlin", 3.3))),
#     ("France", 66, (("Paris", 2.2),))
# )

# for country in countries:
#     countryName, cPop, cities = country
#     print(f"Country name: {countryName}\tPopulation: {cPop}")
#     for city in cities:
#         cityName, cityPopulation = city
#         print(f"City name: {cityName}\tPopulation: {cityPopulation}")

# users = {
#     1: "Lilit",
#     "2": "Serine",
#     3: "Davit"
# }

# obj = {}

# obj2 = dict()
# print(type(obj2))

# users = {
#     "+37495350568": "Lilit",
#     "+37499248836": "Serine",
#     "+37455450568": "Anna"
# }

# print(users["+37495350568"]) #Lilit

# users["33333"] = "Henrik"

# if "+37495350568" in users:
#     print(users["+37495350568"])

# del users["+37495350568"]


# users2 = {
#     "2345": "Aramayis"
# }

# users.update(users2)

# print(users)
# print()

# for key in users:
#     print(key, "-", users[key])
# print()
# for key, value in users.items():
#     print(key, "-", value)

# for key in users.keys():
#     print(key)

# for value in users.values():
#     print(value)

# my_users = {
#     "Lilit": {
#         "age": 21,
#         "gender": "female"
#     },
#     "Fazilia": {
#         "married": True,
#         "works": False
#     }
# }

# print(my_users["Lilit"]["gender"])

# if "works" in my_users["Lilit"]:
#     print(my_users["Lilit"]["works"])

# an_users = frozenset(["Lilit", "Armine", "Qristine"])

# print(len(an_users))
# print("Lilit" not in an_users)
# p = an_users.copy()
# print(p)
# users3 = {"Lilit", "Armine"}
# print(users3.issubset(an_users))
# print(an_users.issuperset(users3))

# users5 = {123, "T", True}

# my_union = an_users.union(users5)
# my_inter = an_users.intersection(users3)
# m_diff = an_users.difference(users3)

# print(my_union)
# print(my_inter)
# print(m_diff)

# import csv

# FILENAME = "my_users.csv"

# users = [
#     {"name": "Lilit", "age": 21},
#     {"name": "Armine", "age": 26}
# ]

# with open(FILENAME, "w", newline="") as file_obj:
#     columns = ["name","age"]
#     writer = csv.DictWriter(file_obj, fieldnames=columns)
#     writer.writeheader()

#     writer.writerows(users)

#     writer.writerow({"name": "Baby", "age": 65})

# with open(FILENAME, "r", newline="") as file_obj:
#     reader = csv.DictReader(file_obj)
#     for row in reader:
#         print(row["name"], "-", row["age"])

# import pickle

# #dump(obj, file) 
# # load(file)

# FILENAME = "hello.dat"

# name = "Lilit"
# age = 21

# with open(FILENAME, "wb") as file_obj:
#     pickle.dump(name, file_obj)
#     pickle.dump(age, file_obj)

# with open(FILENAME, "rb") as file_obj:
#     name = pickle.load(file_obj)
#     age = pickle.load(file_obj)
#     print(f"Name: {name}\tAge: {age}")

#open(file[, flag="c"[, protocol=None[, writeback=False]]])
#c
#r
#w
#n
#close()


# import shelve
# FILENAME="STATES"

# with shelve.open(FILENAME) as states:
#     states["Great Britain"] = "London"
#     states["Arm"] = "Yerevan"

# with shelve.open(FILENAME) as states:
#     states["Germany"] = "Berlin"
#     states["France"]  = "Paris"

# with shelve.open(FILENAME) as states:
#     for state in states:
#         print(state, "-", states[state])

# with shelve.open(FILENAME) as states:
#     for key in states.keys():
#         print(key, end=" ")
#     print()
#     for value in states.values():
#         print(value, end=" ")
#     print()

# def get_emp_data ():
#     lname=input("Inout your last name:")
#     fname=input("Input your first name:")
#     age=int(input("Input your age:"))
#     is_married=bool(input("Enter False(non Married) or True (Married) "))
#     return fname,lname,age,is_married
# emp=get_emp_data()

# i=0
# while i<len(emp):
#     print(emp[i])
#     i+=1

# def is_prime(n):
#     if n==1:
#         return False
#     i = 2
#     while i<=n//2:
#         if n%i==0:
#             return False
#         else:
#             i+=1
#     return True

# print(is_prime(5))

# data = [(3, 4), (1, 2), (3, 1), (2, 3), (1, 4)]
# #(1,2), (1,4), (2,3), (3,1), (3,4)
# for i in range(len(data)):
#     for j in range(len(data)-i-1):
#         if data[j][0]>data[j+1][0]:
#             data[j][0], data[j+1][0] = data[j+1][0], data[j][0]
#             data[j][1], data[j+1][1] = data[j+1][1], data[j][1]
#         elif data[j][0] == data[j+1][0]:
#             if data[j][1]>data[j+1][1]:
#                 data[j][1], data[j+1][1] = data[j+1][1], data[j][1]

# print(data)

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# my_dict = {}
# for item in words:
#     if item not in my_dict:
#         my_dict[item] = 1
#     else:
#         my_dict[item]+=1

# for key, value in my_dict.items():
#     print(key, "-", value)

# students = {
#     "Alice": [85, 90, 78],
#     "Bob": [72, 88, 91],
#     "Charlie": [89, 94, 90]
# }
# f_item = None
# f_max = -1
# for key, value in students.items():
#     average = sum(value)/len(value)
#     if average>f_max:
#         f_max = average
#         f_item = key

# print(f_item)

# tuple1 = (1, 2, 3, 4,4, 5)
# tuple2 = (4, 5, 6, 7, 8)

# tuple3 = tuple(set([item for item in tuple1 if item in tuple2]))
# print(tuple3)

# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 5, "c": 15, "d": 25}
# dict3 = {}
# for key in dict1:
#     if key not in dict3:
#         if key in dict2:
#             dict3[key] = dict1[key]+dict2[key]
#         else:
#             dict3[key] = dict1[key]

# for key in dict2:
#     if key not in dict3:
#         dict3[key] = dict2[key]

# print(dict3)

# tuples = ("apple", "banana", "watermelon", "grape")

# f_max = -1
# f_item = None
# for item in tuples:
#     if len(item)>f_max:
#         f_max = len(item)
#         f_item = item

# print(f_item)

# people = {
#     "Alice": (1200, 5000),  # (համբավ, վարձատրություն)
#     "Bob": (1100, 4000),
#     "Charlie": (1500, 6000),
#     "David": (950, 3000),
#     "Eve": (1200, 4500)
# }
# h_max = -1
# name = None
# cost = None
# for key, value in people.items():
#     if value[0]>h_max:
#         h_max = value[0]
#         name = key
#         cost = value[1]

# print(tuple([name, cost]))

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         if age in range(1, 101):
#             self.__age = age
#         else:
#             print("Unacceptable age given")
    
#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         if age in range(1,101):
#             self.__age = age
#         else:
#             print("Unacceptable age")

#     def display_info(self):
#         print(f"Hello, I am {self.name}. I am {self.age} years old")

# person1 = Person("Lilit", 21)
# print(person1.name)
# person1.age = 22
# print(person1.age)

# person1.__age = 23

# print(person1.__age)

#@property
#@getter_հատկություն․setter

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name:str)->None:
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Lion(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)

    def make_sound(self):
        print(f"Lion {self.name} sounds like AHHH")

    def eat(self):
        print(f"Lion {self.name} eats meat")


lion = Lion("gaby")
lion.make_sound()
lion.eat()
