# merge two dictionaries

d1={"a":10,"b":20,"c":30,"d":40}
d2={"e":40,"f":50,"g":60}
# #with method
# # d1.update(d2)
# # print(d1)
# # with loop
# for i in d2:
#     d1[i]=d2[i]
# print(d1)


# sum all values in a dictionary
# add=0
# for i in d1:
#     add=d1[i]+add

# print(add)
    
# #Count the frequency of each element in a list using a dictionary.
# l=["a","b","a","c","b","a"]
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]=d[i]+1 
#     else:
#         d[i]=1
# print(d)  
   

# #Combine two dicts, adding values for common keys.
# d1={"a":10,"b":20,"c":30,"e":40}
# d2={"e":40,"f":50,"g":60}

# for i in d2:
#     if i in d1.keys():
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i] = d2[i]
    
# print(d1)


# More Questions

#Find the largest Number in dictionary
d = {"a": 15, "b": 42, "c": 27, "d": 9}
largest=0
for i in d:
    if d[i]>largest:
        largest=d[i]
print(largest)

# Create a new dictionary containing only values greater than 10
d = {"a": 5, "b": 15, "c": 8, "d": 20, "e": 12}
n={}
for i in d:
    if d[i]>10:
        n[i]=d[i]
print(n)

# Count how many key-value pairs are in the dictionary using a loop
d = {"apple": 3, "banana": 5, "mango": 2, "orange": 7}
count=0
for i in d:
    count=count+1
print(count)    

# invert a dictionary
d = {"a": 1, "b": 2, "c": 3}
n = {}
for i in d:
    n[d[i]] = i
print(n)

# find common keys
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 8, "d": 12}

for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]

print(d1)

# count the frequency
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
e={}
for i in words:
    if i in e.keys():
        e[i]=e[i]+1
    else:
        e[i]=1
print(e)

# Separate even and odd values
d = {"a": 4, "b": 7, "c": 10, "d": 13, "e": 6}
even={}
odd={}
for i in d:
    if d[i]%2==0:
        even[i]=d[i]
    else:
        odd[i]=d[i]

print(f"Here are the even ones: {even}")
print(f"Here are the odd ones: {odd}")

# Find the key with the largest value
d = {"Ali": 78, "Sara": 92, "Ahmed": 85, "Zoya": 88}
largest=0
larg_key=0
for i in d:
    if d[i]>largest:
        largest=d[i]
        larg_key=i

print(larg_key)

#Merge dictionaries by multiplying common values

d1 = {"a": 2, "b": 3, "c": 4}
d2 = {"b": 5, "c": 6, "d": 7}

for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]*d2[i]
    else:
        d1[i]=d2[i]
print(d1)


# Remove duplicate values
d = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
n = {}

for i in list(d):
    dup = d[i]

    if dup in n.values():
        del d[i]
    else:
        n[i] = dup

print(d)  

        







