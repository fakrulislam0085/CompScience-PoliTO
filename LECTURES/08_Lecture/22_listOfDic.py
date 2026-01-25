def extract_CSV_file(f):
    # Initialize an empty list to hold the dictionaries (records)
    records = []
    
    # Read the first line to get the attribute names
    header = f.readline().strip()  # Read and strip any leading/trailing whitespace
    attributes = header.split(",")  # Split the header line by commas to get the column names
    
    # Read through the file line by line
    for line in f:
        line = line.strip()  # Remove leading/trailing whitespace
        fields = line.split(",")  # Split the line by commas to get individual fields
        
        # Check if the line has the same number of fields as the number of attributes
        if len(fields) != len(attributes):
            raise ValueError(f"Line has a different number of fields than expected: {line}")
        
        # Create a dictionary for the current record
        record = {}
        for i in range(len(attributes)):
            record[attributes[i]] = fields[i]  # Map attributes to fields
        
        # Append the record to the list
        records.append(record)
    
    return records

def main():
    file_name = 'CSV.txt'  # Name of the input file

    try:
        with open(file_name, 'r') as f:
            records = extract_CSV_file(f)
            
            # Print all records
            for record in records:
                print(record)
    
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except ValueError as e:
        print(f"Invalid input. Error: {e}")
    except Exception as explanation:
        print(f"An unexpected error occurred: {explanation}")

main()
