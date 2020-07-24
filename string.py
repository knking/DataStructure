##)1. Write a basic program to take input (String)	from User and just print it.
# s=input("Enter string : ")
# print("you entered-->",s)

##)2. Write	a program to count the number of occurrences of	each character	in the string and print	it.

#n="krishnanand"
# test_char={}
# for i in n:
#     if i in test_char:
#         test_char[i]+=1
#     else:
#         test_char[i]=1
# print(str(test_char))

# # Using counter method
# from collections import Counter
# result=Counter(n)
# print(result)

# # using set and counter
#
# res={i : n.count(i) for i in set(n)}
# print(res)

#3)3. Write	a program to remove	all	whitespaces	in a given string.

# def remove(s):
#     return s.replace(" ","")
# s="kris hna    k"
# print(remove(s))

# def remove(s):
#     return "".join(s.split())
# s="h i i,  h o w, are, yo u"
# print(remove(s))

#4.)Find Duplicate characters in a string.

n="geeksforgeeeks"
# lst={}
# for i in n:
#     if i in lst:
#         lst[i]+=1
#     else:
#         lst[i]=1
#
# for key,value in lst.items():
#     if value >1:
#         print(key,end="")
# print()

from collections import Counter

def find_duplicates(n):
    elements = Counter(n)
    return ([k for k,v in elements.items() if v>1])
print(find_duplicates(n))
