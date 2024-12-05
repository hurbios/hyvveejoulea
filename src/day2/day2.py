def readFile(file_path):
    rows = []
    with open(file_path, 'r') as file:
        for row in file:
            cols = row.replace("\n", "").split(" ")
            rows.append(cols)
    return rows

def is_safe(row):
    increasing = None
    for i in range(1,len(row)):
        diff = int(row[i-1]) - int(row[i])
        if diff == 0:
            return i
        if abs(diff) > 3:
            return i
        if increasing is None:
            increasing = True if diff < 0 else False
        if (increasing and diff > 0) or (not increasing and diff < 0):
            return i
            
    return -1

def main():
    #rows = readFile("./test_input.txt")
    rows = readFile("./input.txt")
    safe_count = 0
    for row in rows:
        for i in range(len(row)):
            temprow = row.copy()
            temprow.pop(i)
            if is_safe(temprow) == -1:
                #print(temprow)
                safe_count+=1
                break
            
    print(f"safe count: {safe_count}")

if __name__ == "__main__":
    main()
