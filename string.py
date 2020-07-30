
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
# assume the first string of list is minimun and then find the minimum length string
#     minlen=len(str[0])
#     for i in range(len(str)):
#         minlen=min(len(str[i]),minlen)
# take a empty string, then fix first string from a list a compare this with all the string and move the cursor
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


##19) Roman number to integer

# def romantointeger(string):
#     dic={
#         'M': 1000,
#         'D': 500,
#         'C': 100,
#         'L': 50,
#         'X': 10,
#         'V': 5,
#         'I': 1
#         }
#     total=0
#     prev=0
#     curent=0
#     for i in range(len(string)):
#         curent=dic[string[i]]
#         if curent > prev:
#             total=total+curent -2 * prev
#         else:
#             total+=curent
#         prev=curent
#     return total
# str='MCMIV'
# print(romantointeger(str))
#

##)Alternative approach

# def value(r):
#     if (r == 'I'):
#         return 1
#     if (r == 'V'):
#         return 5
#     if (r == 'X'):
#         return 10
#     if (r == 'L'):
#         return 50
#     if (r == 'C'):
#         return 100
#     if (r == 'D'):
#         return 500
#     if (r == 'M'):
#         return 1000
#     return -1
#
#
# def romanToDecimal(str):
#     res = 0
#     i = 0
#
#     while (i < len(str)):
#
#         # Getting value of symbol s[i]
#         s1 = value(str[i])
#
#         if (i + 1 < len(str)):
#
#             # Getting value of symbol s[i + 1]
#             s2 = value(str[i + 1])
#
#             # Comparing both values
#             if (s1 >= s2):
#
#                 # Value of current symbol is greater
#                 # or equal to the next symbol
#                 res = res + s1
#                 i = i + 1
#             else:
#
#                 # Value of current symbol is greater
#                 # or equal to the next symbol
#                 res = res + s2 - s1
#                 i = i + 2
#         else:
#             res = res + s1
#             i = i + 1
#
#     return res

##20)minimum character need to be inserted in the begning to make it palindromic

# def minInsert(string,i,j): #i is start pointer and j is end pointer
#     if i >= j:
#         return 0
#
#     if string[i]==string[j]:  #check character for match if all character match then retun
#         return minInsert(string,i+1,j-1)  ##call funcion again and again with increment in i and decrement in j
#     else:
#         decision1=1+minInsert(string,i+1,j)
#         decision2=1+minInsert(string,i,j-1)
#         return min(decision1,decision2)
#
#     return

##21) Check fo anagrms

#basic method using sorted function(1st method)
# s1="cab"
# s2="abc"
# if sorted(s1)==sorted(s2):
#     print("Anagramas")
# else:
#     print("Not anagrams")

##using loops(2nd method)
#
# lst=[False] * len(s2)
# if len(s1)==len(s2):
#     for i in range(len(s1)):
#         c=s1[i]
#         check=False
#         for j in range(len(s2)):
#             if s2[j]==c and not lst[j]:
#                 lst[j]=True
#                 check=True
#                 break
#         if not check:
#             break
# if check:
#     print("anagrams")
# else:
#     print("not aanagrams")

##another mathod

# from collections import Counter
# s=Counter(s1)
# s3=Counter(s2)
# if s==s3:
#     print("anagrams")
# else:
#     print("not anagrams")

##22) Group anagrams
#method 1
# word_list = ["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]
#
# # initialize a list
# anagram_list = []
# for word_1 in word_list:
#     for word_2 in word_list:
#         if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
#             anagram_list.append(word_1)
# print(anagram_list)

#method 2
#
# def checkAnagrams(lst):
#     dic={}
#
#     for word in lst:
#         sortedword="".join(sorted(word))
#
#         if sortedword not in dic:
#             dic[sortedword]=[word]
#
#         else:
#             dic[sortedword].append(word)
#
#     result=[]
#     for item in dic.values():
#         result.append(item)
#
#     return result
# l=["percussion", "supersonic", "car", "tree", "boy", "girl", "arc"]
# print(checkAnagrams(l))
#

##23) count and say

# def countSay(s):
#     if len(s)==1:
#         return "1"


##24) Comapre versions of number

# def compareVersion(version1,version2):
#     version1=[int(v) for v in version1.split(".") ]
#     version2=[int(v) for v in version2.split(".") ]
#
#     for i in range(max(len(version1),len(version2))):
#         v1=version1[i] if i < len(version1) else 0
#         v2=version2[i] if i < len(version2) else 0
#
#         if v1 > v2:
#             return 1
#         elif v2 > v1:
#             return -1
#     return 0
# a="1.01"
# b="1.001"
# print(compareVersion(a,b))

##another method

# Method to compare two versions.
# Return 1 if v2 is smaller,
# -1 if v1 is smaller,,
# 0 if equal
# def versionCompare(v1, v2):
#     # This will split both the versions by '.'
#     arr1 = v1.split(".")
#     arr2 = v2.split(".")
#     n = len(arr1)
#     m = len(arr2)
#
#     # converts to integer from string
#     arr1 = [int(i) for i in arr1]
#     arr2 = [int(i) for i in arr2]
#
#     # compares which list is bigger and fills
#     # smaller list with zero (for unequal delimeters)
#     if n > m:
#         for i in range(m, n):
#             arr2.append(0)
#     elif m > n:
#         for i in range(n, m):
#             arr1.append(0)
#
#             # returns 1 if version 1 is bigger and -1 if
#     # version 2 is bigger and 0 if equal
#     for i in range(len(arr1)):
#         if arr1[i] > arr2[i]:
#             return 1
#         elif arr2[i] > arr1[i]:
#             return -1
#     return 0

##24) strStr() imlementation

def strstr(haystack,needle):
    if not needle:
        return 0
    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            return i

    return -1
s="hellow"
s1="ll"
print(strstr(s,s1))

