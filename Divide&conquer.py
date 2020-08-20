##)1 binary search

def binearySarch(arr,key):
    start=0
    end=len(arr)-1
    while start <=end:
        mid=(start+end)//2

        if arr[mid]==key:
            return mid
        elif arr[mid] > key:
            end=mid-1
        else:
            start=mid+1

    return -1
arr=[1,3,6,9,23,45,68,77,87,98]
key=4
b=binearySarch(arr,key)
if b==-1:
    print('key not found ')
else:
    print('key found at index :',b)