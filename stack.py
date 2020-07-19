# # 1) Create a stack and perform operations
#         # push()
#         #pop()
#         #peek()
#         # empty()
#         # Search()
#
#
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


# 2) Reverse a string using stack

def createStack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    if size(stack) == 0:
        return True

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)

    stack = createStack()

    for i in range(0, n, 1):
        push(stack, string[i])

    string = ""

    for i in range(0, n, 1):
        string += pop(stack)
    return string

string = "GeeksQuiz"
string = reverse(string)
print("Reversed string is " + string)