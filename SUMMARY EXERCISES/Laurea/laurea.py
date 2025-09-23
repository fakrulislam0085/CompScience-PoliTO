def readCfu(filename):
    cfu = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                code, credits, mandatory = line.split(',')
                credits = int(credits)
                mandatory = int(mandatory)
                cfu[code] = (credits, mandatory)
    except FileNotFoundError:
        print(f"Cannot find the file {filename}")
        exit()
    except ValueError:
        print("Credits file contains some error")
        exit()

    return cfu


def main():
    cfu = readCfu('cfu2.dat')
    students = {}
    try:
        with open('exams2.log', 'r') as f:
            for line in f:
                line = line.strip()
                id, date, code, grade = line.split(',')
                # check if the exam was passed
                if grade != 'A' and grade != 'R':
                    # processed the grade
                    if grade == '30L':
                        grade = 33
                    else:
                        grade = int(grade)

                    if id not in students:
                        students[id] = {'tot': 0, 'mand': 0, 'weighted_sum': 0}

                    # get info about the exam
                    cfu_exam, mand = cfu[code]

                    # increment the total credits
                    students[id]['tot'] += cfu_exam
                    # increment the mandatory credits if the exam is mandatory
                    if mand == 1:
                        students[id]['mand'] += cfu_exam
                    # update the weighted average numerator
                    students[id]['weighted_sum'] += cfu_exam * grade

    except FileNotFoundError as error:
        print(error)
        exit()
    except ValueError:
        print(f"The grade {grade} could not be converted to an integer")
        exit()

    for s in students:
        tot = students[s]['tot']
        mand = students[s]['mand']
        ws = students[s]['weighted_sum']
        avg = ws / tot
        if students[s]['tot'] >= 30 and students[s]['mand'] >= 10:
            print(f"STUDENT {s}")
            print(f"Student with {tot} total credits; {mand} mandatory credits; {avg:.2f} average.")


main()
