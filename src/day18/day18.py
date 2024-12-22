
from dijkstra import Dijkstra
def readFile(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        for row in file:
            [x,y] = row.replace("\n","").split(",")
            data.append((int(x),int(y)))
            
    return data


def create_node_network(d, nodes, dimensions, blocked):
    for n1 in nodes:
        for direction in [(-1,0),(1,0),(0,-1),(0,1)]:
            n2 = (n1[0] + direction[0], n1[1] + direction[1])
            if n2[0] <= dimensions and n2[0] >= 0 and n2[1] <= dimensions and n2[1] >= 0 and n2 not in blocked:
                d.add_edge(n1,n2,1)
        

def run():
    # dimensions, cutoff, blocked = 6, 12, readFile("./test_input.txt")
    dimensions, cutoff, blocked = 70, 1024, readFile("./input.txt")
    

    for i in range(cutoff, len(blocked),1):
        nodes = []
        for y in range(dimensions+1):
            for x in range(dimensions+1):
                if (x,y) not in blocked[:i]:
                    nodes.append((x,y))
        d = Dijkstra(nodes)

        create_node_network(d, nodes, dimensions, blocked[:i])

        distances = d.find_distances((0,0))

        # print(blocked[:i])
        print(i, " - distance =", distances[dimensions,dimensions])

        if distances[dimensions,dimensions] == float("inf"):
            print(f"{blocked[i-1]} blocks route")
            break



if __name__ == '__main__':
    run()