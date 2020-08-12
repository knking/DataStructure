##Hash implementation
# class HastTable:
#     def __init__(self):
#         self.MAX=100
#         self.arr=[None for i in range(self.MAX)]
#
#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
#
#     def __setitem__(self,key,value):
#         k=self.get_hash(key)
#         self.arr[k]=value
#
#     def __getitem__(self,key):
#         k=self.get_hash(key)
#         return self.arr[k]
#
#
# t=HastTable()
# t["march 6"]=130
# t["aprail 7"]=120
# t["may 8"]=140
# t["june 10"]=150
# t["july 12"]=160
# print(t["aprail 7"])

##1) Fidn first reapeting character
# s="abcade"
# size=len(s)
# for i in range(size):
#     for j in range(i+1,size):
#         if s[i]==s[j]:
#             print(s[j])
#             break
## using hashing

# def FirstRepeatedChar(str):
#     count=[0]*256
#     size=len(str)
#     for i in range(size):
#         if count[ord(str[i])]==1:
#             print(str[i])
#             break
#         else:
#             count[ord(str[i])]+=1
#     if i==size:
#         print("No repeated char")
#     return 0
# FirstRepeatedChar(["a","c","b","a","d","e","f","g","h","k"])

# class HashTable:
#     def __init__(self):
#         self.MAX=100
#         self.arr=[None for i in range(self.MAX)]
#     def getHash(self,key):
#         h=0
#         for i in key:
#             h+=ord(i)
#         return h % self.MAX
#     def add(self,key,value):
#         k=self.getHash(key)
#         self.arr[k]=value
#         #return self.arr
#
#     def get(self,key):
#         k = self.getHash(key)
#
#         return self.arr[k]
#
#
# table=HashTable()
# table.add("march 6",120)
# table.add("march 7",130)
# table.add("march 8",140)
# table.add("march 9",150)
# print(table.get("march 7"))

##)1remove deplicate

# def RemoveDuplicate(a):
#     m=0
#     for i in range(len(a)):
#         if not element(a,m,a[i]):
#             a[m]=a[i]
#             m+=1
#     return m
# def element(a,n,e):
#     for i in range(0,n):
#         if a[i]==e:
#             return 1
#     return 0
#a=[54,26,93,54,77,31,55,20]
# RemoveDuplicate(a)
# print(a)

##) using sorting
# def RemoveDuplicate(a):
#     a.sort()
#     j=0
#     for k in range(1,len(a)):
#         if a[j]!=a[k]:
#             j+=1
#             a[j]=a[k]
#     print(a[:j+1])
#a=[54,26,93,54,77,31,31,31,55,20]
#a=[31,31,31]
# RemoveDuplicate(a)

##)using hashing
#a=[1,2,3,'a','b','c',2,3,4,'b','c','d']
# helperSet=set()
# print(helperSet)
# lst=[]
# for x in a:
#     if x  not in lst:
#         lst.append(x)
#
# print(lst)

def checkElement(a1,a2):
    a1.sort()
    a2.sort()
    for i in range(0,len(a1)-1):
        if a1[i]!=a2[i]:
            return False

    return True

a1 = [54, 26, 93, 54, 77, 31, 31, 31, 55, 20]
a2 = [54, 26, 93, 540, 77, 31, 31, 31, 55, 20]
if checkElement(a1,a2):
    print("yes ")
else:
    print("not")