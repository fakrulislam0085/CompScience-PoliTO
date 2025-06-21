'''The discard() method removes an element if the element exists. 
▪ It has no effect if the given element is not a member of the set.'''

#discard() method : removes an element from the set if it is a member.
artists = {"Leonardo", "Vincent", "MichaelAngelo", "Picaso"}
artists.discard("Leonardo")
artists.discard("Vinchi")   # Vinchi is not in the set, so no effect
print(artists)  # {'MichaelAngelo', 'Vincent', 'Picaso'}



#remove() method : removes an element from the set if it is a member, otherwise raises a KeyError.
colors = {"Red", "Green", "Blue", "Yellow"}
colors.remove("Green") 
#colors.remove("Black")  #Black is not in the set, so it will raise a KeyError
print(colors)   # {'Red', 'Blue', 'Yellow'}


#clear() method : removes all elements from the set
countries = {'Bangladesh', 'Pakistan', 'Italy', 'France'}
countries.clear()
print(countries)  # set()


#pop() method: removes and returns an arbitrary element from the set
# If the set is empty, raises KeyError
foods = {'Pizza', 'Burger', 'Pasta', 'Sandwich'}
print(foods.pop()) # Pizza or Burger or Pasta or Sandwich
