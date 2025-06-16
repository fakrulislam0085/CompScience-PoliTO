vegetables = ['Tomato', 'Potato', 'Carrot', 'Chilly']

#finding an element using in operator
veg = input("Write the name: ")
if veg in vegetables :
    print("This is a vegetable")
else :
    print("This is not a vegetable")



#finding the index of an element using index() method
n = vegetables.index("Tomato") 
print("Index of Tomato is:", n)

'''If Tomato is not present in our list, a value error occurs when we try to find the
index of Tomato. So it is better to be sure whether Tomato is present or not
in our list using 'in' operator before trying to find out the index.
Or we can use try-except block. '''