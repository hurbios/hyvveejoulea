from gamemap import GameMap

def readFile(file_path):
    gamemap = []
    mapdone = False
    moves = ""
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            if row == "\n":
                mapdone = True
            elif not mapdone:
                gamemap.append(row.replace("\n", ""))
            else:
                moves+=row.replace("\n", "")
    return gamemap, moves

def run():
    # gamemadata, moves = readFile("./test_input2.txt")
    # gamemadata, moves = readFile("./test_input.txt")
    gamemadata, moves = readFile("./input.txt")
    gamemap = GameMap(gamemadata)
    # gamemap.print_map()

    for move in moves:
        # print(f"move {move}")
        gamemap.move_robot(move)
        # gamemap.print_map()

    print(gamemap.get_GPS_sum())

if __name__ == "__main__":
    run()
