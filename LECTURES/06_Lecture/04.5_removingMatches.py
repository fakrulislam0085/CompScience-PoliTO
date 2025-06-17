#removing elemenets that matches a particular condition from a list
#exercises 2 
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
i = 0
while i < len(words):
    word = words[i]
    if len(word) < 6 :
        words.pop(i)    #delete i th element
    else :
        i += 1
print(words)


#remove all elements 2 from a list
ListNum = [2,3,2,4,2,2,5,2,2,5,6,4]
i = 0
while i < len(ListNum) :
    two = ListNum[i]
    if two == 2 :
        ListNum.pop(i)
    else :
        i += 1
print(ListNum)


#however it is wrong to remove elements from a list while iterating over it
for w in words:
    if len(w) < 7:
        words.remove(w)
print(words)