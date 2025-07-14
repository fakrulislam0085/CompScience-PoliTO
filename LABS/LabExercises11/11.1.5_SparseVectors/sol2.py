
def another_vector(a, b) : 
    c = dict()
    
    for i, val in a.items() : 
        c[i] = val 

    for i, val in b.items() : 
        if i in c : 
            c[i] += b[i]
        else :
            c[i] = val 
    
    return c 

def main() : 
    # key: value = position: number 
    a = {5: 4, 9: 2, 10: 9}
    b = {5: 4, 8: 4, 10: 4}

    sum_vector = another_vector(a, b) 

    print(sum_vector)

if __name__ == "__main__" : 
    main() 