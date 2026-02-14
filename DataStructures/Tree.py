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

print("In-order:", in_order(root))


def pre_order(root):
    print(root.value)
    if root.left_node != None:
        pre_order(root.left_node)
    if root.right_node != None:
        pre_order(root.right_node)

print("Pre-order:", pre_order(root))



def post_order(root):
    if root.left_node != None:
        post_order(root.left_node)
    if root.right_node != None:
        post_order(root.right_node)
    print(root.value)

print("Post-order:", post_order(root))
        


# in_order: left parent right
# pre-order: parent left right
# post-order: left right parent 
