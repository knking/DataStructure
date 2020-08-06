##1) Gcd of number
# def gcd(m,n):
#     i=min(m,n)
#     while i >0:
#
#         if m%i==0 and n%i==0:
#             return i
#         else:
#             i=i-1
# g=gcd(16,16)
# print(g)

# 2) Prime number

# num = 11
# # To take input from the user
# # num = int(input("Enter a number: "))
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             #print(i, "times", num // i, "is", num)
#             break
#     else:
#         print(num, "is a prime number")
#
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#     print(num, "is not a prime number")
#
# #3) Binary to integer conversion

# def bToi(num):
#     sum=0
#     i=0
#     while num !=0:
#         rem=num % 10
#         sum=sum+ rem * pow(2,i)
#         num=int(num/10)
#         i+=1
#     return sum
# print("Integer number : ",bToi(int(input("Enter number : "))))

#4) DEcimal to bineary conversion
# def decimalToBinary(n):
#     if(n > 1):
#         # divide with integral result
#         # (discard remainder)
#         decimalToBinary(n//2)
#     print(n%2, end=' ')
# decimalToBinary(10)

## 5) Trailing Zeroes in Factorials

# def trailingZeros(number):
#     p=5
#     count=0
#     while number/p>0:
#         count+=number/p
#         p=p*5
#     return int(count)
# print(trailingZeros(1980))

## 6) Find excel column number
# def excelColumNum(s):
#     res=0
#     for i in range(len(s)):
#         res *=26
#         res+=ord(s[i])-ord("A")+1
#     return res
# print(excelColumNum("AAA"))

# def excelColumn(s):
#     ans=0
#     power=1
#     n=len(s)
#     for i in range(n-1,-1,-1):
#         ans+=(ord(s[i])-64)* power
#         power=power*26
#
#     return ans
# print(excelColumn("AAA"))


## 7) Two sums
# def findTriplets(arr, n):
#     found = False
#     # sort array elements
#     arr.sort()
#     for i in range(0, n - 1):
#         # initialize left and right
#         l = i + 1
#         r = n - 1
#         x = arr[i]
#         while (l < r):
#
#             if (x + arr[l] + arr[r] == 0):
#                 # print elements if it's sum is zero
#                 print(x, arr[l], arr[r])
#                 l += 1
#                 r -= 1
#                 found = True
#             # If sum of three elements is less
#             # than zero then increment in left
#             elif (x + arr[l] + arr[r] < 0):
#                 l += 1
#
#             # if sum is greater than zero than
#             # decrement in right side
#             else:
#                 r -= 1
#
#     if (found == False):
#         print(" No Triplet Found")
#
#     # Driven source
#
#
# arr = [0,0,0]
# n = len(arr)
# findTriplets(arr, n)
#

# def tf(nums):
#     res=[]
#     nums.sort()
#     length=len(nums)
#     for i in range(length-2):
#         if i > 0 and nums[i]==nums[i-1]:
#             continue
#         l=i+1
#         r=length-1
#
#         while l < r:
#             total=nums[i]+nums[l]+nums[r]
#
#             if total < 0:
#                 l=l+1
#             elif total > 0:
#                 r=r-1
#             else:
#                 res.append([nums[i],nums[l],nums[r]])
#                 while l < r and nums[l]==nums[l+1]:
#                     l=l+1
#                 while l < r and nums[r]==nums[r-1]:
#                     r=r-1
#
#                 l=l+1
#                 r=r+1
#
#     return res
# nums=[-2,-3,5,6,0,6,-6]
# print(tf(nums))

##8) check number is palindrom or not
# def palindrom(x):
#     if x <0:
#         return False
#     if x>0 and x %10==0:
#         return False
#     num=0
#     while x>num:
#         num=num*10 + x %10
#         x=x//10
#     if x==num or num//10==x:
#         return True
#     return False
# print(palindrom(-1111))

# n=2147447412
# temp=n
# ans=0
# while n >0:
#     rem=n%10
#     ans=rem+ans *10
#     n=n//10
# if temp==ans:
#     print("palindrom")
#
# else:
#     print("not ")





