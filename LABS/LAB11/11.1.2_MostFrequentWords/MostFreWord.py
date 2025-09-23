def mostFreqWords(fileName) : 
    """Count occurrences of each word in the given file.
    Reads `fileName`, splits on whitespace, lowercases words,
    and returns a dictionary mapping each word to its count.
    """
    resultDic = dict()     

    try: 
        with open(fileName, "r") as inFile : 
            words = inFile.read().strip()
            words = words.split()

            for singleWord in words : 
                singleWord = singleWord.lower()

                if singleWord in resultDic : 
                    resultDic[singleWord] += 1 
                else : 
                    resultDic[singleWord] = 1 
    except FileNotFoundError : 
        print(f"{fileName}: Not found\n") 
    
    return resultDic 

def main() : 
    fileName = "input.txt" 
    wordDict = mostFreqWords(fileName) 

    # Sorted the dictionary based on it's value 
    # wordDict = dict(sorted(wordDict.items(), key=lambda x: x[1], reverse=True))
    wordDict = sorted(wordDict.items(), key=lambda x : x[1], reverse=True)  # now wordDict is a list of tuples(word, count)

    # Get the first 5 key-value pairs 
    topFiveWords = wordDict[:5]

    # Display the result
    for word, count in topFiveWords : 
        print(f"{word:<15}{count}")

if __name__ == "__main__" : 
    main() 