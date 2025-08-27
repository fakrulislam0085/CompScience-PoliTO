#Serving Wine Program
order = input("Take the order: ")

if order == 'wine' or 'Wine':
    id = int(input("Ask for id: "))
    if id >= 21:
        print("Serve Wine")
    else:
        print("Read the law")
else:
    print("Serve a non-alcoholic drink")



#Federal tax program
status = input("Insert marital Status:")
income = float(input("Insert the income:"))

if status.lower() == 'single':
    if income > 32000:
        tax = 3200 + (0.025 * income)
    else:
        tax = 0.01 * income

elif status.lower() == 'married':
    if income > 64000:
        tax = 6400 + (0.025 * income)
    else:
        tax = 0.01 * income

print(f"The Calculated tax is: {tax}")

