##1) Gcd of number
# def gcd(m,n):
#     if m <=1 or n <=1:
#         return max(m,n)
#     i=min(m,n)
#     while i >0:
#
#         if m%i==0 and n%i==0:
#             return i
#         else:
#             i=i-1
# g=gcd(8,6)
# print(g)

# def gcd(A, B):
#     if B > A:
#         A, B = B, A
#     while B != 0:
#         temp = B
#         B = A % B
#         A = temp
#     return A
# print(gcd(2,0))


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
# decimalToBinary(7)

## 5) Trailing Zeroes in Factorials

##basic appoach
# def fact(n):
#     if n ==0:
#         return 1
#     else:
#         return n * fact(n-1)
# s=fact(100)
# count=0
# while s !=0:
#     r=s%10
#     if r==0:
#         count+=1
#     else:
#         break
#     s=s//10
# print(count)

# def trailing_zero(n):
#     count=0
#     while n!=0:
#         count+=n//5
#         n=n//5
#     return count
# print(trailing_zero(100))

# def trailingZeros(number):
#     p=5
#     count=0
#     while number/p>0:
#         count+=number/p
#         p=p*5
#     return int(count)
# print(trailingZeros(1980)

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

# def titleToNumber(A):
# 	T = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
# 	return sum(T[ch] * 26**i for i, ch in enumerate(A[::-1]))
# print(titleToNumber("AAA"))

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

##9) Reverse integer
# def reverseInteger(num):
#     temp=0
#     isNegative=False
#     if num < 0:
#         isNegative=True
#         num = -1 * num
#     while num!=0:
#         temp=temp*10+num%10
#         num=num//10
#     if (temp >=2**31-1 or -1 * temp < -2**31): return 0
#     return temp if not isNegative else -1 * temp
# print(reverseInteger(-1234567891))

#Sum of pairwise Hamming Distance
#Power Of Two Integers
#Power Of Two Integers
#City Tour

##10)Sieve of Eratosthenes

# def sieveOfErathosthenes(n):
#     primes=[True for i in range(n+1)]
#     primes[0]=False
#     primes[1]=False
#     for p in range(2,n+1):
#         if primes[p]==True:
#             for i in range(p*p,n+1,p):
#                 primes[i]=False
#
#     for i in range(2,n+1):
#         if primes[i]==True:
#             print(i,end=" ")
# sieveOfErathosthenes(20)

##11) Sieve of Sundaram

# def sieveOfSundram(n):
#     newN=int((n-1)/2)
#     marked=[0] * (newN+1)
#
#     for i in range(1,newN+1):
#         j=i
#         while i+j+2*i*j <=newN:
#             marked[i+j+2*i*j]=1
#             j+=1
#
#     if n>2:
#         print(2,end=" ")
#     for i in range(1,newN+1):
#         if marked[i]==0:
#             print(2*i+1,end=" ")
# sieveOfSundram(20)

##13)Given an even number(greater than 2)return two prime numbers whose sum will be equal to given number.(Prime Sum)

# def sum_of_primes(num):
#     isPrime = 1
#     for i in range (2,int(num/2),1):
#         if(num % i == 0):
#             isPrime = 0
#             break
#     return isPrime
#
# num = int(input("Enter a number : "))
# flag = 0
# i = 2
# for i in range (2,int(num/2),1):
#     if(sum_of_primes(i) == 1):
#         if(sum_of_primes(num-i) == 1):
#             print(num,"can be expressed as the sum of",i,"and",num-i)
#             flag = 1
# if (flag == 0):
#     print(num,"cannot be expressed as the sum of two prime numbers")
# sum_of_primes(num)

##14) Hamming distance

# def decimalToBinary(x,y):
#     return bin(x^y).count("1")
# print(decimalToBinary(1,4))

# def detob(x,y):
#     ans = 0
#     while x or y:
#         ans += (x % 2) ^ (y % 2)
#         x //= 2
#         y //= 2
#     return ans
# print(detob(1,4))

# def totalHammingDistance(nums):
#     return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))
# nums=[4,14,2]
# print(totalHammingDistance(nums))

# class Solution(object):
#     def totalHammingDistance(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         ans = 0
#         mask = 1
#         for j in range(0, 32):
#             ones = zeros = 0
#             for num in nums:
#                 if num & mask:
#                     ones += 1
#                 else:
#                     zeros += 1
#             ans += ones * zeros
#             mask = mask << 1
#         return ans
# s=Solution()
# print(s.totalHammingDistance(nums=[4,14,2]))

##15)sum of bit differences among all pairs(Hamming distance air sum)
# def decimalToBinary(x,y):
#     return bin(x^y).count("1")
# lst=[1,3,5]
# sum=0
# for i in range(len(lst)):
#     for j in range(len(lst)):
#         sum+=decimalToBinary(lst[i],lst[j])
#
# print(sum)

