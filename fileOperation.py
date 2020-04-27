#FileRead=open('data.txt','r')

#display=FileRead.read()

#print(display)

#FileWrite=open('data.txt','w')

#FileWrite.write("I am Fine \n How are you Dear")
#FileWrite.close()
#l=[30,40,50,60]
#for i in l:
    #FileWrite.write(str(i)+'\n')

#age guess Program

#birth_year=int(input("Enter your birh year:\n"))

#age=2020-birth_year
#print(f'Your age is: {age}')

#password length checker
#username=input("Enter name ")
#password=input("Enter password")

#pass_len=len(password)
#hidden_pas="*" * pass_len
#print(f'Hey {username} ,Your password {hidden_pas} ,length is :{pass_len}')
# lst=['e','e','t','y','y','y','z','d']
# print("Oriinal list with duplicate number",lst)
#
# st=set(lst)
#
# print("After removing the duplicate from list :" ,st)

# import array
#
# arr=array.array('i',[3,4,5,6,3,7])
# print("Old array : " )
# for i in range(0,len(arr)):
#     print(arr[i],end=" ")
# arr.append(10)
# print('\r')
# print("New array : ")
# for j in range(0,len(arr)):
#     print(arr[j],end=" ")
# print('\r')
# print(arr.index(10))
# arr.reverse()
# print("After reverse the vale of array is : ")
# for j in range(0,7):
#     print(arr[j],end=" ")

# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A"))
# print(x.strftime("%d"))
# print(x.strftime("%D"))
# print(x.strftime("%M"))
# print(x.strftime("%m"))

# add,add1=input("Enter number to add : ").split()
# try:
#     sm = add + add1 + 10
#     print(sm)
# except:
#     print("Plzz Enter integer to add ")

def maxNumber(lst):
    max = lst[0]
    for i in range(len(lst)):
        if max < lst[i]:
            max=lst[i]

    return max
lst=[65,3,43,54,56,76]
print(maxNumber(lst))

