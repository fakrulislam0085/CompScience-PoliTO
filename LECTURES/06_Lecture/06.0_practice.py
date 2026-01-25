#Variant page 86
#calculate the final score after removing the lowest two values
def finalScore(s) :
    min_s = min(s)
    for element in s :
        if element == min_s :
            s.remove(element)
    return s

def main() :
    scores = [8, 4, 7, 9, 9, 7, 5, 10]
    first = finalScore(scores)
    first2 = finalScore(first)
    summ = sum(first2)
    print("Final Score:",summ)

main()
