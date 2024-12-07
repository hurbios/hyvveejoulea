import itertools

def readFile(file_path):
    calculations = []
    with open(file_path, 'r') as file:
        for row in file:
            splittedrow = row.replace("\n", "").split(": ")
            result = splittedrow[0]
            numbers = splittedrow[1].split(" ")
            calculations.append((result,numbers))
    return calculations

def check_equation(calculation):
    current_value=None
    #print(len(calculation[1])-1)
    for seq in itertools.product(["*","+"], repeat=len(calculation[1])-1):
        #print(seq)
        for i,num in enumerate(calculation[1]):
            if not current_value:
                current_value = int(num)
            else:
                current_value = current_value * int(num) if seq[i-1] == "*" else current_value + int(num)
        if current_value == int(calculation[0]):
            return True
        else:
            current_value = None

    return False

def main():
    calculations = readFile("./test_input.txt")
    #calculations = readFile("./input.txt")
    correct = 0
    for calculation in calculations:
        if check_equation(calculation):
            correct += int(calculation[0])
    print(f"Correct calculations: {correct}")
   

if __name__ == "__main__":
    main()
