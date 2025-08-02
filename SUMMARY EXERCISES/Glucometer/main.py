FILENAME = "glucometer.txt" 
MAXSUGARLEVEL = 200 

def printTheResult(resultDict) :
    print(resultDict) 
    
    sorted_res = dict(sorted(resultDict.items(), key=lambda x : len(x[1]), reverse = True)) 
    
    for pID, infos in sorted_res.items() : 
        for enty in infos : 
            print(f"{pID} {enty}")

def main() : 
    try : 
        with open(FILENAME, 'r') as rF : 
            resultDict = dict() 

            for line in rF : 
                fields = line.strip().split() 

                if len(fields) == 5 : 
                    pID, time, sLevel, temp, hRate = fields 

                    try : 
                        sLevel = int(sLevel) 
                    except ValueError : 
                        print(f"{sLevel}: Couldn't convert to integer.") 
                        continue
                    
                    if sLevel >= MAXSUGARLEVEL : 
                        if pID in resultDict : 
                            resultDict[pID].append(time + " " + str(sLevel))
                        else : 
                            resultDict[pID] = [time+" "+str(sLevel)]

                else : 
                    continue 

            printTheResult(resultDict)

    except FileNotFoundError : 
        print(f"{FILENAME}: is not found!") 


if __name__ == "__main__" : 
    main() 