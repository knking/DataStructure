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

# 5)Write a program to sort a Array

def quicksort(A,l,r):
    if r-l<=1:
        return 0
    yellow=l+1
    for green in range(l+1,r):
        if A[green]<=A[l]:
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow=yellow+1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])

    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)

l=list(range(5,0,-1))
print(l)
arry_for_sort=array.array('i',[4,3,6,5,7,13,12])
quicksort(arry_for_sort,0,len(arry_for_sort))
for i in arry_for_sort:
    print(i, end=" ")

# 6)find kth smallest and kth greater element in array

def kthSmall(arr1,k,n):
    sorted(arr1)
    return arr1[k-1]

arr1=array.array('i',[23,43,56,76,53])
n=len(arr1)
k=3
print(kthSmall(arr1,n,k))


def kthGreatest(arr2,j,m):
    sorted(arr1)
    return arr1[-m]

arr1=array.array('i',[23,43,56,76,53])
j=len(arr1)
m=3
print(kthGreatest(arr1,j,m))

#7)Given an number	n. Find	the number of occurrences of n in the array.

num=array.array('i',[4,3,3,3,3,3,3,3,3,4,3,4,5,6,3,2,4,5,6,7,1,2,1,2,12])
number=int(input("Enter number for occurrences : "))
if number in num:
    n=num.count(number)
    print(n)
else:
    print("Number is not present")

#8) Given an array which consists of only 0,1 an 2. Sort the array without using sorting algorithm

def SortWithoutSorting(arr):
    l1=[]
    l2=[]
    l3=[]
    for i in range(len(arr)):
        if arr[i]<1:
            l1.append(arr[i])
        elif arr[i]==1:
            l2.append(arr[i])
        else:
            l3.append(arr[i])
    return (l1+l2+l3)
arr=array.array('i',[0,1,0,1,2,2,0,1])
print(SortWithoutSorting(arr))

#9) Find the range of array.Range means the difference between the maximum and minimum element in the array

arr=array.array('i',[10,23,12,3,4,5,16,34])
maximum=max(arr)
minimum=min(arr)
range=maximum-minimum
print("Range of array :",range)

#10) Move all negavtive element to one side of the array

arr=array.array('i',[-2,-3,-10,-5,2,3,4,-6,1,3,-4])
l1=[]
l2=[]
for i in range(len(arr)):
    if arr[i]<0:
        l1.append(arr[i])
    else:
        l2.append(arr[i])
print(l1+l2)

