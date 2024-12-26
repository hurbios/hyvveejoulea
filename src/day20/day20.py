from dijkstra import Dijkstra

def read_file(filepath):
    start, end, walls = (),(),[]
    with open(filepath, 'r', encoding="UTF-8") as file:
        for y,row in enumerate(file):
            for x, col in enumerate(row):
                if col == "#":
                    walls.append((x,y))
                elif col == "S":
                    start = (x,y)
                elif col == "E":
                    end = (x,y)
    return start, end, walls, len(row)


def create_node_network(d, nodes, dimensions, walls):
    for n1 in nodes:
        for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
            n2 = (n1[0] + direction[0], n1[1] + direction[1])
            if n2[0] <= dimensions and n2[0] >= 0 and n2[1] <= dimensions and n2[1] >= 0 and n2 not in walls:
                d.add_edge(n1,n2,1)

def add_cheat_edges_h(d, nodes, wall):
    if (wall[0]-1, wall[1]) in nodes and (wall[0]+1, wall[1]) in nodes:
        d.add_edge((wall[0]-1, wall[1]),(wall[0]+1, wall[1]),2)
        return True
    return False

def add_cheat_edges_v(d, nodes, wall):
    if (wall[0], wall[1]-1) in nodes and (wall[0], wall[1]+1) in nodes:
        d.add_edge((wall[0], wall[1]-1),(wall[0], wall[1]+1),2)
        return True
    return False

def remove_cheat_edges_h(d, nodes, wall):
    if (wall[0]-1, wall[1]) in nodes and (wall[0]+1, wall[1]) in nodes:
        d.remove_edge((wall[0]-1, wall[1]),(wall[0]+1, wall[1]),2)

def remove_cheat_edges_v(d, nodes, wall):
    if (wall[0], wall[1]-1) in nodes and (wall[0], wall[1]+1) in nodes:
        d.remove_edge((wall[0], wall[1]-1),(wall[0], wall[1]+1),2)

def run():
    # start, end, walls, dimensions = read_file("./test_input.txt")
    start, end, walls, dimensions = read_file("./input.txt")

    # print(start)
    # print(end)
    # print(walls)
    
    # 1. create nodes
    nodes = []
    for y in range(dimensions):
        for x in range(dimensions):
            if (x,y) not in walls:
                nodes.append((x,y))
    d = Dijkstra(nodes)

    # 2. create node network
    create_node_network(d, nodes, dimensions, walls)

    # 3. find minimum distance with dijkstra alg
    distances = d.find_distances(start)

    print("distance =", distances[end])

    cheats = []
    # 4. check cheat savings
    amountofwalls = len(walls)
    i = 0
    for wall in walls:
        print(f"{i}/{amountofwalls}")
        if add_cheat_edges_h(d, nodes, wall):
            cheat_distances = d.find_distances(start)
            # if distances[end] - cheat_distances[end] > 0:
            #     print(wall, "-", distances[end] - cheat_distances[end])
            if distances[end] - cheat_distances[end] >= 100:
                cheats.append(wall)
            remove_cheat_edges_h(d, nodes, wall)
        if add_cheat_edges_v(d, nodes, wall):
            cheat_distances = d.find_distances(start)
            # if distances[end] - cheat_distances[end] > 0:
            #     print(wall, "-", distances[end] - cheat_distances[end])
            if distances[end] - cheat_distances[end] >= 100:
                cheats.append(wall)
            remove_cheat_edges_v(d, nodes, wall)
        i+=1
    
    print("1. cheats above 100ps: ", len(cheats))

if __name__ == '__main__':
    run()
