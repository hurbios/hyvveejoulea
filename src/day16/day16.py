import math
import time

visited_scores = {0:[]}


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


def visit(direction, mapdata, previous_steps, score):
    allowed_directions = {"^":["^","<",">"],"<":["^","v","<"],">":["^","v",">"],"v":["v","<",">"]}
    previous_step = previous_steps[-1]
    if not direction[2] in allowed_directions[previous_step[2]]:
        # print("asdf", previous_step, allowed_directions[previous_step[2]], direction)
        return math.inf, False
    curr_position = (previous_step[0] + direction[0], previous_step[1] + direction[1], direction[2])
    if mapdata[curr_position[1]][curr_position[0]] == "E":
        return (score + 1 if previous_step[2] == curr_position[2] else score + 1000), True
    if curr_position in previous_steps:
        return math.inf, False
    if mapdata[curr_position[1]][curr_position[0]] == "#":
        # print(mapdata[curr_position[1]][curr_position[0]], curr_position)
        return math.inf, False
    
    previous_steps.append(curr_position)
    # print("asfds")

    return (score + 1 if previous_step[2] == curr_position[2] else score + 1001), False



def run():
    # madata = readFile("./test_input2.txt")
    madata = readFile("./test_input.txt")
    # madata = readFile("./input.txt")

    visited_scores[0].append([(1,len(madata)-2,">")])
    i=0
    finalscore = False
    while True:
        print("i",i)
        if len(visited_scores.keys()) == 0:
            return False
        
        i=sorted(visited_scores.keys())[0]
        while len(visited_scores[i]) > 0:
            visit_array = visited_scores[i].pop()
            # print(visit_array, len(visited_scores[i]))
            directions = [(0,-1,"^"),(0,1,"v"),(-1,0,"<"),(1,0,">")]
            for direction in directions:
                visit_array_new = visit_array.copy()
                score, finished = visit(direction,madata,visit_array_new,i)
                # print(score)
                if finished:
                    finalscore = score
                    break
                if score != math.inf:
                    if score not in visited_scores:
                        visited_scores[score] = []
                    visited_scores[score].append(visit_array_new)
            if finalscore:
                break
            # print_map(madata, visit_array)
        print_map(madata, visit_array_new)
        # print(visited_scores)
        if len(visited_scores[i]) == 0:
            del visited_scores[i]
        if finalscore:
                break
        
        # time.sleep(0.1)
    print(visit_array_new)
    print_map(madata, visit_array_new)
    print("finalscore: ", finalscore)


if __name__ == "__main__":
    run()