def count_words(string) : 
    word_cnt = 0  
    
    # Removing leading/trailing spaces to make counting easier and then split it in a list of words based on spaces
    string = string.strip() 
    word_list = string.split()   #.split() automatically handles any amount of whitespaces- single, multiple, tabs, even newlilnes. 
    return len(word_list)

    # another way of doing it: string.count(' ') + 1   #To count the first word we will add 1

def main() : 
    user_string = input("Write the string: ") 
    print(f"There are total {count_words(user_string)} words in the given string.")

if __name__ == "__main__" : 
    main() 

