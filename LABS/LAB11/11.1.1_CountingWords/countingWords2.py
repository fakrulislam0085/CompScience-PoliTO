# Solution 2
FILENAME = "input.txt" 

def count_words() : 
    try : 
        with open(FILENAME, "r") as inFile :
            result = dict()  
            for line in inFile : 
                words = line.strip().split() 

                for word in words : 
                    if word in result : 
                        result[word] += 1 
                    else : 
                        result[word] = 1 

    except FileNotFoundError : 
        print(f"File {FILENAME} not found.") 
    
    # sort the dictionary based on count value, dict() does not have any sort() method in python
    # after sorting a dictionary it transforms into a list
    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

    for word, count in sorted_result : 
        print(f"{word:10} => {count}")

def main() : 
    count_words() 
    
if __name__ == "__main__" : 
    main() 