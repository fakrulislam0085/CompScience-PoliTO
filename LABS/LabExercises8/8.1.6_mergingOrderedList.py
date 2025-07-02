def merge_sorted(a, b) : 
    newList = [] 
    curr_indxA = 0      # current index of a
    curr_indxB = 0      # current index of b 

    while curr_indxA < len(a) or curr_indxB < len(b) : 
        # If there are elements in both lists then take an element from the list that starts with the smaller element
        if curr_indxA < len(a) and curr_indxB < len(b) : 
            if a[curr_indxA] < b[curr_indxB] : 
                newList.append(a[curr_indxA])
                curr_indxA += 1 
            else : 
                newList.append(b[curr_indxB]) 
                curr_indxB += 1 

        # If only list 'a' has element then process it's first element 
        elif curr_indxA < len(a) : 
            newList.append(a[curr_indxA])
            curr_indxA += 1 

        # If only list 'b' has element then process its first element 
        else : 
            newList.append(b[curr_indxB]) 
            curr_indxB += 1 

    return ' '.join(map(str, newList))

def main() :
    a = list(map(int, input("Enter list a: ").split()))
    b = list(map(int, input("Enter list b: ").split()))

    resultList = merge_sorted(a, b) 
    print(f"The merged sorted list: {resultList}")


if __name__ == "__main__" : 
    main() 