def main():
    try:
        fw = open("warehouse.txt", "r")
    except FileNotFoundError:
        exit("Cannot open warehouse file")

    # Step 1: read warehouse
    warehouse = {}
    for line in fw:
        fields = line.rstrip().split(",")
        prod = fields[0]
        try:
            price = float(fields[1])
            qty = int(fields[2])
            if prod not in warehouse:
                warehouse[prod] = [price, qty]
            else:
                print(f"Found duplicate product {prod}, skipping line...")
        except ValueError:
            print(f"Skipping line {line}", end='')
    fw.close()

    # Step 2: compute initial total price
    total_price = 0
    for prod in warehouse:
        total_price += warehouse[prod][0] * warehouse[prod][1]

    # Step 3: process the movements file
    try:
        fm = open("movements.txt", "r")
    except FileNotFoundError:
        exit("Cannot open movements file")

    for line in fm:
        fields = line.rstrip().split(",") 
        prod = fields[0]
        try:
            variation = int(fields[1])
        except ValueError:
            print(f"ERROR: Invalid variation {variation}. Skipping...")
            continue
        if prod in warehouse:
            # process product...
            prod_info = warehouse[prod]
            price = prod_info[0]
            qty = prod_info[1]
            if qty + variation < 0:
                print(f"ERROR: Required quantity of {prod} not available!\n")
            elif qty + variation > 10000:
                print(f"ERROR: Provided quantity of {prod} exceeds space!\n")
            else:
                prod_info[1] = qty + variation
                if variation > 0:
                    print_word = "Increasing"
                    print_num = variation
                else:
                    print_word = "Decreasing"
                    print_num = -1*variation
                print(f"{print_word} the quantity of {prod} by {print_num}")
                print(f"Previous total value: {total_price} Euro")
                total_price = total_price + price * variation
                print(f"New total value: {total_price} Euro\n")

        else:
            print(f"ERROR: product {prod} not existent\n")
    fm.close()

    # Step 4: write updated warehouse
    try:
        fout = open("warehouse2.txt", "w")
    except IOError:
        exit("Cannot open output file")
    for prod in warehouse:
        prod_info = warehouse[prod]
        fout.write(f"{prod},{prod_info[0]},{prod_info[1]}\n")
    fout.close()


main()