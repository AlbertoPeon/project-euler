
INPUT = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

INPUT2= """
3
7 4
2 4 6
8 5 9 3
"""

class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

TREE_LIST = [line.split() for line in INPUT[1:-1].split('\n')]

def build_tree(root, level, pos):
    if level < len(TREE_LIST):
        root.left = BinaryTree(TREE_LIST[level][pos])
        root.right = BinaryTree(TREE_LIST[level][pos + 1])
        build_tree(root.left, level + 1, pos)
        build_tree(root.right, level + 1, pos + 1)

def calculate_max_sum(tree):
    maximum = 0
    def calculate_max_sum_acc(tree, acc):
        nonlocal maximum
        if tree is None:
            if acc > maximum:
                maximum = acc
        else:
            calculate_max_sum_acc(tree.left, acc + int(tree.value))
            calculate_max_sum_acc(tree.right, acc + int(tree.value))
    calculate_max_sum_acc(tree, 0)
    return maximum

TREE = BinaryTree(TREE_LIST[0][0])

build_tree(TREE, 1, 0)

print(calculate_max_sum(TREE))
