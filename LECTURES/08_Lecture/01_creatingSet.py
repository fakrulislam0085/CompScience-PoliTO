#manually creating set
country = {"Italy", "UK", "Germany", "France"}
print(country)


#converting list, tuple or string to set
names = ["John", "Alice", "Bob", "Alice"]   #list with duplicate
unique_names = set(names)
print(unique_names)

numbers = [1, 2, 3, 4, 1, 2, 3]   #list with duplicate
unique_numbers = set(numbers)
print(unique_numbers)


string = "Hello" #string
unique_char = set(string) 
print(unique_char)


flowers = ("Tulip", "Daisy", "Rose") #tuple
unique_flower = set(flowers)
print(unique_flower)


#Creating an empty set
animals = set() 
print(animals)

numberOfAnimals = len(animals)
print("Number of animals:", numberOfAnimals)
