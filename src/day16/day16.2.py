import math
import time
from route import Nodes

point_scores = {}


def readFile(file_path):
    gamemap = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            gamemap.append(row.replace("\n", ""))
    return gamemap


def run():
    # mapdata = readFile("./test_input2.txt")
    # mapdata = readFile("./test_input.txt")
    mapdata = readFile("./input.txt")
    starting_point = (1,len(mapdata)-2,">")
    nodes = Nodes((starting_point[0], starting_point[1]),starting_point[2], mapdata)
    nodes.create_network(((starting_point[0], starting_point[1]),starting_point[2]))
    print(nodes.get_score())
    


if __name__ == "__main__":
    run()