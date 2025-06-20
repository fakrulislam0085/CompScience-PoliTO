'''Because sets are unordered, you cannot access the elements of a
set by position as you can with a list.
▪ We use a for loop to iterate over the individual elements
▪ Note that the order in which the elements of the set are visited
depends on how they are stored internally - it's unpredicable'''

names = {"John", "Alice", "Bob", "Kibriana"}
print("The names in the set are: ", end="")
for name in names :
    print(name, end=" ")