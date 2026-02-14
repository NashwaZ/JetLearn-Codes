class Tree_Node:
    def __init__(self, data):
        self.value = data
        self.right_node = None
        self.left_node = None

def insert_node(root, nroll_value):
    if root == None:
        return Tree_Node(nroll_value)
    if nroll_value > root.value:
        root.right_node = insert_node(root.right_node, nroll_value)
    if nroll_value < root.value:
        root.left_node = insert_node(root.left_node, nroll_value)
    return root

def in_order(root):
    if root.left_node is not None:
        in_order(root.left_node)
    print(root.value)
    if root.right_node is not None:
        in_order(root.right_node)
    if root is None:
        return

def BT_search(s_value, root):
    if s_value == root.value:
        return root.value
    elif s_value > root.value and  root.right_node is not None:
        return BT_search(s_value, root.right_node)
    elif s_value < root.value and root.left_node is not None:
        return BT_search(s_value, root.left_node)
    else:
        return -1


roll_numbers = [50, 30, 70, 20, 40, 60, 80]
root = None
for n in roll_numbers:
    root = insert_node(root, n)

print("In-order:", in_order(root))


s_value = 60
result = BT_search(s_value, root)
if result != -1:
    print(f"Roll number {s_value} is in the BST.")
else:
    print(f"Roll number {s_value} is NOT in the BST.")

root = insert_node(root, 65)

print("In-order:", in_order(root))



