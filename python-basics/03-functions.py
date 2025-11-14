#Functions 
def sum(a , b):
    print("You are inside the function!")
    return a+b

res = sum(4,5)
print(res)


def greet():
    print("Hello python!")
    pass        # pass means returs nothing u can also use just simple return  

greet()

def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

def factorial(n = 5):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))
print(factorial())      # takes default value provided in parameters i.e 5


#Returning the values 
# use return statement 
#Returning the multiple values 
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

# Global and the local variables >>>>
#local varibles are var in the function they cannot be used outside the function 
# while local cann be used through out the program 

discount = 69    # global variable 
def calc():
    profit = 63
    return discount * 0.2

# print(profit)   # local variable so cannot be accessed here 