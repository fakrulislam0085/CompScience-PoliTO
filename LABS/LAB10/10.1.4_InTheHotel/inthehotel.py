def fileProcess(inputFile) : 
    try: 
        with open(inputFile, "r") as inFile : 
            linesList = inFile.readlines() 

            # Create a dictionary of `service type` : `total amount`
            result = dict() 

            for line in linesList :
                clearLine = line.strip()
                if clearLine == "":
                    continue
                fields = clearLine.split(';')

                # There are 4 fields in a single line
                if len(fields) == 4 :
                    name, service, amount, date = fields
                    try : 
                        amount = float(amount) 
                    except ValueError : 
                        print(f"Couldn't convert the amount ({amount}) to float!")
                        continue
                else : 
                    print(f"This line is not correctly formatted: {clearLine}")
                    continue 

                if service in result : 
                    result[service] += amount
                else : 
                    result[service] = amount
    
        for key, val in result.items() :  
            print(f"{key}: {val:.2f}")

    except FileNotFoundError : 
        print(f"{inputFile}: Not found\n")
    except OSError : 
        print("General I/O problems(e.g., disk issues)") 
    except Exception as e :
        print(f"An error occurred: {e}")

def main() : 
    inputFile = "hotelRecords.txt" 
    fileProcess(inputFile) 

if __name__ == "__main__" : 
    main() 