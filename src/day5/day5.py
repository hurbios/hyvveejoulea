from NodeTree import NodeTree

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
    incorrect_sets = []
    for page_set in pages:
        if nodes.is_list_correct_order(page_set):
            correct_sets.append(page_set)
        else:
            incorrect_sets.append(page_set)
        

    #print(f"Sum of correct sets middle page numbers: {sum(map(lambda x: int(x[len(x)//2]), correct_sets))}")
    
    #print(incorrect_sets)

    for page_set in incorrect_sets:
        nodes.fix_list_order(page_set)
    
    #print(incorrect_sets)
    print(f"Sum of correct sets middle page numbers: {sum(map(lambda x: int(x[len(x)//2]), incorrect_sets))}")

if __name__ == "__main__":
    main()
