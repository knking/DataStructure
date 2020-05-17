#----------------SelectonSort----------------

# num=int(input("How many number you wants to sort ? :"))
# l=[int(input("Enter number : "))for x in range(num)]
# print("Unsorted list : ",l)
#
# def selectionSort(lst):
#
#     for start in range(len(lst)):
#         minpos=start
#         for i in range(start,len(lst)):
#             if lst[i]<lst[minpos]:
#                 minpos=i
#
#         (lst[start],lst[minpos])=(lst[minpos],lst[start])
# selectionSort(l)
# print("Sorted list",l)


#-----------------------insertion sort------------

def insertionSort(seq):

    for s in range(len(seq)):
        pos=s
        while pos >0 and seq[pos]< seq[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
            pos=pos-1

l=[5,4,9,0,1,2,3,5]
insertionSort(l)
print(l)



