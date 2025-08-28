def readFlights(fileName):
    """
    Reads flight information from a file and initializes flight data.
    Each flight is stored as a dictionary with rows, columns, and reservations.

    :param fileName: Name of the file containing flight information.
    :return: Dictionary containing flight data.
    """
    with open(fileName, "r") as f:
        flights = {}
        for line in f:
            fID, model, rows, cols = line.strip().split()
            try:
                rows, cols = int(rows), int(cols)
            except ValueError:
                print("Flights file contains errors")
                exit()

            # Store flight configuration; initialize reservations as empty (1D list)
            flights[fID] = {'rows': rows, 'cols': cols, 'reservations': [""] * rows * cols}
        
        return flights

def countFreeSeats(flightInfos):
    # Count how many seats are still unreserved (i.e., empty strings)
    return flightInfos['reservations'].count("")

def bookSeats(flightInfos, nSeats, name, surname):
    # Allocate nSeats to the given passenger, filling the first available slots
    for i in range(len(flightInfos['reservations'])):
        if flightInfos['reservations'][i] == "":
            flightInfos['reservations'][i] = name + " " + surname
            nSeats -= 1
            if nSeats == 0:
                return

def cancelSeats(fInfos, name, surname):
    # Remove all seats reserved by the passenger
    for i in range(len(fInfos['reservations'])):
        if fInfos['reservations'][i] == name + " " + surname:
            fInfos['reservations'][i] = ""

def printFlight(flight):
    # Print reservations with their row and column position
    idx = 0
    for i in range(flight['rows']):
        for j in range(flight['cols']):
            if flight['reservations'][idx] != "":
                print(f"{i+1} {j+1} {flight['reservations'][idx]}")
            idx += 1

def main():
    # Initialize flights from file
    flights = readFlights('flights.txt')

    with open('booking.txt', 'r') as f:
        for line in f:
            line = line.strip()
            fields = line.split()

            opCode, fID, name, surname = fields[:4]

            if opCode == "BOOK":
                try:
                    nSeats = int(fields[4])
                except ValueError:
                    print("Cannot convert n. of seats to integer. Terminating...")
                    exit()

                # Check if booking is valid and seats are available
                if fID not in flights or nSeats > countFreeSeats(flights[fID]):
                    print(line + " - Fail")
                else:
                    bookSeats(flights[fID], nSeats, name, surname)

            elif opCode == "CANCEL":
                cancelSeats(flights[fID], name, surname)

            else:
                print(f"Invalid opCode {opCode}. Terminating the program...")
                exit()

        # Display all flights with booked seat information
        for fID in sorted(flights):
            print(f"Flight {fID}:")
            printFlight(flights[fID])

if __name__ == "__main__":
    main()

