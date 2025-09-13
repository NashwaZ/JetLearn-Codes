class Tree_Node():
    def __init__(self, data):
        self.value = data
        self.right_node = None
        self.left_node = None


def add_node(root, n_value):
    if n_value > root.value:
        root.right_node = add_node(root.right_node,n_value)
    if n_value < root.value:
        root.left_value = add_node(root.left_node, n_value)
    if root == None:
        return Tree_Node(n_value)
    
def in_order(root):
    if root.left_node is not None:
        root = in_order(root.left_node)
    print(root.value)
    if root.right_node is not None:
        root = in_order(root.right_node)

def BT_search(s_value, root):
    if s_value == root.value:
        return root.value
    elif s_value > root.value and  root.right_node is not None:
        return BT_search(s_value, root.right_node)
    elif s_value < root.value and root.left_node is not None:
        return BT_search(s_value, root.left_node)
    else:
        return -1
    

    
    



