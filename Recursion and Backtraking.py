import array
#1) Reverse a string using recursion

def reverseString(s):
    if len(s)==0:
        return s
    else:
        #return s[len(s)-1]+reverseString(s[:len(s)-1])
        return reverseString(s[1:])+s[0]
s="abcdef"
k=reverseString(s)
print(k)

# 2) Find sum of N natural number

def naturalNumberSum(n):
    if n==1:
        return 1
    else:
        return n+naturalNumberSum(n-1)
s=naturalNumberSum(5)
print(s)

# # # 3) Find the power using recursion a^b

def power(a,b):
    if b==0:
        return 1
    else:
        return a * power(a,b-1)
p=power(2,4)
print(p)

# 5) fast power

def fastPower(a,b):
    if b==0:
        return 1
    if b % 2==0:
        return fastPower(a*a,b/2)

    return   a * fastPower(a,b-1)

p=fastPower(5,200)
print(p)

# 6) find al the path in N X M gid

def nxmGrid(n,m):
    if (n==1 or m==1) :
        return 1
    return nxmGrid(n,m-1)+nxmGrid(m,n-1)
path=nxmGrid(7,3)
print(path)

#7) Factorial using recursion

def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 8) Find the sum of array element

def sumOfArray(arr,n):
    if len(arr)==1:
        return arr[0]
    else:
        return  arr[0]+sumOfArray(arr[1:],n)

arr=array.array("i",[4,3,5,6,7])
n=len(arr)
print("l",n)
s=sumOfArray(arr,n)
print(s)

##9) Reverse an array

def reverse(array):

    # if len(array) == 0:  # If we encounter an empty array, simply return an empty array
    #     return []


    if len(array) == 1:  # Inverting an array of size 1 returns the same array
        return array


    return [array[len(array) - 1]] + reverse(array[:len(array) - 1])
    # The first part is storing the last element to be appended later
    # The second part is calling another instance of the same function with the last element removed

array = [1, 2, 3, 4]
print(reverse(array))

# 10) Replace all occurrences of pi with 3.14 in a given string

def replacePieHelper(string, start):
    if len(string) < 2 or start == len(string):
        return string
    replacePieHelper(string, start + 1)
    if (string[start] == 'p' and
            string[start + 1] == 'i'):
        # Replacing with "3.14"
        string[start:start + 2] = ['3', '.', '1', '4']
string = "pipipipppppiipiipi"
string = list(string)
replacePieHelper(string, 0)
string = ''.join(string)
print(string)

#11)  String to integer convertor

def myAtoiRecursive(string, num):
    # base case, we've hit the end of the string,
    # we just return the last value
    if len(string) == 1:
        return int(string) + (num * 10)

        # add the next string item into our num value
    num = int(string[0:1]) + (num * 10)

    # recurse through the rest of the string
    # and add each letter to num
    return myAtoiRecursive(string[1:], num)


# Driver Code
string = "112"

print(myAtoiRecursive(string, 0))

#12) Check number is palindrom or not
def palen(num , temp):
    if (num==0):
        return temp
    else:
        temp = (temp*10)+(num%10)
        return palen(num/10,temp)
num=int(input("enter the number : "))
temp=palen(num,0)
if(temp !=num):
    print("yes")
else:
    print("no")

##13) printing all permutations

def permute(a, l, r):
    #s={}
    if l == r:
        print("".join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack

#Driver program to test the above function
string = "1234"
n = len(string)
a = list(string)
permute(a, 0, n - 1)

# ) use of in built method
from itertools import permutations

print ([''.join(p) for p in permutations('ABC')])

#14) Flood fill
# def flood_fill(a,r,c,toFill,prevFill):
#     rows=len(a)
#     cols=len(a[0])
#     if (r < 0 or r>=rows) or (c < 0 or c>=cols):
#         return
#     if a[r][c] !=prevFill:
#         return
#     a[r][c]=toFill
#     flood_fill(a,r-1,c,toFill,prevFill)
#     flood_fill(a, r, c-1, toFill, prevFill)
#     flood_fill(a, r+1, c, toFill, prevFill)
#     flood_fill(a, r, c+1, toFill, prevFill)
# a=[[1, 1, 1, 1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1, 1, 0, 0],
#           [1, 0, 0, 1, 1, 0, 1, 1],
#           [1, 2, 2, 2, 2, 0, 1, 0],
#           [1, 1, 1, 2, 2, 0, 1, 0],
#           [1, 1, 1, 2, 2, 2, 2, 0],
#           [1, 1, 1, 1, 1, 2, 1, 1],
#           [1, 1, 1, 1, 1, 2, 2, 1]]
# flood_fill(a,3,3,5,2)
# for i in range(8):
#     for j in range(8):
#         print(a[i][j],end="")
#     print()

##15) Game theory!(coin problem)

# def coin_max(lst,left,right):
#     if left+1==right:
#         return max(lst[left],lst[right])
#     return max(lst[left]+min(coin_max(lst,left+2,right),coin_max(lst,left+1,right-1)),
#                lst[right]+min(coin_max(lst,left+1,right-1),coin_max(lst,left,right-2)))
# lst=[1,5,7,3,2,4]
# print(coin_max(lst,0,len(lst)-1))
#

def half(lst):
    temp=0
    lst1=[]
    total_sum=sum(lst)
    half_sum=total_sum/2
    for i in range(len(lst)):
        temp+=lst[i]
        if temp <=half_sum:
            lst1.append(lst[i])
    return lst1
lst=[1,2,3,4,5,5]
print(half(lst))




