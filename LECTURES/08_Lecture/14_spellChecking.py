#Function to clean a word by removing non-letters and converting it to lowercase
def clean(word):
    result = ''
    for char in word:
        if char.isalpha():
            result += char
    return result.lower()

#Function to load dictionary words into a set
def load_dictionary(file_name):
    dictionary = set()
    with open(file_name, "r") as file:
        for line in file:
            # Add cleaned word to the dictionary
            dictionary.add(clean(line.strip()))
    return dictionary

# Main function to check spelling
def main():
    # Load the dictionary of correct words
    dictionary = load_dictionary("correctSpelling.txt")
    
    # Set to store misspelled words
    misspelled_words = set()
    
    # Open the story file and check each word
    with open("story.txt", "r") as story_file:
        for line in story_file:
            # Split the line into words
            words = line.split()
            for word in words:
                # Clean the word and check if it is in the dictionary
                cleaned_word = clean(word)
                if cleaned_word and cleaned_word not in dictionary:
                    misspelled_words.add(cleaned_word)
    
    # Output the misspelled words
    if misspelled_words:
        print("Misspelled words found in the story:")
        for word in sorted(misspelled_words):
            print(word)
    else:
        print("No misspelled words found in the story.")

# Run the main function
if __name__ == "__main__":
    main()
