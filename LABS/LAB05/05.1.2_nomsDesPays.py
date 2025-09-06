def main() :
    country_name = input("Enter the country name: ")
    
    while True : 
        if country_name.isalpha() and country_name[0].isupper() :
            break 
        else : 
            if not country_name.isalpha() : 
                print("Country name should contain only letters.")

            if country_name[0].islower() : 
                print("Country name starts with a capital letter.\n")
            
            country_name = input("Enter the country name: ")


    exception_musculine_singular = ['Belize', 'Cambodge', 'Mexique', 'Mozambique', 'Zaire', 'Zimbabwe']
    plural_exceptions = ['Etats-Unis', 'Pays-Bas'] 

    # 'l' if nouns starts with a vowel (aeiou)
    if country_name[0] in 'AEIOU' : 
        print(f"l'{country_name}")

    # 'le' for masculine nouns [nouns end with 'a']
    elif country_name in exception_musculine_singular or country_name[-1] == 'a' :    # way-1 to access last char
        print(f"le {country_name}")
    elif country_name in plural_exceptions :
        print(f"les {country_name}")

    # 'la' for feminine nouns [nouns end with 'e']
    elif country_name[len(country_name)-1] == 'e' :         # way-2 to access last char
        print(f"la {country_name}")


if __name__ == "__main__" : 
    main() 
