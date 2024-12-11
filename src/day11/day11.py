def readFile(file_path):
    sequence = []
    with open(file_path, 'r') as file:
        for row in file:
            for col in row.replace("\n", "").split(" "):
                sequence.append(int(col))

    return sequence

def apply_stone_rules(stone):
    if stone == 0:
        return [1]
    str_stone = str(stone)
    if len(str_stone) % 2 == 0:
        half_length = len(str_stone)//2
        return [int(str_stone[:half_length]), int(str_stone[half_length:])]
    return [stone*2024]


def main():
    #stones = readFile("./test_input.txt")
    stones = readFile("./input.txt")

    for i in range(25):
        print(i)
        second_stones = []
        for stone in stones:
            for new_stone in apply_stone_rules(stone):
                second_stones.append(new_stone)
        stones = second_stones
        #print(stones)
    print(len(stones))


if __name__ == "__main__":
    main()
