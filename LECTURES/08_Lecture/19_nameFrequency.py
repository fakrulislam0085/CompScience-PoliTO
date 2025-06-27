def process(read_file, name_dict) :
    for line in read_file :
        name = line.strip()
        if name in name_dict :
            name_dict[name] += 1 
        else :
            name_dict[name] = 1
    
    print("Name frequency: ")
    for key, value in name_dict.items() :
        print(key, value)
    
def main() :
    read_file = open("names.txt", "r") 
    name_dict = {}

    try :
        process(read_file, name_dict)        
    except :
        print("Error in reading file")

main() 