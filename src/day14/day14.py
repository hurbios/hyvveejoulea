from robot import Robot
import time

def readFile(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            pv = row.replace("\n", "").replace("p=", "").split(" v=")
            data.append([pv[0].split(","),pv[1].split(",")])
    return data

def run():
    #map_boundaries = (11,7)
    #robot_data = readFile("./test_input.txt")
    map_boundaries = (101,103)
    robot_data = readFile("./input.txt")
    robots = []
    for robo in robot_data:
        robots.append(Robot(robo[0],robo[1], map_boundaries))
    
    for robot in robots:
        robot.move(100)

    quadrants = {1:[], 2:[], 3:[], 4:[]}
    dividers = (map_boundaries[0]//2, map_boundaries[1]//2)
    for robot in robots:
        robot_pos = robot.get_position()
        print(robot_pos)
        if robot_pos[0] < dividers[0]:
            if robot_pos[1] < dividers[1]:
                quadrants[1].append(robot)
            elif robot_pos[1] > dividers[1]:
                quadrants[3].append(robot)
        elif robot_pos[0] > dividers[0]:
            if robot_pos[1] < dividers[1]:
                quadrants[2].append(robot)
            elif robot_pos[1] > dividers[1]:
                quadrants[4].append(robot)
    result = False
    for quadrant in quadrants.values():
        if not result:
            result = len(quadrant)
        else:
            result *= len(quadrant)
    print(result)

    ## ====
    robots = []

    for robo in robot_data:
        robots.append(Robot(robo[0],robo[1], map_boundaries))
    

    # for robot in robots:
    #     robot.move()
    for i in range(10000):
        # time.sleep(0.1)
        # print(f"------- {i} --------")
        line = ""
        robot_positions = []
        for robot in robots:
            robot.move()
            robot_positions.append(robot.get_position())
        for row in range(map_boundaries[1]):
            for col in range(map_boundaries[0]):
                if (col,row) in robot_positions:
                    line+="#"
                else:
                    line+="."
            line+="\n"

        #clustered?
        quadrants = {1:[], 2:[], 3:[], 4:[]}
        dividers = (map_boundaries[0]//2, map_boundaries[1]//2)
        for robot in robots:
            robot_pos = robot.get_position()
            #print(robot_pos)
            if robot_pos[0] < dividers[0]:
                if robot_pos[1] < dividers[1]:
                    quadrants[1].append(robot)
                elif robot_pos[1] > dividers[1]:
                    quadrants[3].append(robot)
            elif robot_pos[0] > dividers[0]:
                if robot_pos[1] < dividers[1]:
                    quadrants[2].append(robot)
                elif robot_pos[1] > dividers[1]:
                    quadrants[4].append(robot)
        result = False
        for quadrant in quadrants.values():
            if not result:
                result = len(quadrant)
            else:
                result *= len(quadrant)
        if result < 100000000:
            print("i",i,"result",result)
            print(line)

# easter egg = i+1 & result < 60000000


if __name__ == "__main__":
    run()
