#step 4: clean the words 
#Create a function to clean a word by removing non-letters and converting it to lowercase
def clean(word) :
    #create an empty string to store the cleaner word
    result = ""

    for char in word :
        if char.isalpha() : 
            result += char 
    return result.lower() 


def main() :
    #Step One: Understand the Task
    #The task is to count the number of unique words in a text document.
    #We'll use a set to store unique words, as sets automatically discard duplicates.

    #step 2: Decompose the problem
    #create an empty Set() to store the unique words 
    unique_words = set()  

    #step 3: build the set 
    #open the txt file and read it line by line 
    '''input_files = open('nurseryrhyme.txt', 'r')
        for line in input_files :
            theWords = line.split()'''   #alternate way to open the .txt file
    with open("nurseryrhyme.txt", "r") as inputFile :
        for line in inputFile :
            words = line.split()    #here words is a list who contains all words of a sentence as element
            for word in words : 
                cleaned_word = clean(word)
                if cleaned_word :
                    unique_words.add(cleaned_word)
    
    print(f"Number of unique words: {len(unique_words)}")



#Step Five: Put Everything Together
#Call the main() function
main()