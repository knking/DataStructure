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
# a=link.search(3)
# print(a)
# print(link.display())
#
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
#
# #l.dis()
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

class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class dlink:
    def __init__(self):
        self.head=None

    def append(self,data):
        new=node(data)
        if self.head ==None:
            self.head=new
            new.next=self.head
            self.head=new.prev
        else:
            temp=self.head
            while temp.next !=None:
                temp=temp.next
            temp.next=new
            new.prev=temp
            new.next=self.head
            self.head=n


    def dis(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

d=dlink()
d.append(10)
d.append(20)
d.append(30)
d.append(40)
d.append(50)

d.dis()


# ---------------------------Linled List Medium level---------

# 10) Nth node from end of linked list

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked:
    def __init__(self):
        self.head=None

    def append(self,data):
        new=node(data)
        if self.head==None:
            self.head=new

        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=new

    def nth_Node_from_end(self,key):
        count=0
        temp=self.head
        while temp.next !=None:
            temp=temp.next
            count +=1

        if  key > count :
            print("Location is greter than linked list")

        else:
            temp = self.head
            for i in range(0, count - key):
                temp = temp.next
            print(temp.data)

l=linked()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.nth_Node_from_end(3)


# 11) check the if the linked list is palindrom or not for STRING

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class slink:
    def __init__(self):
        self.head=None

    def appendElement(self,data):
        new=node(data)
        if self.head== None:
            self.head=new
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=new


    def palindromCheck(self,string):
        return (string==string[::-1])

    def isPalindrom(self):
        var=self.head
        lst=[]
        while var:
            lst.append(var.data)
            var=var.next
        string="".join(lst)
        return self.palindromCheck(string)

l=slink()
l.appendElement("a")
l.appendElement("b")
l.appendElement("c")
l.appendElement("b")
l.appendElement("a")
l.appendElement("c")
print("true" if l.isPalindrom() else "false")


# 11) Check linked list is palindrom or not For integer without using list or stack


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current


def is_palindrome(llist):
    start = llist.head
    end = llist.last_node
    while (start != end and end.next != start):
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True


a_llist = LinkedList()

data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))

if is_palindrome(a_llist):
    print('The linked list is palindromic.')
else:
    print('The linked list is not palindromic.')



# 11) Check linked list is palindrom or not for Integer using List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None

    def insert(self, data):
        newNode = Node(data)
        if self.first is None:
            self.first = newNode
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode

    def display(self):
        print("\nLinked List: ", end='')
        temp = self.first
        while temp is not None:
            print(temp.data, end='->')
            temp = temp.next

    def check_palindrome(self):
        stack = []
        temp = self.first
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        temp = self.first
        while temp is not None:
            popped = stack.pop()
            if temp.data == popped:
                temp = temp.next
            else:
                return False
        return True

l=LinkedList()
element =input("Enter element").split()

for data in element:
    l.insert(data)

l.display()

if l.check_palindrome():
    print("Linked list  is Panlidrom")

else:
    print("Linked list is not palindrom")

