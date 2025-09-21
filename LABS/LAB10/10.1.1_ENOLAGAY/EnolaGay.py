def main() : 
    readFile = "input.txt" 
    writeFile = "output.txt" 

    try: 
        # Open the input file for r and output file for w 
        with open(readFile, "r") as inFile, open(writeFile, "w") as outFile : 
            # Read the lines 
            lines = inFile.readlines() 

            # Process each line with line number 
            for Ln, line in enumerate(lines, 1) : 
                # Remove trailing whitespace/newline char
                clearLine = line.rstrip()
                
                # Format the line
                formattedline = f"/*{Ln}*/{clearLine}\n"

                # Write the line 
                outFile.write(formattedline)
        
        print("Successfully formatted the input file.\n") 

    except FileNotFoundError :
        print("Input or output file is not found!") 

if __name__ == "__main__" : 
    main() 

