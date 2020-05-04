# #------------------------print("Welome in inkedList Section")------------------
#
# #1) create a singly linked list class(members -> value and next pointer), with following methods
#          # createNewNode()
#          # addNewNodeBeg()
#          # addnewNodeEnd()
#          # length()
#          # printFn()

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class linkedlist:
#     def __init__(self):
#         self.head=None
#
#     def pri(self):
#         temp=self.head
#         while temp :
#             print(temp.data,"-->",end=" ")
#             temp=temp.next
#
#
#     def count(self):        #length of linkedlist----------
#         temp=self.head
#         count=0
#         while temp:
#             count+=1
#             temp=temp.next
#         return count
#
#
#     def addInBeg(self,beg):      #add node in beg----------------
#         new=node(beg)
#         new.next=self.head
#         self.head=new
#
#     def addInEnd(self,end):      #add in end-----------
#         endNode=node(end)
#         if self.head==None:
#             self.head=endNode
#         else:
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next=endNode
#
#     def addInMid(self,prev,mid):        #add in mid---------------
#         midNode=node(mid)
#         midNode.next=prev.next
#         prev.next=midNode
#
#     def append(self,data):               #add element in linked list------------
#         new_node=node(data)
#         if self.head==None:
#             self.head=new_node
#         else:
#             temp=self.head
#             while temp.next != None:
#                 temp=temp.next
#             temp.next=new_node
#
#
#
#
#
# link=linkedlist()
# link.addInBeg("Name")
# link.append("krishna")
# link.append("nand")
# link.append("Roy")
# link.addInEnd(1)
# link.addInMid(link.head.next,"king")
#
# link.pri()
# print("\n")
# print(link.count())
#



#  2) create a method to search an element in above created linkend list


class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        newNode=node(value)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next !=None:
                temp=temp.next
            temp.next=newNode

    def search(self,s):
        temp=self.head
        while temp:

            if temp.value==s:
                return True
            temp = temp.next

        return False

link=linkedlist()
link.append(1)
link.append(2)
link.append(3)
link.append(4)
a=link.search(3)
print(a)
print(link.display())



