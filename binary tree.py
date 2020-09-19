##1)binary tree

# class node:
#     def __init__(self,key):
#         self.left=None
#         self.right=None
#         self.value=key
#
# root=node(1)
# root.right=node(2)
# root.left=node(3)
# root.right.right=node(4)

##2)Binary tree

class Node(object):
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value

# class BinaryTree(object):
#     def __init__(self,root):
#         self.root=Node(root)


    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder(root,'')
        elif traversal_type=='inorder':
            return self.inorder(root,'')
        elif traversal_type=='postorder':
            return self.postorder(root,'')
        else:
            print('Traversal type'+(str(traversal_type))+'Not supported')
            return False

    def preorder(self,start,traversal):
        if start:
            traversal+=(str(start.value)+'-')
            traversal=self.preorder(start.left,traversal)
            traversal=self.preorder(start.right,traversal)
        return traversal

    def inorder(self,start,traversal):
        if start:
            traversal=self.inorder(start.left,traversal)
            traversal+=(str(start.value)+'-')
            traversal=self.inorder(start.right,traversal)
        return traversal

    def postorder(self,start,traversal):
        if start:
            traversal=self.postorder(start.left,traversal)
            traversal=self.postorder(start.right,traversal)
            traversal+=(str(start.value)+"-")

        return traversal

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)


print(root.print_tree('postorder'))