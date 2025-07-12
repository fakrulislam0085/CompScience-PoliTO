def main() : 
    print("User Input:\n") 
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ") 

    # Transform a string into a set of char
    s1 = set(string1) 
    s2 = set(string2)

    
    #1. The char that appear in both string
    common_chars = s1 & s2 
    print("\nCharacters that appear in both strings:", common_chars)

    #2. char that appear in one string but not in the other 
    unique_chars = s1 ^ s2 
    print("Characters that appear in one string but not in the other",unique_chars)

    #3. the (alphabetical) letters that do not appear in either string 
    alphabet = set("abcdefghijklmnopqrstuvwxyz") 
    missing_chars = alphabet - (s1 | s2) 
    print("Alphabetical letters that do not appear in either string:", missing_chars)

if __name__ == "__main__" : 
    main() 