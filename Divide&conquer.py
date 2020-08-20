##)1 binary search

# def binearySarch(arr,key):
#     start=0
#     end=len(arr)-1
#     while start <=end:
#         mid=start+(end-start)//2
#
#         if arr[mid]==key:
#             return mid
#         elif arr[mid] > key:
#             end=mid-1
#         else:
#             start=mid+1
#     return -1
# arr=[1,3,6,9,23,45,68,77,87,98]
# key=98
# b=binearySarch(arr,key)
# if b==-1:
#     print('key not found ')
# else:
#     print('key found at index :',b)

##) using recursion

# def bsearch(arr,key,left,right):
#     if left-right==0:
#         return False
#     mid=(left+right)//2
#     if key==arr[mid]:
#         return True
#     if key < arr[mid]:
#         return bsearch(arr,key,left,mid)
#     else:
#         return bsearch(arr,key,mid+1,right)
#
# arr=[1,3,6,9,23,45,68,77,87,98]
# key=98
# if bsearch(arr,key,0,len(arr)-1):
#     print('Found')
# else:
#     print('Not found')