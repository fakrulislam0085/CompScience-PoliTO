def count_words(readFile) : 
    result = dict() 

    try : 
        with open(readFile, "r") as inFile : 
            text = inFile.read() 

            # Normalize text 
            words = text.lower().split() 

            for word in words : 
                # strip punctuation from each word 
                word = ''.join(char for char in word if char.isalnum())

                if word :   # The word is not empty 
                    if word in result :
                        result[word] += 1
                    else : 
                        result[word] = 1 
    except FileNotFoundError : 
        print(f"File {readFile} not found.") 
    
    return result

def main() : 
    fileName = "input.txt" 
    wordCounts = count_words(fileName) 

    for word, count in wordCounts.items() : 
        print(f"{word:<10}=>{  count}")

if __name__ == "__main__" : 
    main() 