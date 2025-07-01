def localMaximaDetector(OurList) :
    posOfLocalMaxima = []

    for i, num in enumerate(OurList) :
        if i==0 or i==len(OurList)-1 :          #first and last value should be ignored
            continue
        elif OurList[i-1] < num > OurList[i+1] :
            posOfLocalMaxima.append(i+1)

    return posOfLocalMaxima        
 
def main() :
        integers = input("Read a sequence of integers(terminates by pressing enter or blank line): ") 
        integerList = list(map(int, integers.split()))

        result = localMaximaDetector(integerList)
        sz = len(result)

        if sz == 0 :
            print("There is no local maxima in our List!🤷‍♀️")
        elif sz >= 2 :
            print(f"The local maxima are:", end=" ")
            for pos in result : 
                print(integerList[pos - 1], end=" ")
            print(f"and their positions are respectively: {result}")

        else :
            index = result[0] - 1
            print(f"The only local maxima is: {integerList[index]}, and the position is: {result}")

if __name__ == "__main__" : 
    main()