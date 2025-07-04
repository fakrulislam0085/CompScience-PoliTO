def fileProcess(inputFile) : 

    try: 
        with open(inputFile, "r") as inFile : 
            linesList = inFile.readlines() 

            # Crate a dictionary of "service type" : "total amount" 
            result = dict() 

            for line in linesList :
                clearLine = line.strip()
                fields = clearLine.split(';')

                # There are 4 fields in a single line 
                name, service, amount, date = fields
                if service in result : 
                    result[service] += float(amount)
                else : 
                    result[service] = float(amount) 
        
        for key, val in result.items() :  
            print(f"{key}: {val}")

    except FileNotFoundError : 
        print(f"{inputFile}: Not found\n")


def main() : 
    inputFile = "hotelRecords.txt" 
    fileProcess(inputFile) 

if __name__ == "__main__" : 
    main() 