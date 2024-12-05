def readFile(file_path):
    col0 = []
    col1 = []
    with open(file_path, 'r') as file:
        for row in file:
            cols = row.split("   ")
            col0.append(int(cols[0]))
            col1.append(int(cols[1]))
    return (col0, col1)

def main():
    print("hello")
    col0, col1 = readFile('./input.txt')
    sorted0 = sorted(col0)
    sorted1 = sorted(col1)
    
    distances = []
    for i, s0 in enumerate(sorted0):
        distances.append(abs(s0 - sorted1[i]))

    similarities = []
    for s0 in sorted0:
        similarities.append(s0 * sorted1.count(s0))

    print(f"1. distances {sum(distances)}")
    print(f"2. similarity {sum(similarities)}")

if __name__ == "__main__":
    main()

