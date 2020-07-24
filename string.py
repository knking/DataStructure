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

##4.)Find Duplicate characters in a string.

#n="geeksforgeeeks"
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

# from collections import Counter
#
# def find_duplicates(n):
#     elements = Counter(n)
#     return ([k for k,v in elements.items() if v>1])
# print(find_duplicates(n))

#)5. Write a program to reverse the string in place.

# def reverse_string(s):
#     return s[::-1]
# s1="king"
# print(reverse_string(s1))

# using join and reverse
# s="anhsirk"
# print(" ".join(reversed(s)))

# def rev(s):
#     if len(s)==0:
#         return s
#     else:
#         rev(s[1:])+s[0]
#
# s="anhsirk"
# print(rev(s))

##6) String to integer and integer to string
# def myAtoiRecursive(string, num):
#     # base case, we've hit the end of the string,
#     # we just return the last value
#     if len(string) == 1:
#         return int(string) + (num * 10)
#         # add the next string item into our num value
#     num = int(string[0:1]) + (num * 10)
#     # recurse through the rest of the string
#     # and add each letter to num
#     return myAtoiRecursive(string[1:], num)
# # Driver Code
# string = "112"
#
# print(myAtoiRecursive(string, 0))
# s="420"
# temp=0
# for i in s:
#     temp=int(i)+temp*10
# print(temp)

#)9.Write  a program  to reverse each word	in	the	given string.
# def rev(s):
#     w=s.split(" ")
#     nw=[i[::]for i in w]
#     ns=" ".join(nw)
#     return ns
# s1="king"
# print(rev(s1))
##10) program to check if a string is palindrome or not

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")
