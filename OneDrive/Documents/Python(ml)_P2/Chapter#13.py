#Tuple: is exactly like a list but we cannot change it as it is immutable

# a=("monday","tuesday",123,453)
# print(a)
# print(type(a))

# l=[1,2,4,56,6] # its a list
# tup=tuple(l)
# print(type(tup)) # now make a tuple from the list

# tuple methods only two methods we have in tuple
# 1- index
# t=[1,2,3,4,5,5,5]
# i=t.index(3) # at what index the element 3 placed
# print(i)
# # 2- count 
# c=t.count(5) # check how many time the number appears in the tuple
# print(c)

# Real life use case of the tuple??
# tuple packing and unpacking

def  student():
    return "ifra",24,"ifra@gmail.com" #python consider it as tuple
info=student()
print(type(info))
#unpacked
name,age,mail=info
print(name)
a=23,45,67 # python consider it as a tuple
print(type(a))
