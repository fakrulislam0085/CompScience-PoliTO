def main():
    line = input("Enter your string: ")

    only_uppercase = ""
    only_even_positions = ""
    without_vowels = ""
    num_digits = 0
    vowel_positions = []        # list

    for indx, letter in enumerate(line):        # enumerate 
        if letter.isupper():
            only_uppercase += letter

        if indx % 2 == 0:
            only_even_positions += letter

        if letter.isdigit():
            num_digits += 1

        if letter.lower() in "aeiou":
            without_vowels += "_"
            vowel_positions.append(str(indx))
        else:
            without_vowels += letter

    print(f"I.   Only the uppercase letters: {only_uppercase}")
    print(f"II.  Letters in even positions: {only_even_positions}")
    print(f"III. Vowels replaced with '_': {without_vowels}")
    print(f"IV.  Number of digits in string: {num_digits}")
    print(f"V.   Positions of vowels: {', '.join(vowel_positions)}")        # .join() method

if __name__ == "__main__":
    main()
