##) Queue implementation using python

##1) Simple queue
# queue=[]
# def pus_queue(element):
#     queue.append(element)
#
# def pop_queue():
#     if len(queue) ==0:
#         print('queue is empty ')
#     else:
#         return queue.pop(0)
#
# def display_queue():
#     for i in range(len(queue)-1,-1,-1):
#         print(queue[i],end=" ")
#     print()
#
# pus_queue(10)
# pus_queue(20)
# pus_queue(30)
# pus_queue(40)
# pus_queue(50)
# display_queue()
# pop_queue()
# display_queue()
# pus_queue(100)
# display_queue()


##) queue implementaion using class

# class queue:
#
#     def __init__(self,limit=5):
#         self.que=[]
#         self.limit=limit
#         self.front=None
#         self.rear=None
#         self.size=0
#
#     def isEmpty(self):
#         self.size <=0
#
#     def enQueue(self,element):
#         if self.size >= self.limit:
#             print('Queue overflow')
#             return
#         else:
#             self.que.append(element)
#
#         if self.front is None:
#             self.front=self.rear=0
#         else:
#             self.rear=self.size
#         self.size +=1
#         print('Queue after enqueue',self.que)
#
#     def deQueue(self):
#         if self.size <=0:
#             print('Queue underflow')
#             return 0
#         self.que.pop(0)
#         self.size-=1
#         if self.size==0:
#             self.front= self.rear=None
#         else:
#             self.rear=self.size-1
#             print('Queue after deque',self.que)
#
#     def queueRear(self):
#         if self.rear is None:
#             print('Soerry the queue is empty')
#             raise IndexError
#         return self.que[self.front]
#     def queueFront(self):
#         if self.front is None:
#             print('Sorry, the queue is empty')
#             raise IndexError
#         return self.que[self.front]
#     def sizeOfQueue(self):
#         return self.size
#
# q=queue()
# q.enQueue(10)
# print('front',q.queueFront())
# print('rear',q.queueRear())
# q.enQueue(20)
# print('front',q.queueFront())
# print('rear',q.queueRear())
# q.enQueue(30)
# print('front',q.queueFront())
# print('rear',q.queueRear())
# print('Dequing',q.deQueue())
# print('front',q.queueFront())
# print('rear',q.queueRear())

# class queue:
#     def __init__(self):
#         self.arr=[]
#
#     def enQueue(self,item):
#         self.arr.append(item)
#
#     def deQueue(self):
#         self.arr.pop(0)
#
#     def fornt(self):
#         print(self.arr[0])
#
#     def display(self):
#         for i in range(len(self.arr)-1,-1,-1):
#             print(self.arr[i])
#             #print()
# q=queue()
# q.enQueue(10)
# q.enQueue(20)
# q.enQueue(30)
# q.enQueue(40)
# q.display()
# print('After deque')
# q.deQueue()
# q.display()

##2) Queue using stack

# ##enqueue operation is costly
# # Python3 program to implement Queue using
# # two stacks with costly enQueue()
#
# class queue:
#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#
#     def enQueue(self, x):
#
#         # Move all elements from s1 to s2
#         while len(self.s1) != 0:
#             self.s2.append(self.s1[-1])
#             self.s1.pop()
#
#         # Push item into self.s1
#         self.s1.append(x)
#
#         # Push everything back to s1
#         while len(self.s2) != 0:
#             self.s1.append(self.s2[-1])
#             self.s2.pop()
#
#         # Dequeue an item from the queue
#
#     def deQueue(self):
#
#         # if first stack is empty
#         if len(self.s1) == 0:
#             print("Q is Empty")
#
#         # Return top of self.s1
#         x = self.s1[-1]
#         self.s1.pop()
#         return x
#
#     # Driver code
# q = queue()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
#
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())

# # dequeue operation is costly
#
# class queue:
#     def __init__(self):
#         self.a1=[]
#         self.a2=[]
#
#     def enQueue(self,x):
#         self.a1.append(x)
#
#     def deQueue(self):
#
#         if len(self.a1)==0 and len(self.a2)==0:
#             print('Queue is empty')
#
#         if len(self.a2)==0:
#             while len(self.a1) !=0:
#                 self.a2.append(self.a1[-1])
#                 self.a1.pop()
#
#         x=self.a2[-1]
#         self.a2.pop()
#         return x
#
# q = queue()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
#
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())


## using recurion

# class queue:
#     def __init__(self):
#         self.a1=[]
#
#     def enQueue(self,x):
#         self.a1.append(x)
#
#     def deQueue(self):
#
#         if len(self.a1)<=0:
#             print('queue is empty')
#             return
#         x=self.a1[len(self.a1)-1]
#         self.a1.pop()
#
#         if len(self.a1) <=0:
#             return x
#
#         item=self.deQueue()
#         self.a1.append(x)
#         return item
#
#
# q = queue()
# q.enQueue(1)
# q.enQueue(2)
# q.enQueue(3)
#
# print(q.deQueue())
# print(q.deQueue())
# print(q.deQueue())


##3) Implement stack using queue

##Making push operation costly

# class stack:
#     def __init__(self):
#         self.q1=[]
#         self.q2=[]
#
#     def push(self,x):
#         while len(self.q1) !=0:
#             self.q2.append(self.q1[0])
#             self.q1.pop(0)
#
#         self.q1.append(x)
#
#         while len(self.q2) !=0:
#             self.q1.append(self.q2[0])
#             self.q2.pop(0)
#     def top(self):
#         if len(self.q1)==0:
#             return -1
#         return self.q1[0]
#
#     def popO(self):
#         if len(self.q1) ==0:
#             print('stackl is empty')
#
#         else:
#
#             x=self.q1[0]
#             self.q1.pop(0)
#             return x
#
# s=stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(50)
#
# print(s.popO())
# print(s.top())

##making pop operation costly
class stack:
    def __init__(self):
        self.a1=[]
        self.a2=[]

    def push(self,x):
        self.a1.append(x)
    def top(self):
        if len(self.a1)==0:
            print('Stack is empty')

        return self.a1[0]

    def popOperation(self):
        if len(self.a1)==0:
            print('Queue is empty')
        while len(self.a1) !=1:
            self.a2.append(self.a1[0])
            self.a1.pop(0)
        x=self.a1[0]
        self.a1.pop(0)
        return x

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.popOperation())
print(s.top())