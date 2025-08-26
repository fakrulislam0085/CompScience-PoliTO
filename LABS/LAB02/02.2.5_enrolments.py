def extract_number_part(ID) : 
    return int(ID[1:])  # skip the first character and convert the rest to int

def main() : 
    student_id1 = input("Enter the student ID(matricola): ")        # s339696
    student_id2 = input("Enter the student ID(matricola): ")        # s339494

    if (extract_number_part(student_id1) > extract_number_part(student_id2)) : 
        print(student_id2)
        print(student_id1)
    else : 
        print(f"{student_id1}\n{student_id2}")
    

if __name__ == "__main__" : 
    main() 