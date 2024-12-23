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

cache = {}

def get_towels(types, towel):
    # print(towel)
    if towel == "":
        return 1
    result = 0
    for towel_type in types:
        if towel.startswith(towel_type):
            end_towel = towel[len(towel_type):]
            if end_towel not in cache:
                cache[end_towel] = get_towels(types, end_towel)
            result += cache[end_towel]

    return result

def run():
    types, towels = read_file("./input.txt")
    # types, towels = read_file("./test_input.txt")

    # print(types)
    # print(towels)

    correct = []
    results = []
    towel_len = len(towels)
    for i,towel in enumerate(towels):
        types_clone = types.copy()
        print(f"towel {i+1} / {towel_len}")
        result = get_towels(types_clone, towel)
        if result:
            correct.append(towel)
            results.append(result)

    # print("correct: ", correct, len(correct))
    print("correct amount: ", len(correct), "sum", sum(results))

if __name__ == "__main__":
    run()
