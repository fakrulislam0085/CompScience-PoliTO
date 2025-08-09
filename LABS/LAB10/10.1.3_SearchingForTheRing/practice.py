def readFile() : 
    fileNameList = list(map(str, input("Enter the file names: ").split(',')))
    wordToSearch = input("Enter the word: ")

    for file in fileNameList : 
        try : 
            print() 
            with open(file, 'r') as f : 
                for line in f : 
                    if wordToSearch.lower() in line.lower() : 
                        print(f"{file}: {line.strip()}")
            # print() 

        except FileNotFoundError : 
            print("Trying to open a file that does not exist!")
        except OSError : 
            print("General I/O problems(e.g., disk issues)") 
        except Exception as e :
            print(f"An error occurred: {e}")
    
def main() : 
    readFile() 

if __name__ == "__main__" : 
    main() 