
#
#adcionando items a lista com update;
""" fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits) """


""" #remove banana from the list
fruits = {"apple", "banana", "cherry"}
print(fruits,"\n")
fruits.remove("banana")
print(fruits,"\n")
 """
 
 
 #remove banana from the list
""" fruits = {"apple", "banana", "cherry"}
print(fruits,"\n")
fruits.discard("banana")
print(fruits,"\n")
 """
 
 #######################################################################
 #######################################################################
 #######################################################################
 
 #Python DICTIONARIES
 
 #######################################################################
 #######################################################################
 #######################################################################

# Adquirindo dados de uma lista com método get
""" car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
print(car,"\n")
print(car.get("model"),"\n")
 """
 
 
 #Change the "year" value from 1964 to 2020. Alterando valores individuais no dicionario#
 
""" car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.keys()
print(car,"\n")

car["year"] = 2020
print(car,"\n")"""



#Add the key/value pair "color" : "red" to the car dictionary.

""" car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.keys()
print(car,"\n")

car["color"] = "red"
print(car,"\n") """


#Use the pop method to remove "model" from the car dictionary.

""" car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.keys()
print(car,"\n")

car.pop("model")

print(car,"\n") """



#APAGANDO DICIONÁRIO
#Use the clear method to empty the car dictionary.

""" car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.keys()
print(car,"\n")

car.clear()

print(car,"\n") """


""" car =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
x = car.keys()
print(car,"\n")

car.clear()

print(car,"\n") """


#Print "Hello World" if a is not equal to b.


a = 50
b = 10
if a != b :
    print("Hello World")