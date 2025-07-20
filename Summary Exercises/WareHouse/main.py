# using camelCase 

MOVEMENTSFILENAME = "movements.txt" 
WAREHOUSEFILENAME = "warehouse.txt" 
OUTPUTFILENAME = "warehouse2.txt"

def saveWareHouseToFile(wareH) : 
    try : 
        with open(OUTPUTFILENAME, 'w') as fw : 
            for pCode, details in wareH.items() : 
                fw.write(f"{pCode},{details['unitCost']}, {details['qAvailable']}\n")
    except IOError : 
        print(f"Error writing to {OUTPUTFILENAME}")
        
def writeOutput(wareH, productCode, variation, totalValue) : 
    # condition 1- it must indicate if the product is not present in the database
    if productCode not in wareH : 
        print(f"Error: product {productCode} not existent.")
        return totalValue 
    
    newTotalVal = totalValue

    if variation >= 0:     # increasing 
        if wareH[productCode]['qAvailable']+variation <= 10000:
            print(f"Increasing the quantity of {productCode} by {variation}")
            print(f"Previous total value: {totalValue:.2f}$")
            newTotalVal += wareH[productCode]['unitCost'] * variation 
            print(f"New total value: {newTotalVal:.2f}$") 
            print()
        else : 
            print(f"ERROR: Product quantity must be lower than 10,000.")
            print()
            return totalValue 
        
    else :  # decreasing 
        if wareH[productCode]['qAvailable'] >= abs(variation) :
            print(f"Decreasing the quantity of {productCode} by {abs(variation)}")
            print(f"Previous total value: {newTotalVal:.2f}$")
            wareH[productCode]['qAvailable'] += variation   # minus hocce cause variation negative
            newTotalVal += wareH[productCode]['unitCost'] * variation 
            print(f"New total value: {newTotalVal:.2f}$") 
            print()
        else : 
            print(f"ERROR: Required quantity of {productCode} not available!")
            print()
            return totalValue
        
    return newTotalVal


def wareHouse() : 
    try : 
        with open(WAREHOUSEFILENAME, 'r') as readFile : 
            totalValue = 0.0 
            wareH = dict()

            for line in readFile : 
                line = line.strip().split(',') 

                if len(line) == 3 : 
                    pCode, unitCost, qAvailable = line 

                    try : 
                        unitCost, qAvailable = float(unitCost), int(qAvailable)
                        totalValue += unitCost * qAvailable
                    except  ValueError : 
                        print(f"Coulnd't conver {unitCost} and {qAvailable} to integer.")
                        continue 

                    wareH[pCode] = {'unitCost': unitCost, 'qAvailable': qAvailable}
            
                else : 
                    print("Not enough data to extract")
                    continue
            # Call our write output function
            # writeOutput(wareH, productCode, variation, totalValue)
            return wareH, totalValue

    except FileNotFoundError : 
        print(f"{MOVEMENTSFILENAME}: is not found!") 
        return None, 0
    except OSError : 
        print("General input/output Error.") 
        return None, 0
    except Exception as e : 
        print(f"Some other error occurred: {e}") 
        return None, 0


def movements(wareH, totalValue) : 
    if wareH is None : 
        return 
    
    try : 
        with open(MOVEMENTSFILENAME, 'r') as readFile : 
            for line in readFile : 
                line = line.strip().split(',') 

                if len(line) == 2 : 
                    productCode, variation = line 

                    try : 
                        variation = int(variation) 
                    except ValueError : 
                        print(f"Coulnd't convert {variation} to integer.")
                        continue
                else : 
                    print("Not enough data to extract")
                    continue

                # Call the next function
                totalValue = writeOutput(wareH, productCode, variation, totalValue)
        
        # save final warehouse state after all movements
        saveWareHouseToFile(wareH)

    except FileNotFoundError : 
        print(f"{MOVEMENTSFILENAME}: is not found!") 
    except OSError : 
        print("General input/output Error.") 
    except Exception as e : 
        print(f"Some other error occurred: {e}") 

def main() : 
    wareH, totalValue = wareHouse()
    movements(wareH, totalValue) 

if __name__ == "__main__" : 
    main() 