INPUTFILENAME = "hotelRecords.txt" 

def readFile() : 
    
        try : 
            with open(INPUTFILENAME, 'r') as in_f : 
                hotelRecord = dict() 

                for line in in_f : 
                    line = line.strip().split(";")

                    if len(line) == 4 : 
                        name, service, amount, date = line 
                        try : 
                            amount = float(amount) 
                        except ValueError : 
                            print(f"Couldn't conver the amount({amount}) to float!")

                    else : 
                        print(f"This line is not correctly formatted: {line}")
                        continue 
                     
                    if service in hotelRecord : 
                        hotelRecord[service] += amount 
                    else : 
                        hotelRecord[service] = amount 
                
                for key, value in hotelRecord.items() : 
                    print(f"{key} {value}")


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