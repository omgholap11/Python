# Variables 
# for naming convention in python snake_case is preffered 
name = "om"
age = 25
cgpa = 6.5
is_student = True

#Arithmetic Operations 
sum = 4 + 5
a = 2
b = 3
c = a - b
print(c)
d = a + b
print(d)
e = a * b
print(e)
f = a/b       #  float value 
print(f)
g = a//b        # floor value
print(g)
h = a ** b       # powwer
print(h)       


#strings 
name = "python is crazy for aiml!"
print(name)

description = """This is the
                    Multilinbe string i can customize 
                        it as per my wish"""
print(description)

first = "om"
last = "gholap"
full = first + " " + last
print(full)

long_starline = "*" * 10
print(long_starline)
print(len(long_starline))

#formated strings 
name = "om"
string = "Welcome to python!"
final = f"Hello {name} and {string}"
print(final)

#built in methods in strngs 
name = "Python is interesting"
name.lower()
name.upper()
#and many more just keep checking docs and chatgpt right !!



#operators 
is_flag = 45 >= 35
print(is_flag)          #True 
is_flag = 45 < 35
print(is_flag)        #False


# Control Structures 
a = 5
b = 10
if (a > b) and is_flag :
    print("Hello Python in if")
elif (a < b) and (is_flag == False):
    print("Hello Python Python in elif!")
else:
    print("Hello py on else!")


# Control Flow in Python here >>>
for i in range(1,6):       # 1 - 5   [a,b)
    print(i)

print("------------------------")


for i in range(1,10,2):        #jumps with gap of the 2
    print(i)