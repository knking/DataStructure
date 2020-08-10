
# class HastTable:
#     def __init__(self):
#         self.MAX=100
#         self.arr=[None for i in range(self.MAX)]
#
#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h += ord(char)
#         return h % self.MAX
#
#     def __setitem__(self,key,value):
#         k=self.get_hash(key)
#         self.arr[k]=value
#
#     def __getitem__(self,key):
#         k=self.get_hash(key)
#         return self.arr[k]
#
#
# t=HastTable()
# t["march 6"]=130
# t["aprail 7"]=120
# t["may 8"]=140
# t["june 10"]=150
# t["july 12"]=160
# print(t["aprail 7"])

##1) Fidn first reapeting character
# s="abcdee"
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         print(s[i+1])
#         break
# else:
#     print("No first reapeted character")

## using hashing

def FirstRepeatedChar(str):
    count=[0]*256
    size=len(str)
    for i in range(size):
        if count[ord(str[i])]==1:
            print(str[i])
            break
        else:
            count[ord(str[i])]+=1
    if i==size:
        print("No repeated char")
    return 0
FirstRepeatedChar(["a","c","b","a","d","e","f","g","h","k"])
