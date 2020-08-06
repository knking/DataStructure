# #------------------------print("Welome in inkedList Section")------------------


#1) create a singly linked list class(members -> value and next pointer), with following methods
         # createNewNode()
         # addNewNodeBeg()
         # addnewNodeEnd()
         # length()
         # printFn()

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
# link=linkedlist()
# link.addInBeg("Name")
# link.append("krishna")
# link.append("nand")
# link.append("Roy")
# link.addInEnd(1)
# link.addInMid(link.head.next,"king")

# link.pri()
# print("\n")
# print(link.count())


#  2) create a method to search an element in above created linkend list
#
# class node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#
#     def display(self):
#         temp=self.head
#         while temp:
#             print(temp.value)
#             temp=temp.next
#
#     def append(self,value):
#         newNode=node(value)
#         if self.head==None:
#             self.head=newNode
#         else:
#             temp=self.head
#             while temp.next !=None:
#                 temp=temp.next
#             temp.next=newNode
#
#     def search(self,s):
#         temp=self.head
#         while temp:
#             if temp.value==s:
#                 return True
#             temp = temp.next
#         return False
#
# link=linkedlist()
# link.append(1)
# link.append(2)
# link.append(3)
# link.append(4)
# a=link.search(10)
# print(a)
# print(link.display())

#
# #3) create a method to delete any element in the linked list
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#
#     def deleteFirst(self):
#         self.head=self.head.next
#
#     def deleteAtPostion(self,key):
#         temp=self.head
#         if temp is not None:
#             if temp.data==key:
#                 self.head=temp.next
#                 #temp=None
#                 return
#         while temp is not None:
#             if temp.data==key:
#                 break
#
#             prev=temp
#             temp=temp.next
#         if temp==None:
#              return
#         prev.next=temp.next
#         temp=None

#     # def deleteInEnd(self):
#     #     last=self.head
#     #     while last.next is not None:
#     #         preNode=last
#     #         last=last.next
#     #     preNode.next=None
#
#     def apppend(self,data):
#         newNode=node(data)
#         if self.head== None:
#             self.head=newNode
#         else:
#             var=self.head
#             while var.next!=None:
#                 var=var.next
#             var.next=newNode
#
#     def addInBeg(self,beg):
#         new=node(beg)
#         new.next=self.head
#         self.head=new
#
#     def display(self):
#         var=self.head
#         while var:
#             print(var.data)
#             var=var.next
#
# link=linkedlist()
# link.apppend(0)
# link.apppend(9)
# link.apppend(6)
# link.apppend(3)
# link.apppend(4)
# link.apppend("Krishna")
# link.apppend(2)
#
# # link.addInBeg(6)
# #link.deleteFirst()
# #link.deleteInEnd()
# print(link.deleteAtPostion(2))
# #
# print(link.display())
#
#
# # 4) Create a method to provide a N'th Node from a linked list
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class Linked:
#     def __init__(self):
#         self.head=None
#
#     def element(self,position):
#         pos=0
#         temp=self.head
#         while temp:
#
#             if position==pos:
#                 return temp.data
#
#             temp=temp.next
#             pos+=1
#
#         else:
#             print("Not present in list")
#
#     def append(self,data):
#         new=Node(data)
#         if self.head==None:
#             self.head=new
#         else:
#             temp=self.head
#             while temp.next !=None:
#                 temp=temp.next
#             temp.next=new
#
#     def printLst(self):
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
# link=Linked()
# link.append(10)
# link.append(20)
# link.append(30)
# link.append(40)
# link.append(50)
# l=link.element(1)
# print(l)
# #print(link.printLst())
#
# # 5)Create  a method to count the number of specific value in the linked least
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linkedlist:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         newNode=node(data)
#         if self.head==None:
#             self.head=newNode
#         else:
#             t=self.head
#             while t.next != None:
#                 t=t.next
#             t.next=newNode
#
#     def countSpecific(self,num):
#         var=self.head
#         count=0
#         while var:
#             if var.data==num:
#                 count+=1
#             var=var.next
#         return count
#
#     def dis(self):
#         t=self.head
#         while t:
#             print(t.data)
#             t=t.next
#
# l=linkedlist()
# l.append(10)
# l.append(30)
# l.append(50)
# l.append(70)
# l.append(90)
# l.append(50)
# l.append(90)
# l.append(10)
# print(l.countSpecific(70))
#l.dis()
#
# print("Specific Number in linked List : ",l.countSpecific(90))
#
# # 6) Create a linked list and find a minimum and maximum number
#
# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
#
# class linked:
#     def __init__(self):
#         self.head=None
#
#     def appendData(self,value):
#         newNode=Node(value)
#
#         if self.head==None:
#             self.head=newNode
#         else:
#             temp=self.head
#             while temp.next!=None:
#                 temp=temp.next
#             temp.next=newNode
#
#     # def maximum(self):
#     #     temp=self.head
#     #     lst=[]
#     #     while temp:
#     #         lst.append(temp.value)
#     #         temp=temp.next
#     #     k=sorted(lst)
#     #     print(k[-1])
#
#     def maximum(self):
#         max=-30
#         temp=self.head
#         while temp:
#             if max < temp.value:
#                 max=temp.value
#             temp=temp.next
#         return max
#
#     def minimum(self):
#         temp=self.head
#         min=54637
#         while temp:
#             if min > temp.value:
#                 min=temp.value
#             temp=temp.next
#         return min
#
#     def display(self):
#         t=self.head
#         while t:
#             print(t.value)
#             t=t.next
# l=linked()
# l.appendData(20)
# l.appendData(30)
# l.appendData(40)
# l.appendData(50)
# l.appendData(60)
# #l.display()
# print(l.maximum())
# print(l.minimum())
#

# 7) Create a circular linked list

# class Node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None
#
# class linked:
#     def __init__(self):
#         self.head=None
#
#     def appendData(self,value):
#         newNode=Node(value)
#
#         if self.head==None:
#             self.head=newNode
#             newNode.next=self.head
#         else:
#             temp=self.head
#             while temp.next!=self.head:
#                 temp=temp.next
#             temp.next=newNode
#             newNode.next=self.head
#
#     def display(self):
#         t=self.head
#         while t:
#             print(t.value)
#             t=t.next
#             if t==self.head:
#                 break
#
# l=linked()
# l.appendData(20)
# l.appendData(30)
# l.appendData(40)
# l.appendData(50)
# l.appendData(60)
# l.display()

# 8) Create a doubly linked list and perform all above operation

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
#
#
# class dlink:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         new=node(data)
#
#         if self.head ==None:
#             self.head=new
#             new.prev=None
#         else:
#             temp=self.head
#             while temp.next !=None:
#                 temp=temp.next
#             temp.next=new
#             new.prev=temp
#             new.next=None
#
#     def prepend(self,data):
#         newNode=node(data)
#         if self.head ==None:
#             self.head=newNode
#             newNode.prev=None
#         else:
#             self.head.prev=newNode
#             newNode.next=self.head
#             self.head=newNode
#             newNode.prev=None
#
#     def dis(self):
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
# d=dlink()
# d.append(10)
# d.append(20)
# d.append(30)
# d.append(40)
# d.append(50)
# d.prepend(0)
# d.dis()

# 9) Create a doubly linked list and convert it into a double circular linked list

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.prev=None
#         self.next=None
#
# class dlink:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         new=node(data)
#         if self.head ==None:
#             self.head=new
#             new.next=self.head
#             self.head=new.prev
#         else:
#             temp=self.head
#             while temp.next !=None:
#                 temp=temp.next
#             temp.next=new
#             new.prev=temp
#             new.next=self.head
#             self.head=n
#
#
#     def dis(self):
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
# d=dlink()
# d.append(10)
# d.append(20)
# d.append(30)
# d.append(40)
# d.append(50)
#
# d.dis()

#
# # ---------------------------Linled List Medium level---------
#
# # 10) Nth node from end of linked list
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class linked:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         new=node(data)
#         if self.head==None:
#             self.head=new
#
#         else:
#             temp=self.head
#             while temp.next != None:
#                 temp=temp.next
#             temp.next=new
#
#     def nth_Node_from_end(self,key):
#         count=0
#         temp=self.head
#         while temp.next !=None:
#             temp=temp.next
#             count +=1
#
#         if  key > count :
#             print("Location is greter than linked list")
#
#         else:
#             temp = self.head
#             for i in range(0, count - key):
#                 temp = temp.next
#             print(temp.data)
#
# l=linked()
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# l.nth_Node_from_end(3)
#
#
# # 11) check the if the linked list is palindrom or not for STRING
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class slink:
#     def __init__(self):
#         self.head=None
#
#     def appendElement(self,data):
#         new=node(data)
#         if self.head== None:
#             self.head=new
#         else:
#             temp=self.head
#             while temp.next != None:
#                 temp=temp.next
#             temp.next=new
#
#
#     def palindromCheck(self,string):
#         return (string==string[::-1])
#
#     def isPalindrom(self):
#         var=self.head
#         lst=[]
#         while var:
#             lst.append(var.data)
#             var=var.next
#         string="".join(lst)
#         return self.palindromCheck(string)
#
# l=slink()
# l.appendElement("a")
# l.appendElement("b")
# l.appendElement("c")
# l.appendElement("b")
# l.appendElement("a")
# l.appendElement("c")
# print("true" if l.isPalindrom() else "false")
#
#
# # 11) Check linked list is palindrom or not For integer without using list or stack
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
#
#     def append(self, data):
#         if self.last_node is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
#
#     def get_prev_node(self, ref_node):
#         current = self.head
#         while (current and current.next != ref_node):
#             current = current.next
#         return current
#
#
# def is_palindrome(llist):
#     start = llist.head
#     end = llist.last_node
#     while (start != end and end.next != start):
#         if start.data != end.data:
#             return False
#         start = start.next
#         end = llist.get_prev_node(end)
#     return True
#
#
# a_llist = LinkedList()
#
# data_list = input('Please enter the elements in the linked list: ').split()
# for data in data_list:
#     a_llist.append(int(data))
#
# if is_palindrome(a_llist):
#     print('The linked list is palindromic.')
# else:
#     print('The linked list is not palindromic.')
#
#
#
# # 11) Check linked list is palindrom or not for Integer using List
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.first = None
#
#     def insert(self, data):
#         newNode = Node(data)
#         if self.first is None:
#             self.first = newNode
#         else:
#             temp = self.first
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = newNode
#
#     def display(self):
#         print("\nLinked List: ", end='')
#         temp = self.first
#         while temp is not None:
#             print(temp.data, end='->')
#             temp = temp.next
#
#     def check_palindrome(self):
#         stack = []
#         temp = self.first
#         while temp is not None:
#             stack.append(temp.data)
#             temp = temp.next
#
#         temp = self.first
#         while temp is not None:
#             popped = stack.pop()
#             if temp.data == popped:
#                 temp = temp.next
#             else:
#                 return False
#         return True
#
# l=LinkedList()
# element =input("Enter element").split()
#
# for data in element:
#     l.insert(data)
#
# l.display()
#
# if l.check_palindrome():
#     print("Linked list  is Panlidrom")
#
# else:
#     print("Linked list is not palindrom")


# 12) Create a program which reverse a linked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.first = None
#
#     def insert(self, data):
#         newNode = Node(data)
#         if self.first is None:
#             self.first = newNode
#         else:
#             temp = self.first
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = newNode
#
#     def reverse(self):
#         prev = None
#         current=self.first
#
#         while current:
#             next=current.next
#             current.next=prev
#             prev=current
#             current=next
#         self.first=prev
#
#     def display(self):
#         t=self.first
#         while t:
#             print(t.data)
#             t=t.next
#
#
# l=LinkedList()
# l.insert(10)
# l.insert(20)
# l.insert(30)
# l.insert(40)
# # print("Before reverse \n")
# # l.display()
# print("After reverse \n")
# l.reverse()
# l.display()


# 13) Reverse a linked list in a group of given size

# class Node:
#
#     # Constructor to initialize the node object
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     def reverse(self, head, k):
#         current = head
#         next = None
#         prev = None
#         count = 0
#
#         # Reverse first k nodes of the linked list
#         while (current is not None and count < k):
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#             count += 1
#
#         # next is now a pointer to (k+1)th node
#         # recursively call for the list starting
#         # from current. And make rest of the list as
#         # next of first node
#         if next is not None:
#             head.next = self.reverse(next, k)
#
#
#
#             # prev is new head of the input list
#
#         #print(prev.data," previous")
#         return prev
#
#         # Function to insert a new node at the beginning
#
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#         # Utility function to print the linked LinkedList
#
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data)
#             temp = temp.next
#
#
# # Driver program
# llist = LinkedList()
# llist.push(9)
# llist.push(8)
# llist.push(7)
# llist.push(6)
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)
#
#
# print(llist.printList())
#
#
# llist.head = llist.reverse(llist.head, 3)
# print(llist.printList())


# 14) Write a program to check loop in inked list

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.last_node = None
#
#     def append(self, data):
#         if self.last_node is None:
#             self.head = Node(data)
#             self.last_node = self.head
#         else:
#             self.last_node.next = Node(data)
#             self.last_node = self.last_node.next
#
#     def find_loop(self):
#
#         fast_ptr=self.head
#         slow_ptr=self.head
#
#         while fast_ptr and slow_ptr and fast_ptr.next:
#             slow_ptr=slow_ptr.next
#             fast_ptr=fast_ptr.next.next
#             if fast_ptr==slow_ptr:
#                 print("Loop found")
#                 return

#     def view(self):
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
#
# a_llist = LinkedList()
#
# data_list = input('Please enter the elements in the linked list: ').split()
# for data in data_list:
#     a_llist.append(int(data))
#
# a_llist.view()
#
# a_llist.head.next.next.next.next = a_llist.head
# a_llist.find_loop()

# 15) Write a program to find the length of loop in linked list

# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class linked:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         new=node(data)
#         if self.head==None:
#             self.head=new
#         else:
#             temp=self.head
#             while temp.next !=None:
#                 temp=temp.next
#             temp.next=new
#
#     def makeLoop(self,n):
#         loopNode=self.head
#         for i in range(1,n):
#             loopNode=loopNode.next
#
#         end=self.head
#
#         while end.next:
#             end=end.next
#         end.next=loopNode
#
#     def detectLoop(self):
#         if self.head is None:
#             return  0
#         slow=self.head
#         fast=self.head
#         while slow and fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#             if slow==fast:
#                 count=1
#                 slow=slow.next
#                 while slow !=fast:
#                     slow=slow.next
#                     count +=1
#                 return count
#         return 0
#
# mylnk=linked()
# mylnk.append(3)
# mylnk.append(6)
# mylnk.append(30)
# mylnk.append(32)
# mylnk.append(2)
# mylnk.append(5)
# mylnk.append(22)
# mylnk.append(9)
#
# mylnk.makeLoop(6)
#
# loopLength=mylnk.detectLoop()
#
# print(loopLength)
#
# if mylnk.head is None:
#     print("Linked list is empty")
# else:
#     print(str(loopLength))


# # 16) write a program to delete a linked list
#
# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
# class linked:
#     def __init__(self):
#         self.head=None
#
#     def append(self,data):
#         new=node(data)
#         if self.head==None:
#             self.head=new
#         else:
#             temp=self.head
#             while temp.next !=None:
#                 temp=temp.next
#             temp.next=new
#
#     def display(self):
#         temp=self.head
#         while temp:
#             print(temp.data)
#             temp=temp.next
#
#     def deleteLinkedList(self):
#         temp=self.head
#
#         # while temp:
#         #     self.head = temp.next
#         #     temp = None
#         #     temp = self.head
#         while temp:
#             prev=temp.next
#             del temp.data
#             temp=prev
#
# mylnk=linked()
# mylnk.append(3)
# mylnk.append(6)
# mylnk.append(30)
# mylnk.append(32)
# mylnk.append(2)
# mylnk.append(5)
# mylnk.append(22)
# mylnk.append(9)
#
# mylnk.display()
# print("After deletion ")
# mylnk.deleteLinkedList()
# mylnk.display()
# print("Node deleted")



class node:
    def __init__(self,value):
        self.value=value
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None

    def add_elemen(self,data):
        new=node(data)
        temp=self.head
        if self.head ==None:
            self.head=new
        else:
            while temp.next != None:
                temp=temp.next
            temp.next=new

    def countSpecificValue(self,val):
        temp=self.head
        count=0
        while temp.next !=None:
            if temp.value==val:
                count+=1
            temp = temp.next
        return count

    def display(self):
        temp=self.head
        while temp.next !=None:
            print(temp.value,"->",end=" ")
            temp=temp.next

l=linkedlist()
l.add_elemen(10)
l.add_elemen(20)
l.add_elemen(20)
l.add_elemen(20)
print(l.countSpecificValue(20))
l.display()

