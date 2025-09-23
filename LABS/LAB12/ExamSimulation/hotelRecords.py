def process(file1, file2, file3) : 
    try : 
        with open(file1, "r") as customersFile, open(file2, "r") as suspectsFile, open(file3, "w") as writeFile : 
            # Read the suspects name 
            suspectsList = suspectsFile.readlines() 
            for Sname in suspectsList : 
                Sname = Sname.strip()

                # Reset the file pointer to the beginning of customersFile
                customersFile.seek(0)

                # Read the customers file 
                customersList = customersFile.readlines()

                # Find out the suspects in and out day
                for line in customersList : 
                    line = line.strip()
                    fields = line.split(',') 
                    
                    name, number, checkIn, checkOut = fields 

                    if Sname == name : 
                        try: 
                            SuspectsInD = int(checkIn)
                            suspectsOutD = int(checkOut)
                        except ValueError : 
                            print("Something wrong with the value.")
                            return 
                        
                # now compare with the file 
                writeFile.write(f"** Contacts of the guest: {Sname}: **\n")
                print(f"** Contacts of the guest: {Sname}: **")
                contacts = []   # Collect contacts in a list
                for line in customersList : 
                    line = line.strip()
                    fields = line.split(',') 
                    
                    name, number, checkIn, checkOut = fields 

                    try : 
                        checkIn = int(checkIn) 
                        checkOut = int(checkOut)

                    except ValueError : 
                        print("Something wrong with the value.")
                        return 
                    
                    if Sname != name :
                        if SuspectsInD in range(checkIn, checkOut+1) or suspectsOutD in range(checkIn, checkOut+1):
                            contacts.append((name, number))                      

                if contacts :
                    contacts.sort(key=lambda x : x[0])
                    for contact in contacts : 
                        print(f"\tContact with {contact[0]}, phone {contact[1]}")
                        writeFile.write(f"\tContact with {contact[0]}, phone {contact[1]}\n")
                else : 
                    print(f"\tThe guest {Sname} had no contacts")
                    writeFile.write(f"\tThe guest {Sname} had no contacts\n")


    except FileNotFoundError as e:
        print(f"{e.filename}: Not found.")
      

def main() : 
    file1 = "customers.txt" 
    file2 = "suspects.txt" 
    file3 = "outcome.txt" 

    process(file1, file2, file3) 

if __name__ == "__main__" : 
    main() 