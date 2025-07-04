def reverseTheLinesOrder(inputFile, outputFile) : 
    try : 
        with open(inputFile, "r") as readFile, open(outputFile, "w") as writeFile : 
            lineList = readFile.readlines()     # read the whole file into a list of lines 

            # Reverse the list of lines
            lineList.reverse() 

            # Write the reversed lines to output file 
            for line in lineList :
                writeFile.write(line if line.endswith('\n') else line + '\n')

        print("File Processed successfully.\n") 

    except FileNotFoundError : 
        print("Input file or output file is not found!\n") 

def main() : 
    inputFile = "input.txt" 
    outputFile = "output.txt" 

    reverseTheLinesOrder(inputFile, outputFile)

if __name__ == "__main__" : 
    main()