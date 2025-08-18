def main() : 
    word = input("Enter the word: ")
    n = len(word) 
    substrings_list = [] 

    for i in range(n) : 
        for j in range(i+1, n+1) :      # j goes from i+1 to n 
            substrings_list.append(word[i:j]) 
    
    substrings_list = sorted(substrings_list, key=lambda x: len(x))         # Use of sorted() and lambda function 

    print(f"Substrings of string {word} are:")
    for s in substrings_list :
        print(s)

if __name__ == "__main__" : 
    main() 