# ##1)binary tree
#
# # class node:
# #     def __init__(self,key):
# #         self.left=None
# #         self.right=None
# #         self.value=key
# #
# # root=node(1)
# # root.right=node(2)
# # root.left=node(3)
# # root.right.right=node(4)
#
# ##2)Binary tree(inorder,preorder,postorder)
#
# class Node(object):
#     def __init__(self,value):
#         self.left=None
#         self.right=None
#         self.value=value
#
# # class BinaryTree(object):
# #     def __init__(self,root):
# #         self.root=Node(root)
#
#
#     def print_tree(self,traversal_type):
#         if traversal_type=='preorder':
#             return self.preorder(root,'')
#         elif traversal_type=='inorder':
#             return self.inorder(root,'')
#         elif traversal_type=='postorder':
#             return self.postorder(root,'')
#         else:
#             print('Traversal type'+(str(traversal_type))+'Not supported')
#             return False
#
#     def preorder(self,start,traversal):
#         if start:
#             traversal+=(str(start.value)+'-')
#             traversal=self.preorder(start.left,traversal)
#             traversal=self.preorder(start.right,traversal)
#         return traversal
#
#     def inorder(self,start,traversal):
#         if start:
#             traversal=self.inorder(start.left,traversal)
#             traversal+=(str(start.value)+'-')
#             traversal=self.inorder(start.right,traversal)
#         return traversal
#
#     def postorder(self,start,traversal):
#         if start:
#             traversal=self.postorder(start.left,traversal)
#             traversal=self.postorder(start.right,traversal)
#             traversal+=(str(start.value)+"-")
#
#         return traversal
#
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
#
# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)

# #print(tree.print_tree('preorder'))
# #print(tree.print_tree('inorder'))
# print(root.print_tree('postorder'))

##3) level order traversal

# class Queue:
#     def __init__(self):
#         self.items=[]
#
#     def enqueue(self,data):
#         self.items.insert(0,data)
#
#     def dequeue(self):
#         if not self.isEmpty():
#             return self.items.pop()
#
#     def isEmpty(self):
#         return len(self.items)==0
#
#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1].value
#
#     def __len__(self):
#         return self.size()
#
#     def size(self):
#         return len(self.items)
#
#
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None
#
#     def levelorder(self,start):
#         if start is None:
#             return
#         queue=Queue()
#         queue.enqueue(start)
#
#         traversal=''
#         while len(queue)>0:#(first print then dqueue)
#             traversal+=str(queue.peek())+'-'
#             node=queue.dequeue()
#
#             if node.left:
#                 queue.enqueue(node.left)
#             if node.right:
#                 queue.enqueue(node.right)
#
#         return traversal
#
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
#
# print(root.levelorder(root))

##4) reverse level order

class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items)==0

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()

# class Queue:
#     def __init__(self):
#         self.items=[]
#
#     def enqueue(self,data):
#         self.items.insert(0,data)
#
#     def dequeue(self):
#         if not self.isEmpty():
#             return self.items.pop()
#
#     def isEmpty(self):
#         return len(self.items)==0
#
#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1].value
#
#     def __len__(self):
#         return self.size()
#
#     def size(self):
#         return len(self.items)

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None
#
#
#     def reverse_levelOrder(self,start):
#         if Stack is None:
#             return
#         queue=Queue()
#         stack=Stack()
##(First enque in queue then deque from queue and push it into stack
#         queue.enqueue(start)
#         traversal=''
#
#         while len(queue) > 0:
#             node=queue.dequeue()
#             stack.push(node)
#
#             if node.right:
#                 queue.enqueue(node.right)
#
#             if node.left:
#                 queue.enqueue(node.left)
###(here pop from stack and store it into answer)

#         while len(stack) >0:
#             node=stack.pop()
#             traversal+=str(node.value)+'-'
#         return traversal
#
#
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
#
# print(root.reverse_levelOrder(root))

##)5 Height of binary tree

class Node:

    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

# class BinaryTree:
#     def __init__(self,root):
#         self.root=Node(root)

    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)

        return 1+ max(left_height,right_height)

    def size_of_tree(self,root):
        if root is None:
            return 0

        stack=Stack()
        stack.push(root)
        size=1

        while stack:
            node=stack.pop()
            if node.left:
                size+=1
                stack.push(node.left)

            if node.right:
                size+=1
                stack.push(node.right)

        return size

    def size_of_tree_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.size_of_tree_recursive(node.left) + self.size_of_tree_recursive(node.right)


# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(8)
root.right.right.left.left=Node(9)

print(root.size_of_tree(root))
print(root.size_of_tree_recursive(root))