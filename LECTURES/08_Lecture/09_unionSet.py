#Note that, the union() method returns a new set. It does not modify either of the sets in the call.
#The union of two sets contains all of the elements from both sets, with duplicates removed   

australianAnimals = {"Kangaroo", "Koala", "Wallaby", "Wombat"}
italianAnimals = {"Kangaroo", "Koala", "Wallaby", "Wombat", "Wolf", "Bear", "Fox"}

# Union of two sets
allAnimals = australianAnimals.union(italianAnimals)
print(allAnimals)

