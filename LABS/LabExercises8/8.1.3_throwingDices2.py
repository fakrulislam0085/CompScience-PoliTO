import random 

def dice_rolls() : 
    dice_roll_list = [] 

    for i in range(20) : 
        a = random.randint(1, 6) 
        dice_roll_list.append(a)        # [for random.randint(1, 6) _ in range(20)]
    

    max_length = 1  
    longest_seq = 1
    max_len_finishing_indx = 0 
    for i in range (1, 20) : 
        if dice_roll_list[i] == dice_roll_list[i-1] : 
            longest_seq += 1 

            if longest_seq > max_length :
                max_length = longest_seq 
                max_len_finishing_indx = i 
        else : 
            longest_seq = 1
    
    max_len_starting_indx = abs((max_length-1) - max_len_finishing_indx)
    print(f"Unformatted dice rolls: {dice_roll_list}")
    formatted_list = ' '.join(map(str, dice_roll_list))
    print(f"Formatted dice rolls: {formatted_list}")
    # print(max_length)
    # print(max_len_finishing_indx) 
    # print(max_len_starting_indx)
 
    resultList = list()
    for i in range(len(dice_roll_list)) : 
        if i== max_len_starting_indx : 
            resultList.append('(') 

        resultList.append(dice_roll_list[i])
        
        if i == max_len_finishing_indx : 
            resultList.append(')') 
        
    print(f"Formatted result: {' '.join(map(str,resultList ))}")
    

def main() : 
    dice_rolls() 


if __name__ == "__main__" : 
    main() 