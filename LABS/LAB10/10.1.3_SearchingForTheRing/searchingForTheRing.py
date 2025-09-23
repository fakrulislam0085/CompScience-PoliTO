def main() : 
    fileNames = list(map(str, input("Enter the file names: ").split(',')))
    searchWord = input("Enter the word to search: ") 
    searchTheWord(fileNames, searchWord) 

def searchTheWord(fileNames, sWord) : 
    for file in fileNames : 
        print()     # Print a newline before processing each file
        try : 
            with open(file, "r") as readFile: 
                linesList = readFile.readlines()    # Read the whole file into a list of lines 

                for line in linesList : 
                    if sWord.lower() in line.lower() :  # Found the word
                        print(f"{file}: {line.strip()}")
                print()     # Print a newline after processing each file

        except FileNotFoundError : 
            print(f"{file}: Not found\n")
        except OSError : 
            print("General I/O problems(e.g., disk issues)") 
        except Exception as e :
            print(f"An error occurred: {e}")
            
if __name__ == "__main__" : 
    main() 