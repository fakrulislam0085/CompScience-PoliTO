def make_the_dict(readFiles):
    record = {}
    line = readFiles.readline()  # Read a single line

    if line.strip():  # Check if the line is not empty after stripping
        words = line.strip().split(":")  # Split the line into country and population
        record["country"] = words[0]
        record["population"] = int(words[1])  # Convert population to an integer

    return record


def main():
    try:
        # Open the file in read mode
        with open("countries.txt", "r") as readFiles:
            while True:
                CountryDic = make_the_dict(readFiles)  # Read one record
                if not CountryDic:  # If no more records, break the loop
                    break
                print(CountryDic)  # Print the dictionary
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: File contains invalid data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


#storing all records in a list
''' records = []
    with open("countries.txt", "r") as infile:
        while True:
            record = make_the_dict(infile)
            if not record:
                break
            records.append(record)
    print(records) '''


# Call the main function
main()
