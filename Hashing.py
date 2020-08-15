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
#Brute force approach
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

##) using sorting for duplicating
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

##)using hashing for removing duplicate

#a=[1,2,3,'a','b','c',2,3,4,'b','c','d']
# helperSet=set()
# print(helperSet)
# lst=[]
# for x in a:
#     if x  not in lst:
#         lst.append(x)
#
# print(lst)

# def checkElement(a1,a2):
#     a1.sort()
#     a2.sort()
#     for i in range(0,len(a1)-1):
#         if a1[i]!=a2[i]:
#             return False
#
#     return True
#
# a1 = [54, 26, 93, 54, 77, 31, 31, 31, 55, 20]
# a2 = [54, 26, 93, 540, 77, 31, 31, 31, 55, 20]
# if checkElement(a1,a2):
#     print("yes ")
# else:
#     print("not")

##3)Find whether an array is subset of another array

# def subset(ar1,ar2):
#     for i in range(len(ar2)):
#         for j in range(len(ar1)):
#             if ar2[i]==ar1[j]:
#                 break
#         if j==len(ar1)-1:
#             return 0
#     return 1
# ar1 = [11, 1, 13, 21, 3, 7]
# ar2 = [110, 30, 70, 10]
# if subset(ar1,ar2):
#     print("arr2 is subset of arr1")
# else:
#     print("arr2 is not subset of arr1")

##4)Given two arrays of unordered numbers, check whether both arrays have the same set of numbers

# def checkSameSet(ar1,ar2):
#     hashmap={}
#     n=len(ar1)
#     m=len(ar2)
#     if n!=m:
#         return False
# ##Store arr1[] elements and their counts in hash map
#     for i in range(n):
#         if ar1[i] in hashmap.keys():
#             hashmap[ar1[i]]=hashmap[ar1[i]]+1
#         else:
#             hashmap[ar1[i]]=1
#
# ##Scan the all element of B
#     for i in range(n):
#         if ar2[i] not in hashmap.keys():
#             return False
#         if hashmap[ar2[i]]==0:
#             return False
#         hashmap[ar2[i]]=hashmap[ar2[i]]-1
#
#     return True
# #A = [2, 5, 6, 8, 10, 2, 2]
# #B = [2, 5, 5, 6, 8, 5, 6]
# # A = [2, 5, 6, 8, 2, 10, 2]
# # B = [2, 5, 6, 8, 2, 10, 2]
# A = [2, 5, 8, 6, 10, 2, 2]
# B = [2, 5, 6, 8, 2, 10, 2]
# print(checkSameSet(A,B))

##5)given a list of number pairs if pair(i,j) exists and pair(j,i)exits, report all such pairs
# def demo(lst):
#
# #lst={{1,3},{2,6},{7,4},{5,3},{8,7},{3,5}}
#     dic={}
#     for i in range (len(lst)):
#         if lst[i][1] in dic.keys() and dic[lst[i][1]]==lst[i][0]:
#             print("(", lst[i][1],",",lst[i][0], ")")
#         else:
#             dic[lst[i][0]]=lst[i][1]
#
# lst=[[1,3],[2,6],[7,4],[5,3],[8,7],[3,5]]
# print(demo(lst))

##6) 2 sum problem using hashig(i this we have to return indices of element whos sum is equal to the given target)
##example- nums=[2,7,11,15], target=9

# def twoSum(lst,target):
#     dic={}
#     for i in range(len(lst)):
#         if lst[i] in dic:
#             return dic[lst[i]],i
#         else:
#             dic[target-lst[i]]=i
# target=10
# lst=[1,2,3,5,5]
# print(twoSum(lst,target))

##7) 4 sum problem using hashing
##brute force apporach
# def fourSum(target,arr):
#     n=len(arr)
#     arr.sort()
#     for i in range(0,n-3):
#         for j in range(i+1,n-2):
#             left=j+1
#             right=n-1
#
#             while(left< right):
#                 if arr[i]+arr[j]+arr[left]+arr[right]==target:
#                     print(arr[i],arr[j],arr[left],arr[right])
#                     left=left+1
#                     right=right-1
#                 elif arr[i]+arr[j]+arr[left]+arr[right]< target:
#                     left=left+1
#                 else:
#                     right=right-1
#
#
# a=[10,2,3,4,5,9,7,8]
# tar=23
# fourSum(tar,a)

##)using hasing
# A hashing based Python program to find if there are
# four elements with given summ.
# The function finds four elements with given summ X
# def findFourElements(arr, n, X):
#     # Store summs of all pairs in a hash table
#     mp = {}
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             mp[arr[i] + arr[j]] = [i, j]
#
#         # Traverse through all pairs and search
#         #for X - (current pair summ):
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             summ = arr[i] + arr[j]
#             #If X - summ is present in hash table,
#             if (X - summ) in mp:
#
#                 # Making sure that all elements are
#                 # distinct array elements and an element
#                 # is not considered more than once.
#                 p = mp[X - summ]
#                 if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
#                     print(arr[i], ", ", arr[j], ", ", arr[p[0]], ", ", arr[p[1]], sep="")
#                     return
#
# # Driver code
# arr = [10, 20, 30, 40, 1, 2]
# n = len(arr)
# X = 91
# print(findFourElements(arr, n, X))

##8)longest consecutive sequence
##busing hasing 

def logest(ar,n):
    s=set()
    ans=0
    for e in ar:
        s.add(e)

    for i in range(n):
        if (ar[i]-1) not in s:
            j=ar[i]

            while j in s:
                j+=1
            ans=max(ans,j-ar[i])
    return ans

ar=[100,4,200,1,3,2]
n=len(ar)
print(logest(ar,n))