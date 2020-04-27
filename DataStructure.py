#print("Welcome in array Section ")
import array

# 1	Create an Array of size 10 of integers.Take input from the user for these 10 elements
#and print the entire array

arr1=array.array('i',[])
print("Enter 10 Elements ")
for i in range(10):
    num=int(input())
    arr1.append(num)
print(arr1)

#2)	Check whether n	is	present	in	an array of	size m or not.
# Input	-n,m (Input	number,	size of	array)
# Take	input n elements for the array
# Output ->	true/false

num=int(input("Enter number to search : " ))
size=int(input("Enter the size of array"))
arr2=array.array('i',[])
print("Enter array")
for i in range(size):
    num1=int(input())
    arr2.append(num1)
print(num in arr2)


#3)	Find the minimum and maximum element in	an array.

arr4=array.array('i',[54,3,23,45,65,62])
print(max(arr4))
print(min(arr4))

#4) write a program to reverse a array
arr5=array.array('i',[1,2,3,4,5,6])
arr5.reverse()
print(arr5)
print(arr5[::-1])

# Write a program to sort a Array

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

#l=list(range(5,0,-1))
#print(l)
# arry_for_sort=array.array('i',[4,3,6,5,7,13,12])
# quicksort(arry_for_sort,0,len(arry_for_sort))
# for i in arry_for_sort:
#     print(i, end=" ")

# find kth smallest and kth greater element in array

# def kthSmall(arr1,k,n):
#     sorted(arr1)
#     return arr1[k-1]
#
# arr1=array.array('i',[23,43,56,76,53])
# n=len(arr1)
# k=3
# print(kthSmall(arr1,n,k))


def kthGreatest(arr2,j,m):
    sorted(arr1)
    return arr1[-m]

arr1=array.array('i',[23,43,56,76,53])
j=len(arr1)
m=3
print(kthGreatest(arr1,j,m))



