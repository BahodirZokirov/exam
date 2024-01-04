from faker import Faker
from random import randint
a = Faker ()
lt = []

name = a.name()
for i in range (10):
    age = randint(1, 100)
    lt.append(f"{i}. {name} {age} \n")

with open("test1.txt", "w") as file:
    for i in lt:
        file.write(i)