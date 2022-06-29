# 1) We can create empty list object as follows..
# l=[]
# l.append(10)
# l.append(20)
# l.append("Sudhir")
# l.append(True)
# print(l)
# print(type(l))
#
# ) With Dynamic Input:
# l=eval(input("Please enter the list:"))
# print(l)
# print(type(l))
#
# List with range function
# l=list(range(0,10,2))
# print(l)
# print(type(l))
#
# s="Sudhir"
# l=list(s)
# print(l,type(l))
#
# s="Bhosale Sanajy Bhosale Hippargarao"
# l=s.split()
# print(l,type(l))
#
# Indexing in python
#
# l=[10,20,30,40,50,60]
# print(l[0])
# print(l[-1])
#
# Slicing in python
#
# s=[10,20,30,40,50,60,70,80,90,1,2,3,4,6,7,89,3]
# print(s[0:10:2])
# print(s[4:20:1])
# print(s[4:2:-1])
#
# n = [0,1,2,3,4,5,6,7,8,9,10]
# # i = 0
# # while i < len(n):
# for i in n:
#     print(n[i],end=", ")
#     # i=i+1
#
# To display only Even Numbers:
#
# a=[10,20,30,40,50,60,70,3,5,7]
# for i in a:
#     if i%2==0:
#         print(i,end=" ")
#
# To get information about list:
#
# l=[10,20,30,4,5,6,7,8,9,3,2,3,4,5,6,10]
# # print(len(l))
# print(l.count(10))
#
# Append:---
#
# s=[]
# s.append("Sudhir")
# s.append(1)
# s.append(True)
# s.append(False)
# print(s)
#
# To add all elements to list upto 100 which are divisible by 10
#
# l=[]
# for i in range(101):
#     if i%2==0:
#         l.append(i)
# print(l)
#
# insert()
#
# l=[10,2,30,40,5,8]
# l.insert(0,1)
# l.insert(-1,200)
# print(l)
#
# #extend()
#
# a=[1,20,3,4,5,6,7,7,5,9]
# b=[10,3,4,5,6,10]
# a.extend(b)
# # print(a)
# name=["s","u","d","h","i","r"]
# surname=["b","h","o","s","a","l","e"]
# name.extend(surname)
# print(name)
#
# remove() Function:
#
# name=["s","u","d","h","i","r"]
# name.remove("u")
# print(name)
#
# pop() Function:
#
# n=[10,20,30,40]
# n.pop()
# print(n)
#
# #reverse():
# n=[10,20,30,40]
# n.reverse()
# # print(n)
# n = [20,5,15,10,0]
# n.sort()
# print(n)
#
# s = ["Dog","Banana","Cat","Apple"]
# s.sort()
# print(s)
#
# n = [40,10,30,20]
# n.sort(reverse = True)
# print(n)
#
# #Aliasing and Cloning of List Objects:
# x=[10,20,30,40]
# y=x.copy()
# y.append(100)
# print(x)
# print(y)
#
# ) Repetition Operator (*)
#
# x = [10, 20, 30]
# y = x*3
# print(y)
#
# x = ["Dog", "Cat", "Rat"]
# y = ["Dog", "Cat", "Rat"]
# z = ["DOG", "CAT", "RAT"]
# print(x == y)
# print(x == z)
# print(x != z)
#
# n=[10,20,30,40]
# print(10 in n)
# print (10 not in n)
#
# n=[10,20,30,40]
# print(n)
# n.clear()
# print(n)
#
# vowels=['a','e','i','o','u']
# word=input("Enter the word to search for vowels: ")
# found=[]
# for letter in word:
#  if letter in vowels:
#   if letter not in found:
#     found.append(letter)
# print(found)

# Exercise 1: Reverse a list in Python
#  Reverse a list in Python
# Given:
# list1 = [100, 200, 300, 400, 500]
# Expected output:
#
# [500, 400, 300, 200, 100]
# list1 = [100, 200, 300, 400, 500]
# # d=list1[::-1]
# # print(d)
# list1.reverse()
# # output="".join(d)
# print(list1)

# # Exercise 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # Expected output:
# #
# # ['My', 'name', 'is', 'Kelly']
# for i in list1:
#     for j in list2:
#         list3=i+j
#
#     print(list3,end=" ")
# print(list3)

# Exercise 3: Turn every item of a list into its square
# l=[1,2,3,4,5,6,7,8,9]
# s=[]
# for i in l:
#     d=i*i
#     s.append(d)
# print(s)
# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# for i in list1:
#     for j in list2:
#         d=i+j
#         print(d,end=" ")
# Exercise 5: Iterate both lists simultaneously
# list1 = [10, 50, 30, 40]
# list2 = [100, 200, 300, 400]
# color= ["Red","Blue","Yellow","Black"]
# for (a,b,c) in zip (list1,list2,color):
#     print(a,b,color)

