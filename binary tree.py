class node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.value=key

root=node(1)
root.right=node(2)
root.left=node(3)
root.right.right=node(4)