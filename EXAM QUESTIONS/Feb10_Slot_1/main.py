def getTheAnswer(file, file2) : 
    with open(file, 'r') as f1, open(file2, 'w') as f2 : 
        totalLines = 0 
        correctLines = 0 

        for line in f1 : 
            line = line.strip() 
            totalLines += 1 

            # split the line into values 
            values = line.split() 

            #1. level's should be between 3 and 5
            if (len(values) < 3 or len(values) > 5) :
                continue
            try : 
                # convert values to int 
                int_values = [int(value) for value in values]
            except ValueError :
                print(f"Couldn't convert values in line: {line}")
                continue
    
            
            #2. All values should be strictly increasing / decreasing
            if int_values != sorted(int_values) and int_values != sorted(int_values, reverse=True) : 
                continue 

 
            #3. differences between levels should be >=1 or <=3 
            valid = True 
            for i in range(len(int_values)-1) :                 
                del_L = abs(int_values[i+1] - int_values[i])
                if del_L < 1 or del_L > 3 :
                    valid = False 
                    break

            if valid : 
                correctLines += 1 
                f2.write(f"{line}\n")

        print("File processed successfully\n") 
        print(f"Read {totalLines} reports: {(correctLines/totalLines)*100:.2f}% Correct.")

def main() : 
    file = 'reports.dat' 
    file2 = 'correct_reports.dat' 

    getTheAnswer(file, file2)

if __name__ == "__main__" : 
    main() 
