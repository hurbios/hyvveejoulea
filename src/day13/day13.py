
def readFile(file_path):
    sequence = []
    i=0
    with open(file_path, 'r') as file:
        temp = {}
        for row in file:
            if "Button A: " in row:
                temp["A"] = row.replace("\n", "").replace("Button A: ","").replace("X+","").replace("Y+","").split(", ")
            elif "Button B: " in row:
                temp["B"] = row.replace("\n", "").replace("Button B: ","").replace("X+","").replace("Y+","").split(", ")
            elif "Prize: " in row:
                temp["PRIZE"] = row.replace("\n", "").replace("Prize: ","").replace("X=","").replace("Y=","").split(", ")
                sequence.append(temp)
                temp = {}
                i+=1

    return sequence

def get_possible_combinations(seq):
    #print(seq)
    a_result_X = 0
    a_result_Y = 0
    i=0
    solutions = []
    prize_x = int(seq["PRIZE"][0])
    prize_y = int(seq["PRIZE"][1])
    while a_result_X < prize_x and a_result_Y < prize_y and i <= 100:
        i+=1
        a_result_X = int(seq["A"][0]) * i
        a_result_Y = int(seq["A"][1]) * i
        y=0
        b_result_X = 0
        b_result_Y = 0
        while b_result_X + a_result_X < prize_x and b_result_Y + a_result_Y < prize_y  and y <= 100:
            y+=1
            b_result_X = int(seq["B"][0]) * y
            b_result_Y = int(seq["B"][1]) * y

        # if i == 80:
        #     print(b_result_X,a_result_X,prize_x,"--", b_result_Y, a_result_Y, prize_y)
        if b_result_X + a_result_X == prize_x and b_result_Y + a_result_Y == prize_y:
            solutions.append((i,y))

    return solutions

def main():
    #seqs = readFile("./test_input.txt")
    seqs = readFile("./input.txt")

    solutions = []
    for seq in seqs:
        solutions.append(get_possible_combinations(seq))

    price = 0

    for solution in solutions:
        cheapest = False
        for s in solution:
            cheapest = s[0]*3+s[1]*1 if not cheapest or s[0]*3+s[1]*1 < cheapest else cheapest
        price+=cheapest
                
    print(price)

if __name__ == "__main__":
    main()
