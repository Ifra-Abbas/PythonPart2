# # list questions
# #level 2
# # Given numbers = [10, 20, 30, 40, 50], add 60 to the list

# l1=[10, 20, 30, 40, 50]
# l1.append(60)
# print(l1)

# # remove 3 form the list
# l2=[1,2,3,4,5]
# l2.remove(3)
# print(l2)

# # print length of the list
# l3=[1,2,3,4,5]
# print(len(l3))

# # sort the list in ascending order
# l4=[5, 2, 8, 1, 9]
# l4.sort()
# print(l4)

# # print the last three
# l5=[10, 20, 30, 40, 50]
# print(l5[2:6])

# # level 3

# # sum of numbers 
# l6=[10, 20, 30, 40, 50]
# sum=0
# for i in l6:
#     sum=sum+i
# print(sum)

# # count how many even number are there
# l7=[1, 2, 3, 4, 5, 6, 7, 8]
# count=0
# for i in l7:
#     if(i%2==0):
#         count=count+1
# print(count)

# # find the largest number 
# l8=[12, 45, 7, 89, 23]
# largest=0
# for i in range(0,len(l8)):
#     if l8[i]>largest:
#         largest=l8[i]
# print(largest)

# # Create a new list containing only numbers greater than 10 from 
# l9=[5, 12, 8, 20, 15, 3]
# l=[]
# for i in l9:
#     if i>10:
#         l.append(i)
# print(l)

# #Reverse [1, 2, 3, 4, 5]
# l10=[1, 2, 3, 4, 5]
# reversed_list=l10[::-1]
# print(reversed_list)

#level 4

#Find the second-largest distinct number in `[10, 40, 20, 40, 30]`
l11=[10, 40, 20, 40, 30]
largest=0
second_largest=0
for i in l11:
    if i>largest:
        second_largest=largest
        largest=i
    elif largest>i>second_largest:
        second_largest=i
print(f"the largest number is {largest} and the second largest number is {second_largest}")
#Remove duplicate values from `[1, 2, 2, 3, 4, 4, 5]`, preserving their original order.
l12=[1, 2, 2, 3, 4, 4, 5]
# solution #1
i=0
while i < len(l12):
    if l12[i] in l12[:i]:
        l12.pop(i)
    else:
        i +=1
# solution #2
l12=list(dict.fromkeys(l12))
print(l12)
# all zeros to end
#this approach is not better 
l13=[0, 1, 0, 3, 12]
for i in range(0,len(l13)):
    if l13[i]==0:
        l13.pop(i)
        l13.append(0)
print(l13)

# this one better:
non_zeros = []
zeros = []
for i in l13:
    if i == 0:
        zeros.append(i)
    else:
        non_zeros.append(i)

l13 = non_zeros + zeros
print(l13)

#Find the common elements in `[1, 2, 3, 4]` and `[3, 4, 5, 6]`
d1=[1, 2, 3, 4]
d2=[3, 4, 5, 6]
common=[]
for i in d1:
    for b in d2:
        if i==b:
            common.append(i)
print(common)

#Rotate `[1, 2, 3, 4, 5]` one position to the right.


l15 = [1, 2, 3, 4, 5]
l15 = [l15[-1]] + l15[:-1]
print(l15)