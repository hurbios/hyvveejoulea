class Node:
    def __init__(self, id):
        self._id = id
        self._children = []

    def get_id(self):
        return self._id
    
    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children
    
    def is_child(self, value):
        return value in self._children

    def __str__(self):
        return self._id
    
    def __eq__(self, value):
        return self._id == value

class NodeTree:
    def __init__(self):
        self._nodes = {}

    def add_node(self, value):
        if value not in self._nodes:
            self._nodes[value] = Node(value)

    def add_rule(self, rule):
        if rule[0] in self._nodes:
            self._nodes[rule[0]].add_child(rule[1])

    def get_node(self, id):
        return self._nodes[id] if id in self._nodes else None
    
    def is_list_correct_order(self, page_set):
        for i,page in enumerate(page_set):
            for y in range(i):
                if self._nodes[page].is_child(page_set[y]):
                    return False
        return True

    def __iter__(self):
        return iter(self._nodes)
    
    def values(self):
        return iter(self._nodes.values())

    

def readFile(file_path):
    rules = []
    pages = []
    delimeted = False
    with open(file_path, 'r') as file:
        for row in file:
            if not delimeted:
                if row == "\n":
                    delimeted = True
                else:
                    rules.append(row.replace("\n", "").split("|"))
            else:
                pages.append(row.replace("\n", "").split(","))

    return (rules, pages)


def main():
    #rules, pages = readFile("./test_input.txt")
    rules, pages = readFile("./input.txt")
    nodes = NodeTree()

    for page_set in pages:
        for n in page_set:
            nodes.add_node(n)

    for rule in rules:
        nodes.add_rule(rule)

    # for n in nodes.values():
    #     print(f"{n}, children: {n.get_children()}")
            
    correct_sets = []
    for page_set in pages:
        if nodes.is_list_correct_order(page_set):
            correct_sets.append(page_set)
        
    #print(correct_sets)

    print(f"Sum of correct sets middle page numbers: {sum(map(lambda x: int(x[len(x)//2]), correct_sets))}")
    

if __name__ == "__main__":
    main()
