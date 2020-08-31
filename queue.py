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

class queue:
    def __init__(self):
        self.arr=[]

    def enQueue(self,item):
        self.arr.append(item)

    def deQueue(self):
        self.arr.pop(0)

    def fornt(self):
        print(self.arr[0])

    def display(self):
        for i in range(len(self.arr)-1,-1,-1):
            print(self.arr[i])
            #print()
q=queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
q.display()
print('After deque')
q.deQueue()
q.display()
