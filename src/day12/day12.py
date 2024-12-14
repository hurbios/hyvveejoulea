from plant_map import PlantMap

def readFile(file_path):
    sequence = []
    with open(file_path, 'r') as file:
        for row in file:
            sequence.append(row.replace("\n", ""))
    #print(sequence)
    return sequence

def main():
    #plants = readFile("./test_input.txt")
    plants = readFile("./input.txt")

    plantmap = PlantMap(plants)
    print(plantmap.get_plant_scores())


if __name__ == "__main__":
    main()


