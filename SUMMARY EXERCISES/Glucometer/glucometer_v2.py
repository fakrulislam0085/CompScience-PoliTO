def sortByLen(elem):
    return len(elem[1])

GLUCOSE_THRESHOLD = 200

try:
    f = open("glucometer.txt", "r")
except FileNotFoundError:
    exit("Cannot open measurements file")

# Step 1: read file and store violations
violations = {}
for line in f:
    fields = line.rstrip().split(" ")
    patient = fields[0]
    time = fields[1]
    try:
        glucose = int(fields[2])
    except ValueError:
        print(f"Invalid reading {fields[2]}. Skipping...")
        continue
    if glucose >= GLUCOSE_THRESHOLD:
        new_violation = (time, glucose)
        # if the patient is not already in the dictionary, create an
        # empty list before appending the first violation
        if patient not in violations:
            violations[patient] = []
        violations[patient].append(new_violation)
f.close()

# Step 2: sort...
sorted_items = sorted(violations.items(), key=sortByLen, reverse=True)

# Step 3: print output
for elem in sorted_items:
    patient = elem[0]
    violations = elem[1]
    for vio in violations:
        print(f"{patient} {vio[0]} {vio[1]}")
    print()