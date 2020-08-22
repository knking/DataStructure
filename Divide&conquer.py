##)1 binary search

# def binearySarch(arr,key):
#     start=0
#     end=len(arr)-1
#     while start <=end:
#         mid=start+(end-start)//2
#
#         if arr[mid]==key:
#             return mid
#         elif arr[mid] > key:
#             end=mid-1
#         else:
#             start=mid+1
#     return -1
# arr=[1,3,6,9,23,45,68,77,87,98]
# key=98
# b=binearySarch(arr,key)
# if b==-1:
#     print('key not found ')
# else:
#     print('key found at index :',b)

##) using recursion

# def bsearch(arr,key,left,right):
#     if left-right==0:
#         return False
#     mid=(left+right)//2
#     if key==arr[mid]:
#         return True
#     if key < arr[mid]:
#         return bsearch(arr,key,left,mid)
#     else:
#         return bsearch(arr,key,mid+1,right)
#
# arr=[1,3,6,9,23,45,68,77,87,98]
# key=98
# if bsearch(arr,key,0,len(arr)-1):
#     print('Found')
# else:
#     print('Not found')

##2)merge sort

# def mergeSort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         l=arr[:mid]
#         r=arr[mid:]
#
#         mergeSort(l)
#         mergeSort(r)
#
#         i=j=k=0
#
#         while i < len(l) and j< len(r):
#             if l[i]<r[j]:
#                 arr[k]=l[i]
#                 i+=1
#
#             else:
#                 arr[k]=r[j]
#                 j+=1
#
#             k+=1
#         while i < len(l):
#             arr[k]=l[i]
#             i+=1
#             k+=1
#
#         while j < len(r):
#             arr[k]=r[j]
#             j+=1
#             k+=1
#
# def printarr(arr):
#     for i in range(len(arr)):
#         print(arr[i],end=' ')
#     print()
#
# arr=[12,11,13,5,6,7]
# print('Given array is ', end='\n')
# printarr(arr)
# mergeSort(arr)
# print('sorted array is :',end='\n')
# printarr(arr)

##3) square root of n

# def squareRoot(n,p):
#     start=0
#     end=n
#     ans=0
#
#     while start <= end:
#         mid = (start + end)//2
#         if mid**2 == n:
#             ans=mid
#             break
#         if mid**2 < n:
#             start=mid+1
#             #ans=mid
#         else:
#             end=mid-1
#fractonal part
#     incrment=0.1
#     for i in range(p):
#         while ans**2<=n:
#             ans+=incrment
#
#         ans=ans-incrment
#         incrment=incrment/10
#
#     return ans
# print(squareRoot(49,1))
# print(squareRoot(10,3))
# print(squareRoot(5,2))

##4) matrix median and mean

# def mean(matrix,n):
#     summ=0
#     for i in range(n):
#         for j in range(n):
#             summ+=matrix[i][j]
#     return summ /( n*n)
#
# matrix=[[1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12],
#         [13,14,15,16]]
# n=len(matrix)
# print(mean(matrix,n))
#
# def meadian(matrix,n):
#     if n%2 != 0:
#         return matrix[n//2][n//2]
#     if n%2==0:
#         return (matrix[(n-2)//2][n-1]+ matrix[n//2][0])/2
# print(meadian(matrix,n))

# #by using extend function we can convert a matrix into list using single loop
# l=[]
# for i in range(len(matrix)):
#     l.extend(matrix[i])
# print(l)

##5) Find the element that appears once in a sorted array and other element appears twice in sorted array
#brute force solution using inbuilt count method

ar=[1,1,2,2,3,3,4,4,5,5,6,7,7,8,8]
# for i in range(len(ar)):
#     s=ar.count(ar[i])
#     if s==1:
#         print(ar[i])
#         break

##Using hashing
# d={}
# for i in range(len(ar)):
#     if ar[i] in d:
#         d[ar[i]]+=1
#     else:
#         d[ar[i]]=1
# for k,v in d.items():
#     if v==1:
#         print(k)




