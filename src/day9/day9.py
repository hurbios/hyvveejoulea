from HardDisk import HardDisk

def readFile(file_path):
    sequence = None
    with open(file_path, 'r') as file:
        for row in file:
            sequence = row.replace("\n", "")
    return sequence


def main():
    #sequence = readFile("./test_input2.txt")
    #sequence = readFile("./test_input.txt")
    sequence = readFile("./input.txt")
    hd = HardDisk(sequence)
    #print(hd.get_defragmented_disk())
    hd.fragment_disk()
    #print(hd.get_fragmented_disk())
    #print(hd.get_sizes())
    print(hd.get_checksum())
    hd.reset_defracmented()
    hd.file_move()
    #print(hd.get_defragmented_disk())
    print(hd.get_defragmented_checksum())
    

if __name__ == "__main__":
    main()

