'''The issubset() method returns True or False to report
whether one set is a subset of another set.'''

canadianFlag = {'Red', 'White'}
italianFlag = {'Green', 'White', 'Red'}
britishFlag = {'Blue', 'White', 'Red'}

# True
if canadianFlag.issubset(italianFlag): 
    print('Canadian flag colors is a subset of Italian flag colors')

# False
if italianFlag.issubset(britishFlag): 
    print('Italian flag colors is a subset of British flag colors')
else :
    print("Italian flog colors is not a subset of British flag colors")

# True
if not italianFlag.issubset(britishFlag) :
    print("At least one of the colors in the Italian flag does not.")