
FILENAME = "reports.dat" 
OUTPUT_FILENAME = "correct-reports.dat" 

def processReport(L) : 
    values = L.strip().split() 
    for i in range(len(values)) : 
        try : 
            values[i] = int(values[i]) 
        except ValueError :
            print("Error: record contains non-numerical data.")
            exit()      # or return None
    return values

def checkValidity(int_values) : 
    if len(int_values) in range(3,6) :  # 3~5
        if int_values != sorted(int_values) and int_values != sorted(int_values, reverse=True) : 
            return False 
        
        # check the difference
        for i in range(len(int_values) -1) : 
            diff = abs(int_values[i+1] - int_values[i])            
            
            if diff not in range(1, 4) : # 1~3 
                return False 

        return True

def main() : 
    count_valid = 0 
    count_total = 0 

    try : 
        with open(FILENAME, "r") as fin, open(OUTPUT_FILENAME, "w") as fout : 
            for line in fin : 
                # get the int values 
                int_values = processReport(line) 

                # check the line validity
                valid = checkValidity(int_values) 

                if valid : 
                    fout.write(f"{line}") 
                    count_valid += 1 
                count_total += 1 

            print(f"Read {count_total} reports, {100*count_valid /count_total :.2f}% are Correct.")

    except FileNotFoundError :
        print(f"Error: file {FILENAME} not found.\n")
    except OSError : 
        print(f"Error: cannot write to file {OUTPUT_FILENAME}")


if __name__ == "__main__" : 
    main() 