from trailmap import Trailmap

def readFile(file_path):
    sequence = []
    trailheads = []
    with open(file_path, 'r') as file:
        for y, row in enumerate(file):
            rowseq = []
            for x, col in enumerate(row.replace("\n", "")):
                rowseq.append(int(col))
                if col == "0":
                    trailheads.append((x,y))
            sequence.append(rowseq)
    return sequence, trailheads


def main():
    #mapdata, trailheads = readFile("./test_input.txt")
    mapdata, trailheads = readFile("./input.txt")
    #print(trailmap)
    #print(trailheads)
    
    trailmap = Trailmap(mapdata)
    scores = []
    for trailhead in trailheads:
        scores.append(trailmap.get_traihead_score(trailhead))
    #print(scores)
    print(f"sum of trailhead scores: {sum(scores)}")
    
    

if __name__ == "__main__":
    main()
