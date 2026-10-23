# #Sets ---> Unique Values

# a={} # if it is has no value than t condsider as dictionary
# print(type(a)) #<class 'dict'>

# b={1,2,3,4}
# print(type(b)) #<class 'set'>

# #convert any tuple and list into set to remove dublicates

# l=[1,1,1,2,2,2,3,3,4,4,5,5]
# s=set(l)
# print(s)# {1, 2, 3, 4, 5}

# #--> how sets save there is hollow space in memory and every element saves in the form of hash 
# # how hash look like

# g="hello"
# print(hash(g)) #5753764415901926668

# e={1,"ifra",(5,66,7)} # set don't allow to store the list bcz it is mutable nad it can change the hash
# #sets are unordered we can get the elements through the indexes
#  # loop 
# # we can not apply range function on this as it is un-ordered
# w={10,20,30,40,50}
# for i in w:
#     print(i) #50 20 40 10 30 ---> unordered
# # used in set maths operations 
# # methods
# # w.add(70)
# # print(w)
# # w.clear()
# # print(w)
# w.discard(40)
# print(w) #{50, 20, 10, 30}

# w.pop() # remove an element from set that element is random
# print(w) #{20, 10, 30}



# Maths Operations

s1={10,20,30,40,50}
s2={20,30,40,90,70}
s3={30,70}
# print(s1.difference(s2))
# print(s2.difference(s1))
# print(s1-s2)

# # calculate the difference also update the set with the values we gain from difference
#  # -=
# s1-=s2
# print(s1) # s1 now becomes {50, 10}

# #interesection of sets
# print(s1.intersection(s2)) # common ones {40, 20, 30}

#is subset --. return if all elements are present on other set

# print(s3.issubset(s1)) #False
# print(s3<=(s2)) #True

# is super set reverse of issubset

# symmetric difference removes the common one and return different ones form both sets
print(s1.symmetric_difference(s2)) # {50, 10, 70, 90}
print(s1^(s2)) # {50, 10, 70, 90}

#union

print(s1|s2)

