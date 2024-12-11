import math

def readFile(file_path):
    sequence = []
    with open(file_path, 'r') as file:
        for row in file:
            for col in row.replace("\n", "").split(" "):
                sequence.append(int(col))

    return sequence

def get_divided(digits, stone):
    half_length = digits//2
    divider = math.pow(10, half_length)
    stone1 = int(stone // divider)
    stone2 = int(stone % divider)
    return [stone1, stone2]

def apply_stone_rules(stone):
    if stone == 0:
        return [1]

    digits = int(math.log10(stone)) + 1
    if digits % 2 == 0:
        return get_divided(digits, stone)

    return [stone*2024]



def main():
    #stones = readFile("./test_input.txt")
    stones = readFile("./input.txt")
    stone_amounts = {}
    for stone in stones:
        if stone not in stone_amounts:
            stone_amounts[stone] = 1

    stone_result_cache = {}

    print(stone_amounts)
    for i in range(75):
        print(f"--- {i} ---")
        second_stones = {}
        for stone in stone_amounts.items():
            #print(stone)
            if stone[0] not in stone_result_cache:
                stone_result_cache[stone[0]] = apply_stone_rules(stone[0])
                #print(stone_result_cache[stone[0]])
            for new_stone in stone_result_cache[stone[0]]:
                if new_stone not in second_stones:
                    second_stones[new_stone] = stone[1]
                else:
                    second_stones[new_stone] += stone[1]
        stone_amounts = second_stones
    print("####")
    print(f"amount of stones: {sum(stone_amounts.values())}")


if __name__ == "__main__":
    main()
