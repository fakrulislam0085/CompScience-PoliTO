#we can iterate over the individual keys in a dictionary using a for loop 
favourite_flowers = {"Alice": "rose", "Bob": 'Lily', "Charlie": 'Sunflower', 'David': "Tulip", "Ayush": "Lily", "Boby": 'Sunflower'}
print(favourite_flowers)
print(f"\nPeople: ")
for key in favourite_flowers :
    print(key)

#we can iterate over the individual values in a dictionary using a for loop
print(f"\nFavourite flowers: ")
for flower in favourite_flowers.values():
    print(flower)

#we can iterate over the key-value pairs in a dictionary using a for loop
print(f"\nPeople and their favourite flowers:")
for key in favourite_flowers :
    print(key + ' : ' + favourite_flowers[key])

#we can iterate over the key-value pairs in a dictionary using the items() method
print(f"\nPeople and their favourite flowers(using items() method):")
for key, value in favourite_flowers.items():    #items() method returns a sequence of tuples
    print(key + ' : ' + value)



#We can also have sorted order keys in the dictionary
print(f"\nPeople and their favourite flowers in sorted order:")
for key in sorted(favourite_flowers) :      #sorted() function returns a sorted list of keys
    print(key + ' : ' + favourite_flowers[key])

#We can also have sorted order values in the dictionary
print(f"\nPeople and their favourite flowers in sorted order of flowers:")
for value in sorted(favourite_flowers.values()) :      #sorted() function returns a sorted list of values
    print(value)


#We can also have sorted order key-value pairs in the dictionary    
print(f"\nPeople and their favourite flowers in sorted order of people:")
for key, value in sorted(favourite_flowers.items()) :      #sorted() function returns a sorted list of key-value pairs
    print(key + ' : ' + value)



#we can have the maximum value in the dictionary
number_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
mx_value = max(number_dict.values())
print(f"\nMaximum value in the dictionary is: {mx_value}")
