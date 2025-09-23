# Read the file containing motorways sections and corresponding tolls
def readTolls(filename):
    sections = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            fields = line.split(";")
            try:
                toll = float(fields[2])
            except ValueError:
                # if the toll is not formatted correctly, we assume that 
                # section of the motorway is free
                toll = 0.0
            record = {'start': fields[0], 'end': fields[1], 'toll': toll}

            # check that every section is connected to the previous one
            if len(sections) >= 1 and sections[-1]['end'] != record['start']:
                raise ValueError("Uncorrectly formatted section")

            sections.append(record)
        return sections


# process a single entrance of a car in the motorway.
# start: starting point of the trip
# end: ending point of the trip
# sections: list of dictionaries containing the tolls for each motorway section
def processEntrance(start, end, sections):
    total_toll = 0.0
    number_of_sections = 0
    start_line = 0

    # look for the starting point of the trip in the sections list
    while start_line < len(sections) and sections[start_line]['start'] != start:
        start_line = start_line + 1
    
    # we didn't find the starting point
    if start_line == len(sections):
        # this special return value is used to signal that we didn't find the
        # requested "trip"
        return -1, -1
    
    # look for the ending point of the trip in the sections list, while
    # computing the total toll and number of sections
    end_line = start_line
    flag = True
    while end_line < len(sections) and flag:
        # accumulate total toll and number of sections
        total_toll = total_toll + sections[end_line]['toll']
        number_of_sections = number_of_sections + 1
        # exit when you find the ending point
        if sections[end_line]['end'] == end:
            flag = False
        else:
            end_line = end_line + 1

    # we didn't find the ending point
    if end_line == len(sections):
        return -1, -1
    
    # we reach here if we found the trip
    return total_toll, number_of_sections


# process the cars file.
# filename: name of the file containing the cars entrances
# sections_tomi: list of dictionaries containing the start, end and toll of each
# section in the TURIN to MILAN direction
# sections_mito: list of dictionaries containing the start, end and toll of each
# section in the MILAN to TURIN direction
def processCars(filename, sections_tomi, sections_mito):
    cars = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            fields = line.split(";")
            plate = fields[0]
            start = fields[1]
            end = fields[2]
            # tey to find the trip in the TURIN --> MILAN direction
            total_toll, number_of_sections = processEntrance(start,
                                                             end,
                                                             sections_tomi)
            # if we didn't find the trip, try to find it in the MILAN --> TURIN
            # direction
            if total_toll == -1:
                total_toll, number_of_sections = processEntrance(start,
                                                                 end,
                                                                 sections_mito)

            # if we found the trip, update the cars dictionary
            if total_toll != -1:
                # if the car is already in the dictionary, update the values
                if plate in cars:
                    cars[plate]['total_toll'] += total_toll
                    cars[plate]['number_of_sections'] += number_of_sections
                    cars[plate]['number_of_entrances'] += 1
                # if the car is not in the dictionary, add it
                else:
                    new_dict = {'total_toll': total_toll,
                                'number_of_sections': number_of_sections,
                                'number_of_entrances': 1
                                }
                    cars[plate] = new_dict
            else:
                print(f"I couldn't find a trip from {start} to {end}")
    return cars


# print the output in the format requested by the exercise
def printOutput(cars):
    for plate in cars:
        tt = cars[plate]['total_toll']
        ns = cars[plate]['number_of_sections']
        ne = cars[plate]['number_of_entrances']
        print(f"{plate}: {tt:.2f} toll paid ({ns} routes covered in {ne} entrances)")


# reverse the motorway sections in the TURIN --> MILAN direction to get the
# MILAN --> TURIN direction
def reverseSections(sections_tomi):
    res = [] 
    # iterate over the list in reverse order
    # and set the start of each MILAN --> TURIN section to be equal to the end
    # of the corresponding TURIN --> MILAN section, and viceversa
    for elem in sections_tomi[::-1]:
        res.append({
            'start': elem['end'],
            'end': elem['start'],
            'toll': elem['toll'],
        })
    return res


def main():
    sections_tomi = readTolls('toll.txt')
    sections_mito = reverseSections(sections_tomi)
    cars = processCars('cars.txt', sections_tomi, sections_mito)
    printOutput(cars)

    # find the car that paid the maximum toll
    max_plate = ''
    max_toll = -1
    for plate in cars:
        if cars[plate]['total_toll'] > max_toll:
            max_plate = plate
            max_toll = cars[plate]['total_toll']
    print(f"The car that paid the highest toll has a {max_plate} license plate")


main()