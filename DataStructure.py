#print("Welcome in array Section ")

import array

# 1	Create an Array of size 10 of integers.Take input from the user for these 10 elements
#and print the entire array

# arr1=array.array('i',[])
# print("Enter 10 Elements ")
# for i in range(10):
#     num=int(input())
#     arr1.append(num)
# print(arr1)

# 2) Check whether n is	present	in	an array of	size m or not.
# Input	-n,m (Input	number,	size of	array)
# Take	input n elements for the array
# Output ->	true/false

# size=int(input("Enter the size of array : "))
# arr2=array.array('i',[])
# print("Enter array")
# for i in range(size):
#     #num1=int(input())
#     arr2.append(int(input()))
# num=int(input("Enter number to search : " ))
# print(num in arr2)


#3)	Find the minimum and maximum element in	an array.
# arr4=array.array('i',[54,3,23,45,65,62])
# print(max(arr4))
# print(min(arr4))
#
# #4) write a program to reverse a array
# arr5=array.array('i',[1,2,3,4,5,6])
# arr5.reverse()
# print(arr5)
# print(arr5[::-1])

# 5)Write a program to sort a Array

# def quicksort(A,l,r):
#     if r-l<=1:
#         return 0
#     yellow=l+1
#     for green in range(l+1,r):
#         if A[green]<=A[l]:
#             (A[yellow],A[green])=(A[green],A[yellow])
#             yellow=yellow+1
#     (A[l],A[yellow-1])=(A[yellow-1],A[l])
#
#     quicksort(A,l,yellow-1)
#     quicksort(A,yellow,r)
#
# l=list(range(5,0,-1))
# print(l)
# arry_for_sort=array.array('i',[4,3,6,5,7,13,12])
# quicksort(arry_for_sort,0,len(arry_for_sort))
# for i in arry_for_sort:
#     print(i, end=" ")

# 6)find kth smallest and kth greater element in array

# def kthSmall(arr1,k,n):
#     sorted(arr1)
#     return arr1[k-1]
# arr1=array.array('i',[23,43,56,76,53])
# n=len(arr1)
# k=3
# print(kthSmall(arr1,n,k))
#
#
# def kthGreatest(arr2,j,m):
#     sorted(arr1)
#     return arr1[-m]
#
# arr1=array.array('i',[23,43,56,76,53])
# j=len(arr1)
# m=3
# print(kthGreatest(arr1,j,m))

#7)Given an number	n. Find	the number of occurrences of n in the array.

# num=array.array('i',[4,3,3,3,3,3,3,3,3,4,3,4,5,6,3,2,4,5,6,7,1,2,1,2,12])
# number=int(input("Enter number for occurrences : "))
# if number in num:
#     n=num.count(number)
#     print(n)
# else:
#     print("Number is not present")

#8) Given an array which consists of only 0,1 an 2. Sort the array without using sorting algorithm

# def SortWithoutSorting(arr):
#     l1=[]
#     l2=[]
#     l3=[]
#     for i in range(len(arr)):
#         if arr[i]<1:
#             l1.append(arr[i])
#         elif arr[i]==1:
#             l2.append(arr[i])
#         else:
#             l3.append(arr[i])
#     return (l1+l2+l3)
# arr=array.array('i',[0,1,0,1,2,2,0,1])
# print(SortWithoutSorting(arr))


# def sortArray(start,mid,high,lst):
#     while (mid <= high):
#         if lst[mid]==0:
#             lst[start],lst[mid]=lst[mid],lst[start]
#             start+=1
#             mid +=1
#         elif lst[mid]==1:
#             mid +=1
#         else:
#             lst[mid],lst[high]=lst[high],lst[mid]
#             high -=1
#     return lst
# lst=[0,1,2,0,0,0,2,1,2]
# c=sortArray(0,0,len(lst)-1,lst)
# print(c)


#9) Find the range of array.Range means the difference between the maximum and minimum element in the array

# arr=array.array('i',[10,23,12,3,4,5,16,34])
# maximum=max(arr)
# minimum=min(arr)
# range=maximum-minimum
# print("Range of array :",range)
#
# #10) Move all negative element to one side of the array
#
# arr=array.array('i',[-2,-3,-10,-5,2,3,4,-6,1,3,-4])
# l1=[]
# l2=[]
# for i in range(len(arr)):
#     if arr[i]<0:
#         l1.append(arr[i])
#     else:
#         l2.append(arr[i])
# print(l1+l2)

# def moveArray(arr,n):
#     j=0
#     for i in range(0,n):
#         if arr[i] < 0:
#             arr[i],arr[j]=arr[j],arr[i]
#             j +=1
#     return arr
# arr=[3,-2,-3,-4,4]
# n=len(arr)
# c=moveArray(arr,n)
# print(c)

# #11) find the union and intersecton of two sorted array
#
# def unionOfArray(arr1,arr2):
#     i,j=0,0
#     #  while loop for comparing all the value which present in both array
#     while i < len(arr1) and j < len(arr2):
#         #  while loop   handle the duplicate value  in arr1
#         # if dupicate value present then move the i pointer
#         while i < len(arr1)-1 and arr1[i]==arr1[i+1]:
#             i+=1
#          #while loop   handle the duplicate value  in arr2
#          #if dupicate value present then move the j pointer
#         while j < len(arr2)-1 and arr2[j]==arr2[j+1]:
#             j+=1
#         # this if conditions are for comparing the value which present in array
#         if arr1[i] < arr2[j]:
#             print(arr1[i])
#             i+=1
#         elif arr1[i] > arr2[j]:
#             print(arr2[j])
#             j+=1
#         else:
#             print(arr2[j])
#             i+=1
#             j+=1
#     # print reaming element which present if larger array
#     while i < len(arr1):
#         # compare duplicates in larger array
#         if i< len(arr1)-1 and arr1[i]==arr1[i+1]:
#             i+=1
#         else:
#             print(arr[i])
#             i+=1
#
#     while j < len(arr2):
#         ## compare duplicates in larger array
#         if j < len(arr2)-1 and arr2[j]==arr2[j+1]:
#             j+=1
#         else:
#             print(arr2[j])
#             j+=1
#
# def intersectionOfArray(arr1,arr2):
#     i,j=0,0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] < arr2[j]:
#             i+=1
#         elif arr1[i] > arr2[j]:
#             j+=1
#         else:
#             print(arr2[j])
#             i+=1
#             j+=1
# # Driver program
# arr1 = [1,2, 2,4, 5, 6]
# arr2 = [2,1,3, 5, 7]
# unionOfArray(arr1,arr2)
# print("Intesection of two array")
# intersectionOfArray(arr1,arr2)
#
# # 12) Rotate array by 1

# def rotateArray(arr,n):
#
#     temp=arr[n-1]
#     for i in range(n-1,0,-1):
#         arr[i]=arr[i-1]
#     arr[0]=temp
# arr=[1,3,5,7,9]
# n=len(arr)
# print("Before Rotation")
# for j in range(0,n):
#     print(arr[j],end=" ")
# print()
# print("After rotation ")
# rotateArray(arr,n)
# for j in range(0,n):
#     print(arr[j],end=" ")

## 13) Maximum sum of array

# def subArray(lst,n):
#     max_sum=-100
#     cur_sum=0
#     for i in range(0,len(lst)):
#         cur_sum+=lst[i]
#
#         if cur_sum > max_sum:
#             max_sum = cur_sum
#         if cur_sum < 0:
#             cur_sum=0
#     return max_sum
# lst=[-1,4,-2,4,-1,3,5,-6]
# n=len(lst)
# c=subArray(lst,n)

# 14) Find the duplictes in array

# def dupicates(A):
#     lenA=len(A)
#     temp=[0] * lenA
#     for i in A:
#         if temp[i-1]:
#             return i
#         else:
#             temp[i-1]=1
#     return -1
# A=[1,2,3,1,2,3,4,5,6,6,6]
# print(dupicates(A))


# def repeatedNumber(A):
#     sumOfList = sum(A)
#     n = len(A)
#     sumOfRange = int(n * (n + 1) / 2) - n
#     return sumOfList - sumOfRange
# A=[1,2,3,4,5,2,3,4,5,6]
# print(repeatedNumber(A))

##Find repeate and missing nuber
#(using hasing)

# lst=[1,2,4,5,5,6]
# lst1=[0]*len(lst)
# for i in range(len(lst)):
#     s=lst[i]
#     lst1[s-1]=lst1[s-1]+1
#
# for i in range(len(lst1)):
#     if lst1[i]> 1:
#         print(" Reapete number is :",i+1)
#     elif lst1[i]==0:
#         print("Missing number :",i+1)





# def dupicate(lst):
#     for i in range(len(lst)):
#         if lst[abs(lst[i])]>= 0:
#             lst[abs(lst[i])]=-lst[abs(lst[i])]
#         else:
#             print(abs(lst[i]))
# lst=[1,2,3,3,2,4,5]
# dupicate(lst)

# def misN(lst,n):
#     sumN =((n+1) * (n + 2))/ 2
#     sumA=sum(lst)
#     return sumN-sumA
# lst=[1,2,3,4,6]
# n=len(lst)
# print(misN(lst,n))

# def duplicate(lst,n):
#     sum_of_lst=sum(lst)
#     sum_of_n=sum(set(lst))
#     return sum_of_lst-sum_of_n
# lst=[1,2,3,3,3,4]
# n=len(lst)
# print(duplicate(lst,n))

# 14) set matrix zeros
# def setZeroes(A):
#     rows = set()
#     cols = set()
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             if A[i][j] == 0:
#                 rows.add(i)
#                 cols.add(j)
#     for i in rows:
#         for j in range(len(A[0])):
#             A[i][j] = 0
#     for j in cols:
#         for i in range(len(A)):
#             A[i][j] = 0
#     return A

# class Solution:
#     # @param A : list of list of integers
#     # @return the same list modified
#     def setZeroes(self, A):
#         N = len(A)
#         M = len(A[0])
#         del_first_row = False
#         del_first_col = False
#
#         for i in xrange(N):
#             if A[i][0] == 0:
#                 del_first_row = True
#                 break
#         for i in xrange(M):
#             if A[0][i] == 0:
#                 del_first_col = True
#                 break
#
#         for i in xrange(N):
#             for j in xrange(M):
#                 if A[i][j] == 0:
#                     A[i][0] = 2
#                     A[0][j] = 2
#
#         for i in xrange(1, N):
#             for j in xrange(1, M):
#                 if A[i][0] == 2:
#                     A[i][j] = 0
#                 elif A[0][j] == 2:
#                     A[i][j] = 0
#         for i in xrange(N):
#             if A[i][0] > 1 or del_first_row:
#                 A[i][0] = 0
#         for i in xrange(M):
#             if A[0][i] > 1 or del_first_col:
#                 A[0][i] = 0
#
#         return A

#
# class Solution:
#     # @param A : list of list of integers
#     # @return the same list modified
#     def setZeroes(self, A):
#         rowz = 0
#         colz = [0] * len(A[0])
#         # for i in range(len(A[0])):
#         #     colz += "0"
#         # print(len(A),len(A[0]))
#         for i in range(len(A)):
#             p = 0
#             rowz = 0
#             for j in range(len(A[0])):
#                 # print(i,j,colz)
#                 # print(i,j)
#                 if A[i][j] == 0:
#                     if p == 0:
#                         rowz = 1
#                         p = 1
#                     if colz[j] != 1:
#                         colz[j] = 1
#                         if i != 0:
#                             k = i - 1
#                             while k >= 0:
#                                 A[k][j] = 0
#                                 k -= 1
#
#                 if colz[j] == 1:
#                     A[i][j] = 0
#
#                 # print(A)
#
#             if rowz == 1:
#                 A[i] = [0] * len(A[0])
#
#                 # if colz[j]==1 or rowz == 1:
#                 #     A[i][j] = 0
#                 #     if colz[j]==1 and A[i-1][j] !=0:
#                 #         k = i-1
#                 #         while k>=0:
#                 #             A[k][j] = 0
#                 #             k-=1
#             # print(A[i][j])
#
#         return A

##set matrix zeros (Naive approcha)
# def setZeros(lst):
#     row_set=set()
#     col_set=set()
# #check the wether element is zros or not
#     for i in range(len(lst)):
#         for j in range(len(lst[i])):
#             if lst[i][j]==0:
#                 row_set.add(i)
#                 col_set.add(j)
# #check row and colomn which contain zeors, then make all element zero
#     for row in range(len(lst)):
#         for col in range(len(lst[row])):
#             if row in row_set or col in col_set:
#                 lst[row][col]=0
#     return lst
# lst1=[[0,4,1,0],
#       [3,2,1,5],
#       [4,0,7,2]]
#
# print(setZeros(lst1))


# def set_matrix(lst):
#     n=len(lst)
#     m=len(lst[0])
#     hasFirstrow=False
#     hasFirstCol=False
#     for i in range(n):
#         if lst[i][0]==0:
#             hasFirstrow=True
#             break
#     for i in range(m):
#         if lst[0][i]==0:
#             hasFirstCol=True
#             break
#
#     for i in range(1,n):
#         for j in range(1,m):
#             if lst[i][j]==0:
#                 lst[i][0]=0
#                 lst[0][j]=0
#     for i in range(1, n):
#         for j in range(1,m):
#             if lst[i][0]==0 or lst[0][j]==0:
#                 lst[i][j]=0
#
#     if hasFirstrow:
#         for i in range(m):
#             lst[0][i]=0
#
#     if hasFirstCol:
#         for j in range(n):
#             lst[j][0] =0
#     return lst
#
# lst2=[[1,1,1],
#       [1,0,1],
#       [1,1,1]]
#
# print(set_matrix(lst1))

#18) pascal triangle
#
# n=int(input("Enter number : "))
# lst1=[]
# for i in range(n):
#     temp_list=[]
#     for j in range(i+1):
#         if j==0 or j==i:
#             temp_list.append(1)
#         else:
#             temp_list.append(lst1[i-1][j-1]+lst1[i-1][j])
#     lst1.append(temp_list)
#
# for i in range(n):
#     for j in range(n-i-1):
#         print(format(" ","<2") ,end="")
#     for j in range(i+1):
#         print(format(lst1[i][j],"<3"),end=" ")
#     print()
##19) Buy and sell stock

# def buy_sell(lst):
#     mini=lst[0]
#     ans=0
#     for i in range(len(lst)):
#         if lst[i] < mini:
#             mini=lst[i]
#         else:
#             ans=max(ans,(lst[i]-mini))
#     print(ans)
# lst1=[7,1,5,3,6,4]
# buy_sell(lst1)

#20) buy and sell stock(buy and cell maximum time)

# def buy_sell(lst):
#     ans=0
#     for i in range(1,len(lst)):
#         if lst[i-1] < lst[i]:
#             ans+=lst[i]-lst[i-1]
#
#     print(ans)
# lst1=[7,1,5,3,6,4]
# buy_sell(lst1)

##21) rotate a marix or roate a image

# lst=[[5,1,9,11],
#     [2,4,8,10],
#     [13,3,6,7],
#      [15,14,12,16]]
# n=len(lst)
# m=len(lst[0])
#
# for row in range(n):
#     for col in range(row,m):
#         lst[row][col],lst[col][row]=lst[col][row],lst[row][col]
#print(lst)

# for i in range(n):
#     lst[i].reverse()

# for i in range(n):
#     s = 0
#     e = m - 1
#
#     while (s < e):
#         lst[i][s], lst[i][e] = lst[i][e], lst[i][s]
#         s+=1
#         e-=1
#print(lst)

# #22) print spiral matrix
# def spiralMatrix(lst):
#     # if not lst:
#     #     return lst
#     rowbegin=0
#     rowend=len(lst)
#     colbegin=0
#     colend=len(lst[0])
#     spiral=[]
#
#     while rowend > rowbegin and colend >colbegin:
#         for i in range(colbegin,colend):
#             spiral.append(lst[rowbegin][i])
#         for j in range(rowbegin+1,rowend-1):
#             spiral.append(lst[j][colend-1])
#         if rowend!=rowbegin+1:
#             for i in range(colend-1,colbegin-1,-1):
#                 spiral.append(lst[rowend-1][i])
#         if colbegin!=colend-1:
#             for j in range(rowend-2,rowbegin,-1):
#                 spiral.append(lst[j][colbegin])
#         rowbegin+=1
#         rowend-=1
#         rowbegin+=1
#         rowend-=1
#     return spiral
#
# lst1=[[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# print(spiralMatrix(lst1))










