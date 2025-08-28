#This program takes input of richter scale's point and give us an output based on the point
richter = int(input("Give us the richter scale point: "))

#Note: here the order is important
if richter >= 8:
    print("Most structures fall")
elif richter >= 7:
    print("Many buildings destroyed")
elif richter >= 6:
    print("Many buildings damaged, some collapse")
elif richter >= 4.5 :
    print("Damage to poorly constructed buildings")
else :      #so that the ‘general case’ can be handled last
    print("No destruction of buildings")


#Remembering the conditon
age = int(input("Insert the age: "))
canDrink = age > 18 and age < 30

if canDrink:        #or we can write, if canDrink == true:
    print("You can drink wine, bear, champagne whatever you want")
else:
    print("You can not drink as you are a minor!")