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

    def fix_list_order(self, page_set):
        changed=True
        while changed:
            changed=False
            for page in page_set:
                for check_page in page_set:
                    if check_page == page:
                        break
                    if self._nodes[page].is_child(check_page):
                        temppage = check_page
                        page_set.remove(check_page)
                        page_set.append(temppage)
                        changed=True


    def __iter__(self):
        return iter(self._nodes)
    
    def values(self):
        return iter(self._nodes.values())