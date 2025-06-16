#create a vegetables list
vegetables = ['Tomato', 'Potato', 'Apple', 'Carrot', 'Chilly', 'Banana']

#remove an element using pop() method 
vegetables.pop()    #pop() removes the last element
print(vegetables)
vegetables.pop(2)   #pop(indx) removes the specific element
print(vegetables)


#append the value that we have popped up now
vegetables.append('Apple')
print(vegetables)       #Check whether our appending works or not
vegetables2 = list(vegetables)  #make a copy or our vegetables list


#Create a fruit list
fruits = ['Mango', 'Banana', 'Apple', 'Cherry', 'Strawberry']       
if 'Banana' in fruits :
    fruits.remove('Mango')
print(fruits)


#if some of our vegetable is in our fruit list, then this is a fruit
for indx, element in enumerate(vegetables.copy()) :
    if element in fruits :
        vegetables.remove(element)
print(vegetables)


#list comprehension
vegetables2 = [veg for veg in vegetables2 if veg not in fruits]
print(vegetables2)