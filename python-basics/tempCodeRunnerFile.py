def simple_function():
    numbers = [1,2,3,4,5]
    first = "om"
    last = "gholap"
    return numbers , first , last

# print(simple_function())     #error 
# call with same number of variables right 
a , b , c = simple_function()
print(a)
print(b)
print(c)