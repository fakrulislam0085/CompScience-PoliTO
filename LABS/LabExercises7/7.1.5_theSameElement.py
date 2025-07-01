def same_set(a, b) :
    a_set = set(a) 
    b_set = set(b) 

    return a_set == b_set 
    
def main() :
    a = list(map(int, input("List A: ").split()))
    b = list(map(int, input("List B: ").split()))

    ans = same_set(a, b) 

    if ans : 
        print("True🤞 : Both lists are same.")
    else :
        print("False: Both lists are not same.")

if __name__ == "__main__" : 
    main()