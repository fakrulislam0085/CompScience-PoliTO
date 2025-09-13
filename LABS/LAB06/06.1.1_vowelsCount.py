def count_vowels(string) : 
    cnt = 0
    for i in range(len(string)) : 
        if string[i].lower() in "aeiou" : 
            cnt +=1 
    return cnt 


def main() : 
    string = input("Write the string: ") 
    print(f"The string contains {count_vowels(string)} vowels")


if __name__ == "__main__" : 
    main() 