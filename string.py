
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
#     nw=[i[::-1]for i in w]
#     ns=" ".join(nw)
#     return ns
# s1="king krishna"
# print(rev(s1))

# def reverserWords(string):
#       st = list()
#       for i in range(len(string)):
#             if string[i] != " ":
#                   st.append(string[i])
#             else:
#                   while len(st) > 0:
#                         print(st[-1], end="")
#                         st.pop()
#                   print(end=" ")
#
#       while len(st) > 0:
#             print(st[-1], end="")
#             st.pop()
#
# string="geeks for"
# reverserWords(string)

##10) program to check if a string is palindrome or not

# string=input(("Enter a string:"))
# if(string==string[::-1]):
#       print("The string is a palindrome")
# else:
#       print("Not a palindrome")
#
# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")

# #11.Write a Code to check whether one string is a rotation	of another
#
# def check_rotation(s1,s2):
#      size1=len(s1)
#      size2=len(s2)
#      if size1!=size2:
#            return 0
#      temp=s1+s2
#      if temp.count(s2)>0:
#            return 1
#      else:
#            return 0
# s1="abcd"
# s2="acda"
# if check_rotation(s1,s1):
#       print("String are rotation of each other")
# else:
#       print("Strig are not rotation of each other")


# #12)Write a program to	remove	Duplicate characters from the String
# s="geeksforgeeks"
# s=" ".join(set(s))
# print(s.replace(" ",""))

# s="krishnanand"
# i=0
# s1=""
# for x in s:
#       if s.index(x)==i:
#             s1+=x
#       i+=1
# print(s1)

##13) Interleaving of two given strings with no common characters

# def isInterleaving(a,b,c):
#     i=0
#     j=0
#     k=0
#     while k !=len(c)-1:
#         if i< len(a) and a[i]==c[k]:
#             i+=1
#         elif j < len(b) and b[j]==c[k]:
#             j+=1
#         else:
#             return 0
#         k+=1
#     if a[i-1] or b[j-1]:
#         return 0
#     return 1
# a="ab"
# b="cd"
# c="abcd"
# if isInterleaving(a,b,c)==1:
#     print("Interleaving")
# else:
#     print("Not interleaving")
#
# ##)interiving of strinng
# s1='aaabb'
# s2='cd'
# s=list(s2)
#
# for i,c in enumerate(s1):
#     s.insert(i*2,c)
# print(''.join(s))
#
#
#00) Check palindrom or not

#def pal(a,s,e):
#     while s <=e:
#         if a[s]==a[e]:
#             s+=1
#             e-=1
#             return True
#         else:
#             return False
# a='aabbaa'
# s=0
# e=len(a)-1
# print(pal(a,s,e))

##)Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#"A man, a plan, a canal: Panama" is a palindrome.


#) Given the array of strings A,
# you need to find the longest string S which is the prefix of ALL the strings in the array.
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
# and S2.
# For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".




# The count-and-say sequence is the sequence of integers beginning as follows:


#15) Longest palindromic sub string(Brute force apporach)
# def longestPalindrome( s):
#     """
#     :type s: str
#     :rtype: str
#     """
#
#     def isPalindrome(s):
#         left = 0
#         right = len(s) - 1
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
#
#     if len(s) == 1:
#         return s
#
#     if len(s) < 1:
#         return ""
#
#     maxSubstring = s[0]
#     for i in range(len(s)):
#         currentSubstring = s[i]
#         for j in range(i + 1, len(s)):
#             currentSubstring += s[j]
#             if (isPalindrome(currentSubstring) and
#                     len(currentSubstring) > len(maxSubstring)):
#                 maxSubstring = currentSubstring
#
#     return maxSubstring
# str='ashdkabajjseiw'
# print(longestPalindrome(str))
#

##16) Reverse each word in a string

# def reverse(str):
#     reversedString=''
#     for i in str:
#         reversedString=i+reversedString
#     print("Reversed string is : ",reversedString)
#
# str=input("Enter string : ")
# print("Entered string : ",str)
# reverse(str)

# s='google how are you'
# print(''.join(s[::-1]))



#17) Reverse whole string from a sentence
# sentence = sentence = "dread it run from it destiny still arrives"
# print(' '.join(sentence.split()[::-1]))

##18) longest comman frefix

# def longestCommanprefix(str):
#     if len(str)==0:
#         return ""
#     minlen=len(str[0])
#     for i in range(len(str)):
#         minlen=min(len(str[i]),minlen)
#     lcp=''
#     i=0
#     while i < minlen:
#         char=str[0][i]
#         for j in range(1,len(str)):
#             if str[j][i]!=char:
#                 return lcp
#
#         lcp=lcp+char
#         i=i+1
#     return lcp
# str=["geeksforgeeks", "geeks","geek", "geezer"]
# print(longestCommanprefix(str))




