import sys, time
# import pygame
from gamemap import GameMap

print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

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

def input_direction(key):
    print(key if key == "^[[" else 0)


def run():
    # gamemadata, moves = readFile("./test_input4.txt")
    # gamemadata, moves = readFile("./test_input3.txt")
    # gamemadata, moves = readFile("./test_input2.txt")
    # gamemadata, moves = readFile("./test_input.txt")
    gamemadata, moves = readFile("./input.txt")
    # pygame.init()
    gamemap = GameMap(gamemadata)
    gamemap.print_map()
    moveslen = len(moves)
    i=0
    for move in moves:
        i+=1
        print(f"{i}/{moveslen}, move {move}")
        gamemap.move_robot(move)
        # print(gamemap.print_map())
        # sys.stdout.write(gamemap.print_map())
        # sys.stdout.flush()
        # time.sleep(0.5)
    # while True:
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             ch = False
    #             if event.key == pygame.K_LEFT:
    #                 ch = "<"
    #             elif event.key == pygame.K_RIGHT:
    #                 ch = ">"
    #             elif event.key == pygame.K_UP:
    #                 ch = "^"
    #             elif event.key == pygame.K_DOWN:
    #                 ch = "v"
    #             if ch:
    #                 gamemap.move_robot(ch)

    #     # gamemap.print_map()
    #     sys.stdout.write(gamemap.print_map())
    #     sys.stdout.flush()
    #     time.sleep(0.5)


    print(gamemap.get_GPS_sum())

if __name__ == "__main__":
    run()

# just awful code but gets it done...
