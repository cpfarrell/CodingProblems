import bin_tree
import print_tree_level

def trim(root, min, max):
    if not root:
        return
    if root.value<min:
        return trim(root.right, min, max)
    if root.value>max:
        return trim(root.left, min, max)
    root.left = trim(root.left, min, max)
    root.right = trim(root.right, min, max)
    return root

a = bin_tree.bin_node(1, None, None)
b = bin_tree.bin_node(3, None, None)
c = bin_tree.bin_node(5, None, None)
d = bin_tree.bin_node(7, None, None)
e = bin_tree.bin_node(2, a, b)
f = bin_tree.bin_node(6, c, d)
g = bin_tree.bin_node(4, e, f)
tree = bin_tree.bin_tree(g)
print_tree_level.print_tree(tree)
g = trim(g, -4
,13)
tree = bin_tree.bin_tree(g)

print_tree_level.print_tree(tree)
