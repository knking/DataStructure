
##1)right set bit
# def setBit(n):
#     rsb=n & (~n)+1
#     print(rsb)
#
# setBit(12)

##2)kernighms algorithm

# def kernighms(n):
#     count=0
#     rsb=0
#     while n!=0:
#         rsb=(n & -n)
#         n=n-rsb
#         count+=1
#     return count
# print(kernighms(4))

##3)Find repeate and missing number

# arr=[2,3,5,5,8,3,2,7,7]
# x=arr[0]
# for i in range(1,len(arr)):
#     x=x^arr[i]
# print(x)


##4)All repeating except two(two unique reat repeate)

# def twoUnique(arr):
#     xxory=0
# #xor all the element,after this we get non repeating number
#     for i in range(len(arr)):
#         xxory=xxory ^ arr[i]
#
# #right set bit mask of unique element
#     rsb=xxory & -xxory
#     x=0
#     y=0
# #here we check all the element which right set bit mask is ON or OFF
# #then distinguish between the number which rsb mask is on and oFF
#     for i in range(len(arr)):
#         #here bit is off so we take xor
#         if arr[i] & rsb==0:
#             x=x^arr[i]
#         #here bit is on so again we take xor
#         else:
#             y=y^arr[i]
#
#     if x < y:
#         print(x)
#         print(y)
#     else:
#         print(y)
#         print(x)
# ar=[3,4,3,5,6,5,7,7,9,9]
# twoUnique(ar)

##5)find duplicate and missing number

def dupAndMiss(ar):
    xor=0
    for i in range(len(ar)):
        xor ^=ar[i]

    for i in range(1,len(ar)+1):
        xor ^= i

    rsb=xor & -xor
    x=0
    y=0
    for i in range(len(ar)):
        if ar[i] & rsb==0:
            x=x^ar[i]
        else:
            y=y^ar[i]

    for i in range(len(ar)+1):
        if i & rsb == 0:
            x = x ^ i
        else:
            y = y ^ i

    for i in range(len(ar)):
        if ar[i]==x:
            print('Missing is :',y)
            print('repeating is :',x)
            break
        elif ar[i]==y:
            print('Missing is :', x)
            print('repeating is :', y)
            break

ar=[1,2,3,4,5,7,7,8,9]
dupAndMiss(ar)