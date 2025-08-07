def merge(a, b) :
    lenA = len(a) 
    lenB = len(b) 
    finalList = []

    if lenA >= lenB : 
        for i in range(lenA) :
            if i < lenB :
                finalList.append(a[i])
                finalList.append(b[i])
            else :
                finalList.append(a[i])

    else :
        for i in range(lenB) :
            if i < lenA :
                finalList.append(a[i])
                finalList.append(b[i])

            else: 
                finalList.append(b[i])

    return ' '.join(map(str, finalList))

def main():
    a = list(map(int, input("Enter list a: ").split()))
    b = list(map(int, input("Enter list b: ").split()))

    newList = merge(a, b) 
    print(f"Our merged list is: {newList}")

if __name__ == "__main__" : 
    main() 