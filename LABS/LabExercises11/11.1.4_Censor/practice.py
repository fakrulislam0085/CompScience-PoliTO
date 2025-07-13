INPUTFILE1 = "raw_text.txt"
INPUTFILE2 = "bad_words.txt"
OUTPUTFILE = "censored2.txt" 

def readFile() : 
    badWordList = [] 
    try : 
        with open(INPUTFILE2, 'r') as in_f2 : 
            for word in in_f2 : 
                word = word.strip() 
                badWordList.append(word) 
    except FileNotFoundError : 
        print(f"Tried to open {INPUTFILE2}. File is not found.")
    

    try : 
        with open(INPUTFILE1, 'r') as in_f1, open(OUTPUTFILE, 'w') as wFile : 

                for line in in_f1: 
                    Words = line.split() 
                    
                    for word in Words : 
                        if any(word.lower() == badWord.lower() for badWord in badWordList) :
                            l = len(word) 
                            # now censor this badword 
                            wFile.write('*' * l + ' ')
                        else : 
                            wFile.write(word + ' ') 
                    wFile.write('\n') 

        print("File processed successfully") 

    except FileNotFoundError:
        print(f"Tried to open {INPUTFILE1}. File is not found.")





def main() : 
    readFile() 

if __name__ == "__main__" : 
    main() 