import math
import time

visited_scores = {0:[]}
point_scores = {}


def readFile(file_path):
    gamemap = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            gamemap.append(row.replace("\n", ""))
    return gamemap

def print_map(mapdata, line):
    mapcopy=mapdata.copy()
    # print(mapcopy)
    for point in line:
        mapcopy[point[1]] = mapcopy[point[1]][:point[0]]+point[2]+mapcopy[point[1]][point[0]+1:]
    graph = ""
    for row in mapcopy:
        for col in row:
            graph+=col
        graph+="\n"
    print(graph)
    # return graph


def visit(direction, mapdata, previous_step, score):
    allowed_directions = {"^":["^","<",">"],"<":["^","v","<"],">":["^","v",">"],"v":["v","<",">"]}
    point_scores[previous_step] = { "value": score.get("value"), "checked": True }
    curr_position = (previous_step[0] + direction[0], previous_step[1] + direction[1], direction[2])
    if not direction[2] in allowed_directions[previous_step[2]]:
        return math.inf, False
    new_score = (score.get("value") + 1 if previous_step[2] == curr_position[2] else score.get("value") + 1001)
    if mapdata[curr_position[1]][curr_position[0]] == "E":
        # print(previous_step, curr_position)
        return new_score, True
    if curr_position in point_scores and point_scores[curr_position].get("value") < new_score:
        return math.inf, False
    if mapdata[curr_position[1]][curr_position[0]] == "#":
        point_scores[curr_position] = { "value": math.inf, "checked": True }
        return math.inf, False

    point_scores[curr_position] = { "value": new_score, "checked": False }

    return new_score, False



def run():
    # madata = readFile("./test_input2.txt")
    # madata = readFile("./test_input.txt")
    madata = readFile("./input.txt")
    startin_point = (1,len(madata)-2,">")
    visited_scores[0].append([startin_point])
    point_scores[startin_point] = {"value": 0, "checked": False}
    i=0
    finalscore = False
    while True:
        print("i",i)
        # filtered = filter(lambda x: not point_scores[x].get("checked"),point_scores)
        # if len(filtered) <= 0:
        #     break
        try:
            i=min(filter(lambda x: not point_scores[x].get("checked"),point_scores), key=point_scores.get("score"))
        except ValueError:
            break
        directions = [(0,-1,"^"),(0,1,"v"),(-1,0,"<"),(1,0,">")]
        for direction in directions:
            score, finished = visit(direction,madata,i,point_scores[i])
            if finished and (not finalscore or score < finalscore):
                finalscore = score


        # if finalscore:
        #         break
        
        # time.sleep(0.1)

    print("finalscore: ", finalscore)


if __name__ == "__main__":
    run()