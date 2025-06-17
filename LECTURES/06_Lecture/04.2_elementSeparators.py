#element Separator using loop
flowers = ['Rose', 'Belly', 'MarryGold', 'White Rose']
result = ''

for i in range(len(flowers)) :
    if i>0 :
        result += ", "
    result = result + flowers[i]
print(result)


#The .join() method
'''The .join method of strings automatically joins the elements of a
list, using the string as a separator separator_string.join(list)'''
result2 = ', '.join(flowers)
print(result2)

result3 = '\n'.join(flowers)
print(result3)

result4 = '.!\n'.join(flowers)
print(result4)


#split shortcut
line = "Marry had a little lamb"
wordlist = line.split()
print(wordlist)