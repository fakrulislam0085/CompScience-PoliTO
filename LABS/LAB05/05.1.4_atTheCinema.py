MAX_CAN_BUY = 4 
TOTAL_TICKETS = 100 

def main() : 
    total_buyers = 0
    total_sells = 0

    while total_sells < TOTAL_TICKETS:
        try:
            user_input = int(input("How many tickets do you wanna buy?: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        if user_input < 1:
            print("You must buy at least 1 ticket!\n")
            continue

        if user_input > MAX_CAN_BUY:
            print(f"You can buy max {MAX_CAN_BUY} tickets. Please choose another number!\n")
            continue

        if total_sells + user_input > TOTAL_TICKETS:
            print(f"Not enough tickets left! Only {TOTAL_TICKETS - total_sells} tickets remaining.\n")
            continue

        total_sells += user_input
        total_buyers += 1
        print(f"Tickets left: {TOTAL_TICKETS - total_sells}\n")

    print(f"Total Buyers: {total_buyers}")

if __name__ == "__main__" : 
    main() 
