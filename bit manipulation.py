
##1)right set bit
def setBit(n):
    rsb=n & (~n)+1
    print(rsb)

setBit(12)

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




