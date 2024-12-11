# --- Day 7: No Space Left On Device ---
# https://adventofcode.com/2022/day/7


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.isDirectory = False
        self.size = 0
        self.parent = None
        self.contents_size = 0

    def __str__(self):
        if not self.isDirectory:
            return "File {} {} ".format(self.name, self.size)
        else:
            msg = "Dir {} {} [".format(self.name, self.contents_size)
            for child in self.children:
                msg += "{}".format(str(child))
            msg += "]"
            return msg


filename = "day07_puzzle.txt"
f = open(filename, "r")
commands = f.read().split("\n")

files = []
directories = []

currently_listing = False
root_node = None
current_node = None
for cmd in commands:
    if cmd.startswith("$ cd /"):
        root_node = Node("/")
        root_node.isDirectory = True
        current_node = root_node
        currently_listing = False
    if cmd.startswith("$ cd"):
        value = cmd.split(" ")[2]
        if value == "..":
            current_node = current_node.parent
        else:
            for node in current_node.children:
                if node.name == value:
                    current_node = node
        currently_listing = False
        # Do cd operation
    elif cmd.startswith("$ ls"):
        currently_listing = True
        # Next non cmd's are the directory structure
    elif cmd.startswith("dir "):
        dirName = cmd.split(" ")[1]
        directory = Node(dirName)
        directory.isDirectory = True
        directory.parent = current_node
        current_node.children.append(directory)
    elif cmd[0].isnumeric():
        fileName = cmd.split(" ")[1]
        file = Node(fileName)
        file.isDirectory = False
        file.size = int(cmd.split(" ")[0])
        file.parent = current_node
        current_node.children.append(file)


def calculate_content_size(this_node):
    for child in this_node.children:
        if child.isDirectory:
            this_node.contents_size += calculate_content_size(child)
        else:
            this_node.contents_size += child.size
    return this_node.contents_size


def get_largest_under_100k(this_node):
    if this_node.contents_size <= 100000:
        nodes_matching_criteria.append(this_node)
    for child in this_node.children:
        if child.isDirectory:
            get_largest_under_100k(child)


def get_largest_over_x(this_node, x):
    if this_node.contents_size > x:
        nodes_matching_criteria.append(this_node)
    for child in this_node.children:
        if child.isDirectory:
            get_largest_over_x(child, x)


def part_1():
    calculate_content_size(root_node)
    get_largest_under_100k(root_node)
    totals = 0
    for n in nodes_matching_criteria:
        totals += n.contents_size
    print(totals)


def part_2():
    calculate_content_size(root_node)
    free_space = 70000000 - root_node.contents_size
    required_space = 30000000 - free_space
    print(required_space)
    get_largest_over_x(root_node, required_space)

    smallest_node = root_node
    for n in nodes_matching_criteria:
        if n.contents_size < smallest_node.contents_size:
            smallest_node = n
    print(smallest_node)


nodes_matching_criteria = []
part_2()
