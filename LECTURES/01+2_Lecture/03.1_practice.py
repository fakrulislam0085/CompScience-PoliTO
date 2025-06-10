#This program converts cents to euros

cents = 1729
euros = 1729//100   #Calculate only the number of euros using floor division
remainingCents = 1729%100   #Calculate the number of cents
totaleuro = euros + remainingCents/100
print(totaleuro)



cents = 1729
euros = 1729/100    #directly gives us floating point value
print(euros)
