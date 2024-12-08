import itertools

def readFile(file_path):
    maparea = []
    with open(file_path, 'r') as file:
        for row in file:
            maparea.append(row.replace("\n", ""))   
    return maparea

def get_antennas(maparea):
    antennas = {}
    for y,row in enumerate(maparea):
        for x,col in enumerate(row):
            if col.isalnum():
                if col not in antennas:
                    antennas[col] = [(x,y)]
                else:
                    antennas[col].append((x,y))
    return antennas

def get_boundaries(maparea):
    yboundary = len(maparea) - 1
    return (len(maparea[0]) - 1 if yboundary >= 0 else 0, yboundary if yboundary >= 0 else 0)

def check_antinode_boundaries(antinode, mapboundaries):
    if antinode[0] > mapboundaries[0] or antinode[0] < 0 or antinode[1] > mapboundaries[1] or antinode[1] < 0:
        return False
    return True

def get_antinodes(antenna1, antenna2, mapboundaries):
    antinodes = set()
    antinode1x = antenna1[0] + (antenna1[0] - antenna2[0])
    antinode1y = antenna1[1] + (antenna1[1] - antenna2[1])
    antinode2x = antenna2[0] + (antenna2[0] - antenna1[0])
    antinode2y = antenna2[1] + (antenna2[1] - antenna1[1])
    antinode1 = (antinode1x,antinode1y)
    antinode2 = (antinode2x,antinode2y)
    if check_antinode_boundaries(antinode1, mapboundaries):
        antinodes.add(antinode1)
    if check_antinode_boundaries(antinode2, mapboundaries):
        antinodes.add(antinode2)
    return antinodes

def get_antenna_type_antinodes(antennanodes, mapboundaries):
    antinodes = set()
    for products in itertools.combinations(antennanodes, 2):
        tempantinodes = get_antinodes(products[0], products[1], mapboundaries)
        antinodes.update(tempantinodes)
    antinodes.discard(None)
    return antinodes


def main():
    #maparea = readFile("./test_input.txt")
    maparea = readFile("./input.txt")
    antennas = get_antennas(maparea)
    mapboundaries = get_boundaries(maparea)
    #print(antennas)
    #print(mapboundaries)
    antinodes = set()
    for antenna in antennas:
        antenna_type_antinodes = get_antenna_type_antinodes(antennas[antenna], mapboundaries)
        #print(f"antenna tyep: {antenna}, antennas: {antennas[antenna]}, anitnodes: {antenna_type_antinodes}")
        antinodes.update(antenna_type_antinodes)
    print(f"Number of antinodes: {len(antinodes)}")

if __name__ == "__main__":
    main()
