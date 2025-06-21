'''Sets are mutable collections, so you can add elements by using the
add() method'''

cast = set(['Arthur', 'Shelbi', 'John', 'Thomas'])
cast.add('Michael')
cast.add('Ada')
cast.add('Thomas')  # Thomas is already in the set, set doesn't allow duplicates

print(cast) 