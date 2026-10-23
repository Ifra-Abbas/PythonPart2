# # Dictionary --> key-values pairs

# d={}
# print(type(d)) # <class 'dict'>
# dic={1:10,2:20,3:30,4:40} # 1,2,3,4---> keys means we are creating custom indexing
# print(dic[3]) # 30 

# # if we give that key which does'nt exits it gives error KeyError
# #CRUD # Vanilla Python
# #Create
# dic[5]=50
# print(dic) #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
# #Read
# print(dic[4]) # 40 
# #Update
# dic[1]=0
# print(dic) #{1: 0, 2: 20, 3: 30, 4: 40, 5: 50}


# #methods 
# d1={1:10,2:20,3:30,4:40}
# # d1.clear()
# # print(d1) #{}

# # q=d1.fromkeys([10,20,40,80],90)
# # print(q)
# # items -->tuple
# print(d1.items())
#  # keys return keys but in the list
# print(d1.keys()) #dict_keys([1, 2, 3, 4])
# #values
# print(d1.values())
# pop specfic
# print(d1.pop(2))
# #pop item remove last
# print(d1.popitem())

# d1.setdefault(60,300)
# print(d1)

# d1.update({1:1000})
# print(d1)


# #traversing:
# d={1:10,2:20,3:30,4:40}

# for i in d:
#     print(f"{i}-->{d[i]}")

#  Dictionay Questions
# d1={1:10,2:20,3:30,4:40}
# d2={5:50,6:60,7:70,8:80}

#Q1 merge two dictionaries into 1
# d1.update(d2)
# print(d1)

# for i in d2:
#     d1[i]=d2[i]
# print(d1)

#Q2 sum of all values in the dictionary
# sum=0
# for i in d1:
#     sum=sum+d1[i]
# print(sum)

#Q3 counting the frequency of each element in the dictionary
# l=["a","b","a","c","b","a","c","a","b"]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1
#     else:
#         d[i]=1

# print(d)

#Q4 combine two dicts and add common values
 
# d1={1:10,2:20,3:30,4:40}
# d2={4:50,6:60,7:70,8:80}

# for i in d2:
#     if i in d1.keys():
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d2[i]

# print(d1)




