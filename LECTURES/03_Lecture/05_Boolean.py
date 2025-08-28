#boolean not operator can inverse our output to an opposite direction
attending = True
print(not attending)        # output: False

grade = 17
if not (grade < 18):
    print("Passed")
else :
    print("Failed")


number = 200
if number > 0:
    print("True")

m = 85
if not m < 0:  #If m is not less than 0, then executes the code block
    print("True")


#Combining not with Other Logical Operators
if not attending or grade < 18 :
    print("Drop!")
if attending and not(grade < 18) :
    print("Stay!")