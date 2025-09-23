# This version of the program considers also the possibility
# that the exam was passed multiple times, and considers the
# latest date for computing the average.

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
    cfu = readCfu('cfu.dat')
    students = {}
    try:
        with open('exams.log', 'r') as f:
            for line in f:
                line = line.strip()
                id, date, code, grade = line.split(',')
                # go from DD/MM/YYYY to YYYYMMDD
                # so that we can compare dates as strings!
                day, month, year = date.split('/')
                date = year + month + date
                # check if the exam was passed
                if grade != 'A' and grade != 'R':
                    # processed the grade
                    if grade == '30L':
                        grade = 33
                    else:
                        grade = int(grade)

                    if id not in students:
                        # this will be the dictionary of exams passed
                        # by this student
                        students[id] = {}

                    if code not in students[id]:
                        students[id][code] = [date, grade]
                    else:
                        # if the exam we are currently processing happened
                        # later than the one currently memorized in the
                        # dictionary, then update the dictionary
                        if students[id][code][0] < date:
                            students[id][code] = [date, grade]

    except FileNotFoundError as error:
        print(error)
        exit()
    except ValueError:
        print(f"The grade {grade} could not be converted to an integer")
        exit()

    students_stats = {}
    for s in students:
        students_stats[s] = {'tot': 0, 'mand': 0, 'weighted_sum': 0}
        # iterate over all the exams passed by this student
        for code in students[s]:
            # get the date (that i don't need anymore) and the grade
            date, grade = students[s][code]
            # get info about the exam
            cfu_exam, mand = cfu[code]
            # increment the total credits
            students_stats[s]['tot'] += cfu_exam
            # increment the mandatory credits if the exam is mandatory
            if mand == 1:
                students_stats[s]['mand'] += cfu_exam
            # update the weighted average numerator
            students_stats[s]['weighted_sum'] += cfu_exam * grade

    for s in students_stats:
        tot = students_stats[s]['tot']
        mand = students_stats[s]['mand']
        ws = students_stats[s]['weighted_sum']
        avg = ws / tot
        if students_stats[s]['tot'] >= 30 and students_stats[s]['mand'] >= 10:
            print(f"STUDENT {s}")
            print(f"Student with {tot} total credits; {mand} mandatory credits; {avg:.2f} average.")


main()
