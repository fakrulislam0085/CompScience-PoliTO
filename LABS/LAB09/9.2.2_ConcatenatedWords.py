def main() : 
    #stop = False 
    #while not stop : 
        # match() 
        # sessions = input("Do you wanna play another session?(Y/N): ")
        # if sessions.strip().upper().startswith("N") : 
        #     stop = True 

    try: 
        sessions = int(input("How many session do you wanna play?: "))
        for i in range(sessions) : 
            print(f"Session {i+1}\n")
            match() 
        print("All sessions are Finished.\n") 

    except ValueError : 
        print("Please Enter a Valid Integer.\n") 
            
def match() : 
    wordsList = [] 
    initialWord = input("Insert the starting word: ").strip().lower() 
    wordsList.append(initialWord)
    validGame = True 

    while validGame: 
        if initialWord == "*" : 
            validGame = False     
            break

        newWord = input("Insert a word: ").strip().lower() 
        if newWord == "*":
            validGame = False     
            break
        
        if(len(newWord) < 2) :
            print("Enter a valid Word, please!")
            continue 

        lastSyllable = initialWord[-2:]
        firstSyllable = newWord[:2] 
        
        # If the word has been said already 
        if newWord in wordsList : 
            print("The Word has been pronounced already!\n") 
            validGame = False
            break

        # If syllables do not match 
        if lastSyllable != firstSyllable : 
            print("Last Player Entered a wrong word!\n")
            validGame = False 
            break

        # Update the words 
        initialWord = newWord 
        wordsList.append(newWord)

        
if __name__ == "__main__" : 
    main() 