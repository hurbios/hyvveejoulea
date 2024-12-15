
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
    # prize_x = int(seq["PRIZE"][0]) + 10000000000000
    # prize_y = int(seq["PRIZE"][1]) + 10000000000000
    prize_x = int(seq["PRIZE"][0])
    prize_y = int(seq["PRIZE"][1])
    while a_result_X < prize_x and a_result_Y < prize_y:
        i+=1
        a_result_X = int(seq["A"][0]) * i
        a_result_Y = int(seq["A"][1]) * i
        y=0
        b_result_X = 0
        b_result_Y = 0
        while b_result_X + a_result_X < prize_x and b_result_Y + a_result_Y < prize_y:
            y+=1
            b_result_X = int(seq["B"][0]) * y
            b_result_Y = int(seq["B"][1]) * y

        # if i == 80:
        #     print(b_result_X,a_result_X,prize_x,"--", b_result_Y, a_result_Y, prize_y)
        if b_result_X + a_result_X == prize_x and b_result_Y + a_result_Y == prize_y:
            solutions.append((i,y))

    return solutions


#
# 94A + 22B = 8400
# 34A + 67B = 5400
# 
# X1*A + X2*B = P1
# Y1*A + Y2*B = P2
#
# A = (P1 * Y2 - P2 * X2) / (X1 * Y2 - Y1 * X2)
# B = (P1 * Y1 - X1 * P2) / (Y1 * X2 - X1 * Y2)
#
def get_possible_combinations2(seq):
    # print(seq)
    X1=int(seq["A"][0])
    X2=int(seq["B"][0])
    Y1=int(seq["A"][1])
    Y2=int(seq["B"][1])
    P1=int(seq["PRIZE"][0]) + 10000000000000
    P2=int(seq["PRIZE"][1]) + 10000000000000

    A = (P1 * Y2 - P2 * X2) / (X1 * Y2 - Y1 * X2)
    B = (P1 * Y1 - X1 * P2) / (Y1 * X2 - X1 * Y2)

    #print(A, B)

    if A == float(int(A)) and B == float(int(B)):
        return [(int(A), int(B))]
    else:
        return []


def main():
    #seqs = readFile("./test_input.txt")
    seqs = readFile("./input.txt")

    solutions = []
    i=0
    for seq in seqs:
        print(f"--- getting {i} ---")
        solutions.append(get_possible_combinations2(seq))
        i+=1

    price = 0

    for solution in solutions:
        cheapest = False
        for s in solution:
            cheapest = s[0]*3+s[1]*1 if not cheapest or s[0]*3+s[1]*1 < cheapest else cheapest
        price+=cheapest
                
    print(price)

if __name__ == "__main__":
    main()
