def main() : 
    fileNames = list(map(str, input("Enter the file names: ").split(',')))
    searchWord = input("Enter the word to search: ") 
    searchTheWord(fileNames, searchWord) 

def searchTheWord(fileNames, sWord) : 
    for file in fileNames : 
        print()     # Print a newline before processing each file
        try : 
            with open(file, "r") as readFile: 
                linesList = readFile.readlines()    # read the whole file into a list of lines 

                for line in linesList : 
                    if sWord.lower() in line.lower() :  # found the word
                        print(f"{file}: {line.strip()}")
                #print()     # print a newline after processing each file

        except FileNotFoundError : 
            print(f"{file}: Not found\n")

if __name__ == "__main__" : 
    main() 