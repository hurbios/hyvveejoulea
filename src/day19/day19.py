def read_file(file_path):
    types = []
    towels = []
    with open(file_path, "r", encoding="UTF-8") as file:
        for row in file:
            if len(types) == 0:
                types += sorted(row.replace("\n","").split(", "))
            elif row != "\n":
                towels.append(row.replace("\n",""))
    return types, towels


def check_type_in_sub_towel(start, typelen, towel_type, towel):
    for i in range(typelen):
        # print(i, towel_type)
        if not towel_type[i] == towel[start+i]:
            return False
    return True

checked_towels = set()

def get_towels(types, towel, start):
    # print(towel)

    for towel_type in reversed(types):
        typelen = len(towel_type)
        towel_len = len(towel)
        end_len = start + typelen
        if towel_len == end_len:
            if check_type_in_sub_towel(start, typelen, towel_type, towel):
                return True
        elif towel_len > end_len:
            if check_type_in_sub_towel(start, typelen, towel_type, towel):
                new_towel = towel[:end_len]
                if new_towel not in types:
                    # print(new_towel)
                    types.append(new_towel)
                if get_towels(types, towel, end_len):
                    return True

    return False

def run():
    types, towels = read_file("./input.txt")
    # types, towels = read_file("./test_input.txt")

    # print(types)
    # print(towels)

    correct = []
    towel_len = len(towels)
    for i,towel in enumerate(towels):
        types_clone = types.copy()
        print(f"towel {i+1} / {towel_len}")
        if get_towels(types_clone, towel, 0):
            correct.append(towel)
        # print(types_clone)

    # print("correct: ", correct, len(correct))
    print("correct amount: ", len(correct))

if __name__ == "__main__":
    run()
