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
#         return bsearch(arr,key,left,mid-1)
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

#ar=[1,1,2,2,3,3,4,4,5,5,6,7,7,8,8]
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

##using xor
# ans=ar[0]
# for i in range(1,len(ar)):
#     ans=ans ^ ar[i]
# print(ans)

##using bineary search

# def binarySearch(ar,low,high):
#
#     if low > high:
#         return None
#     if low== high:
#         return ar[low]
#
#     mid=low+(high-low)//2
#
#     if mid % 2==0:
#         if ar[mid]==ar[mid+1]:
#             return binarySearch(ar,mid+2,high)
#         else:
#             return binarySearch(ar,low,mid)
#
#     else:
#         if ar[mid]==ar[mid-1]:
#             return binarySearch(ar,mid+1,high)
#         else:
#             return binarySearch(ar,low,mid-1)
#
# ar=[1,1,2,4,4,5,5,6,6]
# result=binarySearch(ar,0,len(ar)-1)
# if result is not None:
#     print(' the required element is :',result)
# else:
#     print('invilid array')

# def singleNonDup(nums):
#     left=0
#     right=len(nums)-1
#     while left < right:
#         mid=left + (right-left)//2
#         check_halves=(right-mid) % 2==0
#         if nums[mid+1]==nums[mid]:
#             if check_halves:
#                 left=mid+2
#             else:
#                 right=mid-1
#         elif nums[mid-1]==nums[mid]:
#             if check_halves:
#                 right=mid-2
#             else:
#                 left=mid+1
#         else:
#             return nums[mid]
#     return nums[left]
#
# nums=[1,1,2,2,3,3,4,4,5,5,6,7,7,8,8]
# print(singleNonDup(nums))

##6) search element in sorted and rotatd array

# def search(ar,start,end,key):
#     if start> end:
#         return -1
#     mid=(start+end)//2
#
#     if ar[mid]==key:
#         return mid
#     if ar[start]<=ar[mid]:
#         if key >= ar[start] and key <= ar[mid]:
#             return search(ar,start,mid-1,key)
#         return search(ar,mid+1,end,key)
#
#     if key >= ar[mid] and key <= ar[end]:
#         return search(ar,mid+1,end,key)
#     return search(ar,start,mid-1,key)
#
# ar=[5, 6, 7, 8, 9, 10, 1, 2, 3]
# print('found at index :',search(ar,0,len(ar)-1,0))

##)7 finding first and last occurances
##)first
# def firstOccurence(arr,key):
#     start=0
#     end=len(arr)-1
#     result=-1
#     while start <= end:
#         mid =(start+end)//2
#
#         if arr[mid]==key:
#             result=mid
#             end=mid-1
#         elif key > arr[mid]:
#             start=mid+1
#         else:
#             end=mid-1
#
#     return result
# arr=[2,3,4,6,7,7,7,8,9,20]
# key=7
# print('First occurance of ',key,'is :',firstOccurence(arr,key))

##)Last occurances
# def lastOccurence(arr,key):
#     start=0
#     end=len(arr)-1
#     result=-1
#     while start <= end:
#         mid =(start+end)//2
#
#         if arr[mid]==key:
#             result=mid
#             start=mid+1
#         elif key > arr[mid]:
#             start=mid+1
#         else:
#             end=mid-1
#
#     return result
# arr=[2,3,4,6,7,7,7,7,8,9,20]
# key=7
# print('First occurance of ',key,'is :',lastOccurence(arr,key))

##8)Count number of occurence

# def binarySearch(arr,key,search=bool):
#     start=0
#     end=len(arr)-1
#     result=-1
#     while start <= end:
#         mid =(start+end)//2
#
#         if arr[mid]==key:
#             result=mid
#             if search:
#                 end=mid-1
#             else:
#                 start=mid+1
#         elif key > arr[mid]:
#             start=mid+1
#         else:
#             end=mid-1
#
#     return result
# arr=[2,3,4,6,7,7,7,7,8,9,20]
# key=2
# firstIndex=binarySearch(arr,key,True)
# if firstIndex==-1:
#     print('Count of ',key,'is 0')
#
# else:
#     lastIndex=binarySearch(arr,key,False)
#     print('Count of ',key,'is :', lastIndex-firstIndex+1)

##9) K- th element of two sorted array
#Brute force approach

# def kth(arr1, arr2, m, n, k):
#     sorted1 = [0] * (m + n)
#     i = 0
#     j = 0
#     d = 0
#     while (i < m and j < n):
#
#         if (arr1[i] < arr2[j]):
#             sorted1[d] = arr1[i]
#             i += 1
#         else:
#             sorted1[d] = arr2[j]
#             j += 1
#         d += 1
#
#     while (i < m):
#         sorted1[d] = arr1[i]
#         d += 1
#         i += 1
#     while (j < n):
#         sorted1[d] = arr2[j]
#         d += 1
#         j += 1
#     return sorted1[k - 1]
# # driver code
# arr1 = [2, 3, 6, 7, 9]
# arr2 = [1, 4, 8, 10]
# k = 7
# print(kth(arr1, arr2, 5, 4, k))

