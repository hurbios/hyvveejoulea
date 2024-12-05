def readFile(file_path):
    rows = ""
    with open(file_path, 'r') as file:
        for row in file:
            rows+=row
    return rows

def get_mul_nums(row):
    command_depth = 0
    disabled = False
    num1string = ""
    num2string = ""
    mul_nums = []
    for i, char in enumerate(row):
        if disabled:
            if i >= 4 and row[i-3:i+1] == "do()":
                num1string = ""
                num2string = ""
                command_depth = 0
                disabled = False
            continue
        if i >= 7 and row[i-6:i+1] == "don\'t()":
            num1string = ""
            num2string = ""
            command_depth = 0
            disabled = True
            continue
        if command_depth == 0 and char == "m":
            command_depth+=1
        elif command_depth == 1 and char == "u":
            command_depth+=1
        elif command_depth == 2 and char == "l":
            command_depth+=1
        elif command_depth == 3 and char == "(":
            command_depth+=1
        elif command_depth == 4 and char in ["1","2","3","4","5","6","7","8","9","0"]:
            num1string += char
            if len(row) > i+1 and row[i+1] not in ["1","2","3","4","5","6","7","8","9","0"]:
                command_depth+=1
        elif command_depth == 5 and char == ",":
            command_depth+=1
        elif command_depth == 6 and char in ["1","2","3","4","5","6","7","8","9","0"]:
            num2string += char
            if len(row) > i+1 and row[i+1] not in ["1","2","3","4","5","6","7","8","9","0"]:
                command_depth+=1
        elif command_depth == 7 and char == ")":
            mul_nums.append((int(num1string), int(num2string)))
            num1string = ""
            num2string = ""
            command_depth = 0
        else:
            num1string = ""
            num2string = ""
            command_depth = 0
    return mul_nums

def mul_func(nums):
    return nums[0] * nums[1]

def main():
    #rows = readFile("./test_input2.txt")
    #rows = readFile("./test_input.txt")
    rows = readFile("./input.txt")
    num_pairs = get_mul_nums(rows)
    #print(f"output: {num_pairs}")
    print(sum(map(mul_func, num_pairs)))

if __name__ == "__main__":
    main()
