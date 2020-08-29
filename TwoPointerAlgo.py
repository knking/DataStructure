
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
# B=[1,2,4,5,6,8]
# A=[3,7,10]
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
# print(c)
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

##4) 3 sum

# class tsum:
#
#     def threeSum(self,arr,n):
#         n=len(arr)
#         for i in range(n-1):
#             if self.twoSum(arr,-arr[i],i+1):
#                 return True
#         return False
#
#     def twoSum(self,ar,sum,i):
#         j=len(ar)-1
#         while i < j:
#             total=ar[i]+ar[j]
#             if total < sum:
#                 i+=1
#             elif total > sum:
#                 j-=1
#             else:
#                 return True
#         return False
# l=tsum()
# ar=[4,3,0,1,4,-5]
# print(l.threeSum(ar,len(ar)))

##) find all set of number whose sum is zero(3 sum)

# def threeSum(arr,n):
#     arr.sort()
#     res=[]
#     n=len(arr)
#     for j in range(n-2):
#         if j >0 and arr[j] == arr[j-1]:
#             continue
#         l=j+1
#         r=n-1
#
#         while l < r:
#             total=arr[j]+arr[l]+arr[r]
#             if total <0:
#                 l+=1
#             elif total >0:
#                 r-=1
#             else:
#                 res.append([arr[j],arr[l],arr[r]])
#                 while l<r and arr[l]==arr[l+1]:
#                     l+=1
#                 while l<r and arr[r] ==arr[r-1]:
#                     r-=1
#                 l+=1
#                 r-=1
#     return res
# arr=[-1, 0, 1, 2, -1, -4]
# n=len(arr)
# print(threeSum(arr,n))
#

##5)Trapping rain water problem

# def trpping(arr,n):
#     res=0
#     for i in range(1,n-1):
#         left=arr[i]
#
#         for j in range(i):
#             left=max(left,arr[j])
#
#         right=arr[i]
#         for k in range(i+1,n):
#             right=max(right,arr[k])
#
#         res=res+(min(left,right)-arr[i])
#     return res
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# n = len(arr)
# print(trpping(arr,n))

##) Another mathod

# def trapping(arr,n):
#     left_max=0
#     right_max=0
#     left=0
#     right=n-1
#     res=0
#     while left<=right:
#         if arr[left] < arr[right]:
#             if arr[left] > left_max:
#                 left_max=arr[left]
#             else:
#                 res+=left_max-arr[left]
#             left+=1
#         else:
#             if arr[right]> right_max:
#                 right_max=arr[right]
#             else:
#                 res+=right_max-arr[right]
#
#             right-=1
#     return res
#
# arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# n = len(arr)
# print(trapping(arr,n))
#

##)Another method

def trapping(height):
    left,right=0,len(height)-1
    leftMax=0
    rightMax=0
    result=0
    while left < right:
        leftMax=max(leftMax,height[left])
        rightMax=max(rightMax,height[right])

        if leftMax <= rightMax:
            result+=leftMax-height[left]
            left+=1
        else:
            result+=rightMax-height[right]
            right-=1
    return result

h=[0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping(h))

##6) Maximum consecutive one’s (or zeros) in a binary array
# def consecutive(arr,n):
#     count=0
#     maximum=0
#     for i in range(len(arr)):
#         if arr[i]==0:
#             count=0
#         else:
#             count+=1
#             maximum=max(maximum,count)
#     return maximum
# arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]#[1, 1, 0, 0, 1, 0, 1,0, 1, 1, 1, 1]
# n=len(arr)
# print(consecutive(arr,n))
