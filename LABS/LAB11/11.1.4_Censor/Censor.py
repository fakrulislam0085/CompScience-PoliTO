import re 

def censored_text(fileName1, badWords, fileName3) : 
    try : 
        with open(fileName1, "r") as inFile, open(fileName3, "w") as writeFile : 
            readBlocks = inFile.read() 
            tokens = re.findall(r'\w+|\W+', readBlocks) 

            for word in tokens : 
                if word.strip().isalnum() and word.lower() in badWords : 
                    writeFile.write(len(word) * '*')
                else : 
                    writeFile.write(word)
            print("File Processed Successfully!\n") 

    except FileNotFoundError : 
        print(f"{fileName1} or {fileName3}: Not found.\n") 
    

def main() : 
    fileName1 = "raw_text.txt" 
    fileName2 = "bad_words.txt" 
    fileName3 = "censored.txt"

    # Extract the bad words in a set 
    try : 
        with open(fileName2, "r") as readFile : 
            badWords = readFile.read().split()
            badWords = set(word.lower() for word in badWords) 

    except FileNotFoundError : 
        print(f"{fileName2}: Not found.\n") 

    censored_text(fileName1, badWords, fileName3) 

if __name__ == "__main__": 
    main() 