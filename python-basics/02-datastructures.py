# 1. Lists >>> 
# duplicates are allowed in python lists 
#lists are mutable in python

age = 25
my_list = ["om" , True , age , 69 , 63.336]
print(my_list)

#indexing in list 
# forward 0 - >>  n-1   (left to right)
# backward -n  -->>  -1   (left to right)
leng = len(my_list)
for i in range(0,leng):
    print(my_list[i])

my_list[0] = "arrav"
print(my_list)
my_list.append("Yash")
print(my_list)
my_list.remove("Yash")
print(my_list)
my_list.insert(3,"Banana")    # insert at that index 0 based
print(my_list)

lists = [6,8,5,5,3,55,0]
print(lists.count(5))
print(lists.index(55))
lists.sort()
print(lists)
lists.reverse()
print(lists)

newlists = lists
print(newlists)



#Dictinaries >>>  like a map that has the key value pairs right 
person = {
    "name" : "om",
    "age" : 20,
    "city" : "Pune"
}
print(person)
print(person["name"])
person["name"] = "gholap"
print(person)
del person["city"]
print(person)

#Tuples 
#They are immutable right 
#Others things are same
t1 = (2,3,5)
t2 = ("om" , 12 , True )
print(t1)
print(t2)

# t2[2] = False     # this will respond the error as tuples are immutable right


# Set 
# Set is nothing but the list only but wwith the unique values 
# it allows no duplicates here 
#always stores data in the sorted order
set1 = {1,2,3,5,5,8,1,1}
print(set1)
set2 = {"om" , "python" , "gholap"}      
print(set2)   

#lists as the sets 
lx = [45,32,89,89,63]
sx = set(lx)
print(sx)