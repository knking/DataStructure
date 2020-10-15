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
# ##2)Binary tree(inorder,preorder,postorder recursive)
#
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
#
# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)

##print(root.print_tree('preorder'))
##print(root.print_tree('inorder'))
print(root.print_tree('postorder'))

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

# class Stack:
#     def __init__(self):
#         self.items=[]
#
#     def push(self,item):
#         self.items.append(item)
#
#     def pop(self):
#         if not self.isEmpty():
#             return self.items.pop()
#
#     def isEmpty(self):
#         return len(self.items)==0
#
#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#     def __len__(self):
#         return self.size()

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

# class Node:
#
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None
#
# # class BinaryTree:
# #     def __init__(self,root):
# #         self.root=Node(root)
#
#     def height(self,node):
#         if node is None:
#             return -1
#         left_height=self.height(node.left)
#         right_height=self.height(node.right)
#
#         return 1+ max(left_height,right_height)
#
#     def size_of_tree(self,root):
#         if root is None:
#             return 0
#
#         stack=Stack()
#         stack.push(root)
#         size=1
#
#         while stack:
#             node=stack.pop()
#             if node.left:
#                 size+=1
#                 stack.push(node.left)
#
#             if node.right:
#                 size+=1
#                 stack.push(node.right)
#
#         return size
#
#     def size_of_tree_recursive(self,node):
#         if node is None:
#             return 0
#         return 1 + self.size_of_tree_recursive(node.left) + self.size_of_tree_recursive(node.right)


# tree=BinaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)

# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
# root.right.right.left=Node(8)
# root.right.right.left.left=Node(9)
#
# print(root.size_of_tree(root))
# print(root.size_of_tree_recursive(root))

##)6 inorder,preorder and postorder traversal itetrtative

# class Node:
#     def __init__(self,value):
#         self.left=None
#         self.right=None
#         self.value=value
#
# class binaryTree:
#     def __init__(self,root):
#         self.root=Node(root)
#
#     def preorder_iterative(self,start,result):
#         if not start:
#             return
#         stack=[]
#         stack.append(start)
#         while stack:
#             node=stack.pop()
#             result.append(node.value)
#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)
#         return result
#
#     def inorder_iterative(self,start,result):
#         if not start:
#             return
#         stack=[]
#         node=start
#         while stack or node:
#             if node:
#                 stack.append(node)
#                 node=node.left
#             else:
#                 node=stack.pop()
#                 result.append(node.value)
#                 node=node.right
#
#         return result
#
#     # def postorder_traversal(self,start,result):
#     #     if not start:
#     #         return
#     #     stack=[]
#     #     stack.append(start)
#     #
#     #     while stack:
#
#
# s=[]
# tree=binaryTree(1)
# tree.root.left=Node(2)
# tree.root.right=Node(3)
# tree.root.left.left=Node(4)
# tree.root.left.right=Node(5)
# tree.root.right.left=Node(6)
# tree.root.right.right=Node(7)
# #print(tree.preorder_iterative(tree.root,s))
# print(tree.inorder_iterative(tree.root,s))

##7) Left view of a binary tree
# class Queue:
#     def __init__(self):
#         self.items=[]
#
#     def enqueue(self,data):
#         self.items.insert(0,data)
#
#     def dequeue(self):
#         if not self.isEmpty():
#             return self.items.pop(0)
#     def peek(self):
#         if not self.isEmpty():
#             return self.items[-1].value
#
#     def isEmpty(self):
#         return len(self.items)==0
#
#     def __len__(self):
#         return self.size()
#
#     def size(self):
#         return len(self.items)
#
# class Node:
#     def __init__(self,value):
#         self.left =None
#         self.right=None
#         self.value=value

    # def leftview_recursive(self,root,level,max_level):
    #     if root!=None:
    #         if max_level[0] < level:
    #             print(root.value)
    #             max_level[0]=level
    #
    #         self.leftview_recursive(root.left,level+1,max_level)
    #         self.leftview_recursive(root.right,level+1,max_level)

    # def rightview_recurisive(self,root,level,max_level):
    #     if root!=None:
    #         if max_level[0] < level:
    #             print(root.value)
    #             max_level[0]=level
    #
    #         self.rightview_recurisive(root.right,level+1,max_level)
    #         self.rightview_recurisive(root.left,level+1,max_level)

#     def rightView_iter(self,start):
#         if not start:
#             return
#         q=[]
#         q.append(start)
#
#         while len(q):
#             n=len(q)
#
#             for i in range(1,n+1):
#                 temp=q[0]
#                 q.pop(0)
#
#                 if i==n:
#                     print(temp.value,end=' ')
#
#                 if temp.left !=None:
#                     q.append(temp.left)
#
#                 if temp.right !=None:
#                     q.append(temp.right)
#
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.left=Node(4)
# root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
# root.right.left.right=Node(8)

#max_level=[0]
# root.leftview_recursive(root,1,max_level)
#root.rightview_recurisive(root,1,max_level)
# root.rightView_iter(root)
#print(root.leftViewIter(root))
##8) Sum of binary tree
# class Node:
#     def __init__(self,value):
#         self.left=None
#         self.right=None
#         self.value=value
#
#     def sum_of_node(self,node):
#         if node is None:
#             return 0
#         left_sum=self.sum_of_node(node.left)
#         right_sum=self.sum_of_node(node.right)
#         total_sum=left_sum + right_sum + node.value
#
#         return total_sum
#
#     def max_in_node(self,node):
#         if node is None:
#             return -1
#         left_max=self.max_in_node(node.left)
#         right_max=self.max_in_node(node.right)
#         maximum=max(node.value,left_max,right_max)
#
#         return maximum
#
# root=Node(1)
# root.left=Node(2)
# root.right=Node(3)
# root.left.right=Node(4)
# root.right.left=Node(5)
# root.right.left.right=Node(6)
# root.right.left.right.left=Node(8)
# root.right.left.right.right=Node(7)
# #print(root.sum_of_node(root))
# print(root.max_in_node(root))

##9)Vertical order traversal

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#
#
# def vertical_order(root):
#     if root is not None:
#         dict={}
#         node_dict={}
#         que=list()
#         que.append(root)
#         node_dict[root.data]=0
#         while len(que) >0:
#             temp=[]
#             cur=que.pop(0)
#             if cur is not None:
#                 level=node_dict[cur.data]
#                 if level in dict:
#                     temp=dict.get(level)
#                     temp.append(cur.data)
#                 else:
#                     temp.append(cur.data)
#                     dict[level]=temp
#
#                 if cur.left is not None:
#                     left_node=cur.left
#                     que.append(left_node)
#                     node_dict[left_node.data]=node_dict[cur.data]-1
#
#                 if cur.right is not None:
#                     right_node=cur.right
#                     que.append(right_node)
#                     node_dict[right_node.data]=node_dict[cur.data]+1
#         print(dict)
#
# root=Node('a')
# root.left=Node('b')
# root.right=Node('c')
# root.left.left=Node('d')
# root.left.right=Node('e')
#
# vertical_order(root)

##10)bottom view of binary tree

# def bottom_view(root):
#     ansDict={}
#     nodes_dict={}
#     queue=list()
#     queue.append(root)
#     nodes_dict[root.data]=0
#
#     while len(queue) >0:
#         var=[]
#         current=queue.pop(0)
#
#         if current is not None:
#             level=nodes_dict[current.data]
#             if level in ansDict:
#                 var=ansDict.get(level)
#                 var.clear()
#                 var.append(current.data)
#             else:
#                 var.append(current.data)
#                 ansDict[level]=var
#             if current.left is not None:
#                 queue.append(current.left)
#                 nodes_dict[current.left.data]=nodes_dict[current.data]-1
#
#             if current.right is not None:
#                 queue.append(current.right)
#                 nodes_dict[current.right.data]=nodes_dict[current.data]+1
#
#     print(ansDict)
#
# root=Node('a')
# root.left=Node('b')
# root.right=Node('c')
# root.left.left=Node('d')
# root.left.right=Node('e')

#bottom_view(root)

##11) Diameter of a binary tree
class Node:
    ptr=0
    def __init__(self,value):
        self.left =None
        self.right=None
        self.value=value
#     def diameter(self,root):
#         if root is None:
#             return 0
#
#         left_height=self.height(root.left)
#         right_height=self.height(root.right)
#
#         ldiameter=self.diameter(root.left)
#         rdiameter=self.diameter(root.right)
#
#         return max(left_height+right_height,max(ldiameter,rdiameter))
#
#     def height(self,root):
#         if root is None:
#             return 0
#
#         return 1 + max(self.height(root.left+1),self.height(root.right))
    def diameterOfTree(self,node):
        global ptr
        if not node:
            return 0
        left=self.diameterOfTree(node.left)
        right=self.diameterOfTree(node.right)
        if left+right > ptr:
            ptr=left+right
        return max(left,right)+1

#
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
# root.right.left=Node(6)
# root.right.right=Node(7)
# root.right.left.right=Node(8)
# print(root.diameter(root))
#print(root.diameterOfTree(root))

##12) print K levels Down

# def kLevelsDown(node,k):
#     if node is None or k <0:
#         return
#     if k==0:
#         print(node.value,end=' ')
#     kLevelsDown(node.left,k-1)
#     kLevelsDown(node.right,k-1)
# kLevelsDown(root,2)
