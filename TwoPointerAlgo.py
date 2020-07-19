
# 3) Remove Duplicates from Sorted Array
# 4)Remove Duplicates from Sorted Array
#
# Given a sorted array,
# remove the duplicates in place such that each element can appear atmost twice and return the new length.
#
# # 1) Given two sorted integer arrays A and B, merge B into A as one sorted array
# def merge(A,B):
#     i,j=0,0
#     while i < len(A) and j< len(B):
#         if A[i] <= B[j]:
#             i+=1
#         else:
#             A.insert(i,B[j])
#             i+=1
#             j+=1
#     if i==len(A):
#         while j < len(B):
#             A.insert(i,B[j])
#             i+=1
#             j+=1
#     return A
# A=[1,2,4,5,6,8]
# B=[3,7,10]
# c=merge(A,B)
# print(c)
#
# # 2) Find the intersection of two sorted arrays.
# def intersecion(arr1,arr2):
#     i,j=0,0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             i+=1
#         elif arr1[i]>arr2[j]:
#             j+=1
#         else:
#             print(arr2[i],end="  ")
#             i+=1
#             j+=1
#
# arr1=[1,2,3,4,5,6]
# arr2=[1,2,3,4,5,6,7,8]
# intersecion(arr1,arr2)
#
# 3) Remove Duplicates from Sorted Array
#
# def remove(a1):
#     print(set(a1))
# a1=[0,0,1,1,2]
# remove(a1)
#
# def removeDuplicate(a1):
#     i,j=0,0
#     while i < len(a1):
#         if a1[i]!=a1[i+1]:
#             a1[j]=a1[i]
#             j+=1
#     a1[j]=a1[len(a1)-1]
#     j+=1
#     return j
# a1=[1,2,3,4,4,5,5,5,6]
# c=removeDuplicate(a1)
# for i in range(0,c):
#     print(a1[i],end="")
#
# def removeDuplicates(arr, n):
#     if n == 0 or n == 1:
#         return n
#
#         # To store index of next
#     # unique element
#     j = 0
#
#     # Doing same as done
#     # in Method 1 Just
#     # maintaining another
#     # updated index i.e. j
#     for i in range(0, n - 1):
#         if arr[i] != arr[i + 1]:
#             arr[j] = arr[i]
#             j += 1
#
#     arr[j] = arr[n - 1]
#     j += 1
#     return j
#
#
# # Driver code
# arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# n = len(arr)
#
# # removeDuplicates() returns
# # new size of array.
# n = removeDuplicates(arr, n)
#
# # Print updated array
# for i in range(0, n):
#     print(" %d " % (arr[i]), end=" ")
#
# def lsa(lst,n):
#     maxSum=-100
#     for i in range(n):
#         for j in range(i,n):
#             currentSum=0
#             for k in range(i,j+1):
#                 currentSum+=lst[k]
#             if currentSum > maxSum:
#                 maxSum=currentSum
#     return maxSum
# lst=[-1,4,-2,4,-1,3,5,-6]
# n=len(lst)
# c=lsa(lst,n)
# print(c)
#
#
# print(c)
#
# def zeroSum(lst,n):
#     cur_sum=0
#     found=False
#     for i in range(1,len(lst)):
#         cur_sum+=lst[i]
#         if cur_sum ==0:
#             return  True
#         else:
#             return False
# lst=[2,1,3,4,2]
# n=len(lst)
# c=zeroSum(lst,n)
# print(c)