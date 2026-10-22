# #List --> heterogeneous as we can add any type of data unlike arrays
# a=[1,2,3,4]
# print(type(a))

# # there are some special power of list 
# # 1- it is ordered 
# print(a[1])
# print(a[-1])

# #2- it is mutable
# a[2]=50
# print(a)

# #3- duplicate values
# a=[2,34,54,54,65,65]

# #traversing of list
# b=[2,4,6,76,542,3,5]
# #traversing on values
# for i in b:
#     print(i)
# #traversing on index
# for i in range (0,len(b)):
#     print(i)

#list methods
# c=[10,20,30,40,60]
#tell us all the methods of the list 
# # print(dir(list))
# # add an elements at the end of the array
# c.append(60)
# print(c)
# # adds an element at any index
# c.insert(4,50)
# print(c)

# l=[10,20,30,40,55,60]
# removes from first
# l.remove(55) # take the value that you wnat to remove if that value repeats then it just remove the first one
# print(l)
# #remove from last by default(also add specific one) and also return that element
# # l.pop(4)
# # print(l)

# clear remove all he elements of a list
# lst=[1,2,3,4,5]
# lst.clear()
#sort
# t=[51,27,36,44,87,12]
# print(t)
# #ascending
# t.sort()
# print(t)
# #decending
# t.sort(reverse=True)
# print(t)

# Now sole some questions

#Q1: Print all postive and negative elements of a list separately

# l1=[0,1,-2,3,-4,5]
# p=[]
# n=[]
# for i in l1:
#     if i>0:
#         p.append(i)
#     elif i<0:
#         n.append(i)
#     else:
#         print("The number is 0")
# print(f"The positive Numbers are:{p}")
# print(f"The negative numbers are:{n}")

#Q2 find mean of the list elements

# l2=[20,37,68,90,37]
# sum=0
# mean=0
# for i in l2:
#     sum=sum+i
# mean=sum/len(l2)
# print(f"The mean of all elements is:-{mean}")    

#Q3: find the greatest number and return its index

# l3=[23,45,78,98,56]
# n=0
# index=0
# for i in range(0,5):
#     if l3[i]>n:
#         n=l3[i]
#         index=i

# print(f"The greatest number is: {n} at the index: {index}")

#Q4: find the second greatest number in the list

# l4=[4,7,2,9,1,8]
# largest=0
# second_largest=0
# for i in l4:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif i>second_largest:
#         second_largest=i

# print(f"The second largest number is: {second_largest}")        
 
#Q#5 check that if the list is sorted or not?
# l5=[23,45,12,56,78]
# l5=[1,2,3,4,5]
# for i in range(0,len(l5)-1):
#     if l5[i]>l5[i+1]:
#         print("The list is not sorted")
#         break
# else:
#     print("list is sorted")
    

