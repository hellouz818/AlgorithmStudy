class Node:
    def __init__(self, number):
        self.number = number
        self.children = []

    def find_child_by_number(self, number):
        for child in self.children:
            if child.number == number:
                return child

    def is_leaf(self):
        return self.children == []


def set_number(number):
    parent = root
    for c in number:
        node = Node(c)
        child = parent.find_child_by_number(c)
        if child is None:
            child = node
            parent.children.append(child)
        else:
            if child.is_leaf():
                return False
        parent = child
    if child.is_leaf() == False:
        return False
    return True


def set_numbers(numbers):
    for i, number in enumerate(numbers):
        success = set_number(number)
        if success == False:
            return False
    return True


T = int(input())
for t in range(T):
    N = int(input())
    numbers = [input() for _ in range(N)]
    root = Node("0")
    if set_numbers(numbers) == False:
        print("NO")
    else:
        print("YES")
