import sys
from collections import deque
import bin_tree

def print_tree_reverse(tree):
    nodes = deque()
    nodes.append(tree.root)
    nodes.append(None)
    output = []
    while nodes:
        next = nodes.popleft()
        if next:
            output.append(str(next.value) + " ")
            if next.left:
                nodes.append(next.left)
            if next.right:
                nodes.append(next.right)
        elif len(nodes)>0:
            output.append("\n")
            nodes.append(None)

    #Remove trailing newline
    for node in reversed(output):
        sys.stdout.write(node)

    #Add last newline
    sys.stdout.write("\n")

a = bin_tree.bin_node(1, None, None)
b = bin_tree.bin_node(2, None, None)
c = bin_tree.bin_node(3, None, None)
d = bin_tree.bin_node(4, None, None)
e = bin_tree.bin_node(5, a, b)
f = bin_tree.bin_node(6, c, None)
g = bin_tree.bin_node(7, e, f)
tree = bin_tree.bin_tree(g)
print_tree_reverse(tree)
