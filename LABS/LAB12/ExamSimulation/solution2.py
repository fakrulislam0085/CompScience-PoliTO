FILENAME1 = "customers.txt"
FILENAME2 = "suspects.txt" 

suspectList = []
customerDict = dict() 

def findTheContacts() : 
    for sName in suspectList : 
        if sName in customerDict : 
            sIn = customerDict[sName]['Check-in'] 
            sOut = customerDict[sName]['Check-out'] 
            try : 
                sIn, sOut = int(sIn), int(sOut) 
            except ValueError : 
                print("Couldn't convert the values to int")
            # print(f"{sName} : {sIn}, {sOut}")

            print(f"** Contacts of the guest: {sName} ** ")
            foundConnection = False
            collectContacts = [] 

            for cName in customerDict :     # cName is a dict inside the customersDict
                cIn = customerDict[cName]['Check-in']    # accessing the value based on assigned key 
                cOut = customerDict[cName]['Check-out']
                #print(f"{cName} : {cIn}, {cOut}")

                try : 
                    cIn , cOut = int(cIn), int(cOut) 
                except ValueError : 
                    print("Couldn't convert the values to int")

                if cName != sName :
                    if cIn in range(sIn, sOut+1) or cOut in range(sIn, sOut+1): 
                        foundConnection = True
                        collectContacts.append((cName, customerDict[cName]['Phone']))
                        # print(f"\tContact with {cName}, phone {customerDict[cName]['Phone']}")

            if foundConnection == False : 
                print(f"\tThe guest {sName} had no contacts")
            else : 
                sortedContacts = sorted(collectContacts, key=lambda x : x[1]) 
                for n, p in sortedContacts : 
                    print(f"\tContact with {n}, phone {p}")

def main() : 
    try : 
        with open(FILENAME2, 'r') as suspectF : 
            for name in suspectF : 
                suspectList.append(name.strip()) 
    except FileNotFoundError : 
        print(f"{FILENAME2}: Is not found.") 
    
    # print(suspectList)

    try : 
        with open(FILENAME1, 'r') as customersF : 
            for line in customersF : 
                line = line.strip().split(',') 

                if len(line) == 4 : 
                    name, phone, inD, outD = line 
                    customerDict[name] = {'Phone':phone, 'Check-in': inD, 'Check-out': outD}
                
                else : 
                    print("Couldn't translate the line.")
                    continue 
            # print(customerDict) 

    except FileNotFoundError : 
        print(f"{FILENAME1}: Is not found.") 
    
    findTheContacts()

if __name__ == "__main__" : 
    main() 

