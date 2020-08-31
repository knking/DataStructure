# # 1) Create a stack and perform operations
#         # push()
#         #pop()
#         #peek()
#         # empty()
#         # Search()
# class stack:
#     def __init__(self):
#         self.items=[]
#
#     def push(self,item):
#         return self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def get_item(self):
#         for i in range(len(s.items)-1,-1,-1):
#             print(s.items[i])
#
#     def search(self,value):
#         for i in (range(len(s.items))):
#             if s.items[i]==value:
#                 print("Found at ",i)
#                 break
#         else:
#             print("Not Found ")
#
#     def empty(self):
#         if len(s.items)<= 0:
#             print(" Stack is Empty")
#         else:
#             print("Not Empty")
#
# s=stack()
# s.push("Name")
# s.push("krishna")
# s.push("Nand")
# s.push("Roy")
# s.push(2)
# s.push(5)
# s.pop()
#
# s.get_item()
# s.empty()
# s.search("Roy")


# # 2) Reverse a string using stack
#
# def createStack():
#     stack = []
#     return stack
#
# def size(stack):
#     return len(stack)
#
# def isEmpty(stack):
#     if size(stack) == 0:
#         return True
#
# def push(stack, item):
#     stack.append(item)
#
# def pop(stack):
#     if isEmpty(stack):
#         return
#     return stack.pop()
#
# def reverse(string):
#     n = len(string)
#
#     stack = createStack()
#
#     for i in range(0, n, 1):
#         push(stack, string[i])
#
#     string = ""
#
#     for i in range(0, n, 1):
#         string += pop(stack)
#     return string
#
# string = "GeeksQuiz"
# string = reverse(string)
# print("Reversed string is " + string)

# a=[]
# def stackPush(element):
#     return a.append(element)
#
# def stackPop():
#     if len(a)> 0:
#         return a.pop()
#     else:
#         print(" Stack is empty")
#
# def display():
#     for i in range(len(a)-1,-1,-1):
#         print(a[i])
#
# def search(value):
#     for i in range(len(a)):
#         if a[i]==value:
#             print("Found at index :",i)
#             break
#     else:
#         print("Not Found")
# def checkEmpty():
#     if len(a)<=0:
#         print("Stack is empty")
#     else:
#         print("Stack is not empty")
#
# def reverse(string):
#     n=len(string)
#
# stackPush(10)
# stackPush(20)
# stackPush("k")
# #stackPop()
# search("kn")
# checkEmpty()
# display()

##reverse string
# stack=[]
# def reverseString(string):
#     for i in range(len(string)):
#         stack.append(string[i])
#     s=''
#     for i in range(len(string)):
#         s+=stack.pop()
#     return s
# string='good'
# print(reverseString(string))

##4) Valid paranthesis

#def valisParinthesis(expre):
#     stack=[]
#     for char in expre:
#         if char in ["(", "{", "["]:
#             stack.append(char)
#         #else conditon check here for closing element i.e. if stack contain only closing parantehsins the it will give run time error
#         #so to avoid runtime error we use here check condition for stack
#         else:
#             if not stack:
#                 return False
#             current_char=stack.pop()
#             if current_char=='(':
#                 if char!=')':
#                     return False
#             if current_char=='{':
#                 if char!='}':
#                     return False
#             if current_char=='[':
#                 if char!=']':
#                     return False
#     if stack:
#         return False
#     return True
# expre="{()}[]"
# if valisParinthesis(expre):
#     print('Paranthesis is balanced :')
# else:
#     print('Not a valid paranthesis')

##5) implement two stack in single array

# Python Script to Implement two stacks in a list
class twoStacks:

    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

    # Method to push an element x to stack1
    def push1(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

        # Method to push an element x to stack2

    def push2(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
        exit(1)

    # Method to pop an element from first stack
    def pop1(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

        # Method to pop an element from second stack

    def pop2(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()

        # Driver program to test twoStacks class
ts = twoStacks(5)
ts.push1(5)
ts.push2(10)
ts.push2(15)
ts.push1(11)
ts.push2(7)

print("Popped element from stack1 is " + str(ts.pop1()))
# ts.push2(40)
# print("Popped element from stack2 is " + str(ts.pop2()))

