def fileProcess(file1, file2) : 
    with open(file1, "r") as flights, open(file2, "r") as bookings :
        flightsInfos = flights.readlines() 
        
        successfulBooking = [] 
        unsuccessfulBooking = []

        for infos in flightsInfos : 
            info = infos.split()
            flightId, model, row, col = info 

            try : 
                row = int(row) 
                col = int(col) 
            except ValueError : 
                print("The values couldn't convert to int.\n") 
                continue 
                
            seatsMap = [["O" for _ in range(col)] for _ in range(row)]

            # print(seatsMap)
            # print() 

            # reset pointer to starts 
            bookings.seek(0) 
            bookingInfos = bookings.readlines() 
            for binfos in bookingInfos : 
                binfo = binfos.split() 

                if len(binfo) == 5 : 
                    opCode, fID, name, surname, Nseats = binfo 
                    try : 
                        Nseats = int(Nseats) 
                    except : 
                        print("The value couldn't convert to int.\n") 
                        continue 
                    
                    # opCode = "BOOK" 
                  
                    if fID == flightId : 
                        # check whether the requested seats are available or not 
                        successfulBooking, unsuccessfulBooking = reserve_seats(seatsMap, row, col, fID, name, surname, Nseats, successfulBooking, unsuccessfulBooking) 

                elif len(binfo) == 4 : 
                    opCode, fID, name, surname = binfo
                    # opCode = "CANCEL" 
                    if fID == flightId and successfulBooking : 
                        successfulBooking = cancel_seats(seatsMap, row, col, name, surname, successfulBooking)

        # print unsuccessful booking info  
        print()
        for opC, fID, n, s, SN in unsuccessfulBooking : 
            print(f"{opC} {fID} {n} {s} {SN}- Fail")
        
        # print successful booking info  
        for infos in flightsInfos : 
            info = infos.split()
            flightId, model, row, col = info 

            print(f"Flight {flightId}:") 
            successfulBooking.sort(key=lambda x : (x[0], x[1]))
            for r, c, nam, snam, id in successfulBooking : 
                if (id == flightId) : 
                    print(f"{r} {c} {nam} {snam}")

            
def reserve_seats(seatsMap, row, col, fID, name, surname, Nseats, successfulBook, unsuccessfulBook): 
    # check the availability of seats 
    available = sum(row.count('O') for row in seatsMap) 

    if available >= Nseats : 
        reserved = 0    # to track the reserved seats
        for i in range(row) : 
            for j in range(col) : 
                if seatsMap[i][j] == "O" and reserved < Nseats :
                    seatsMap[i][j] = f"{name} {surname}" 
                    successfulBook.append((i+1, j+1, name, surname, fID))       # fID to compare while printing
                    reserved += 1
    else : 
        unsuccessfulBook.append(("BOOK", fID, name, surname, Nseats))

    return successfulBook, unsuccessfulBook

def cancel_seats(seatsMap, row, col, name, surname, successfulBooking) : 
        # remove the seats from the seatmap
        for i in range(row) : 
            for j in range(col) : 
                if seatsMap[i][j] == f"{name} {surname}" : 
                    seatsMap[i][j] = "O" 
        
        # remove the entries from successfulBook list 
        newSuccessfulBooking = []
        for i, j, nm, sNm, Id in successfulBooking : 
            if f"{nm} {sNm}" != f"{name} {surname}" :
                newSuccessfulBooking.append((i, j, nm, sNm, Id))
            
        return newSuccessfulBooking
        
def main() : 
    file1 = "flights.txt" 
    file2 = "booking.txt" 

    fileProcess(file1, file2) 

if __name__ == "__main__" : 
    main() 