values = [10, 50, 30, 40, 10, 100, 200]
limit = 40 
pos = 0
found = False 

while pos < len(values) and not found:
    if values[pos] > limit:
        found = True
    else:
        pos += 1
if found:
    print(f"Found a value greater than {limit} at index {pos}")
else:    
    print(f"Value greater that {limit} not found at index {pos}")