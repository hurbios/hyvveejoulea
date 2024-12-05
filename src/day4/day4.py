def readFile(file_path):
    rows = []
    with open(file_path, 'r') as file:
        for row in file:
            rows.append(row.replace("\n",""))
    #print(rows)
    return rows


def check_xmas(x, y, dirx, diry, rows):
    # for i,char in enumerate("XMAS"):
    for i,char in enumerate("MAS"):
        if y + diry * i < 0 or len(rows) <= y + diry * i or len(rows[y + diry * i]) <= x + dirx * i or x + dirx * i < 0 or char != rows[y + diry * i][x + dirx * i]:
            return False
    return True

def get_xmas_number(x, y, rows):
    amount = 1 if check_xmas(x,y,1,1,rows) and check_xmas(x,y+2,1,-1,rows) else 0
    amount += 1 if check_xmas(x,y,-1,1,rows) and check_xmas(x,y+2,-1,-1,rows) else 0
    amount += 1 if check_xmas(x,y,1,1,rows) and check_xmas(x+2,y,-1,1,rows) else 0
    amount += 1 if check_xmas(x,y,1,-1,rows) and check_xmas(x+2,y,-1,-1,rows) else 0
    
    # obsolete 1st part:
    # amount = 1 if check_xmas(x,y,1,1,rows) else 0       # right-down
    # amount += 1 if check_xmas(x,y,1,-1,rows) else 0     # right-up
    # amount += 1 if check_xmas(x,y,-1,1,rows) else 0     # left-down
    # amount += 1 if check_xmas(x,y,-1,-1,rows) else 0    # left-up
    # amount += 1 if check_xmas(x,y,-1,0,rows) else 0     # left
    # amount += 1 if check_xmas(x,y,1,0,rows) else 0      # right
    # amount += 1 if check_xmas(x,y,0,1,rows) else 0      # down
    # amount += 1 if check_xmas(x,y,0,-1,rows) else 0     # up
    return amount

def main():
    #rows = readFile("./test_input.txt")
    rows = readFile("./input.txt")
    xmas_amounts = []

    for y, row in enumerate(rows):
        #print(y)
        for x, char in enumerate(row):
            # if char == "X":
            #     xmas_amounts.append(get_xmas_number(x, y, rows))
            xmas_amounts.append(get_xmas_number(x, y, rows))
    
    print(f"xmas amount: {sum(xmas_amounts)}")
        

if __name__ == "__main__":
    main()
