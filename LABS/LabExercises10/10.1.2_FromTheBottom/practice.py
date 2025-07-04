INPUTFILENAME = "input.txt"
OUTPUTFILENAME = "output2.txt"

def readFile() : 
    try : 
        with open(INPUTFILENAME, 'r') as in_f, open(OUTPUTFILENAME, 'w') as out_f : 
            lineList = in_f.readlines() 
            reverseLine = lineList[::-1]
            for line in reverseLine : 
                out_f.write(line if line.endswith('\n') else line+'\n') 

        print("Line reversed successfully.")

    except FileNotFoundError : 
        print("Trying to open a file that does not exist!")
    except OSError : 
        print("General I/O problems(e.g., disk issues)") 
    
def main() : 
    readFile() 

if __name__ == "__main__" : 
    main() 