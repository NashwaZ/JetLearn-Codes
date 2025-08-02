class BinaryNode():
    def __init__(self, data):
        self.value = data
        self.left_node = None
        self.right_node = None

root = BinaryNode(15)
root.left_node = BinaryNode(12)
root.right_node = BinaryNode(1)
root.left_node.left_node = BinaryNode(12)

def in_order(root):
    if root.left_node != None:
        in_order(root.left_node)
    print(root.value)

    if root.right_node != None:
        in_order(root.right_node)

in_order(root) 



    

