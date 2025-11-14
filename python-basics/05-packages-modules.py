#Modeules >>>  single python file 
#Packages >>>  Folder with multiple python files 

#Types of packages 
# 1.  Built in packages 
#2. User defined packages 

import math
print(math.sqrt(16))

from math import sqrt , pi
print(sqrt(25))
print(pi)

import random
number = random.randint(1,10)
print(number)
ch = random.choice(["apple" , "grapes" , "banana"])
print(ch)

import datetime
now = datetime.datetime.now()
print(now)

import os
cdir = os.getcwd()  #current working directory
print(cdir)

#alias
import math as m
print(m.sqrt(81))

# Installing extarnal packages like pandas requests and many more 
import pandas as pd     #pip install packagename

# Managing all packages in the file and togetherly installing them just like package.json in javascript 
# here we have requirements.txt 

# First create requirements.txt
# mention all the packages with there vaersiong 
# when u runs >>  pip install -r requirements.txt    it will install all the packages 
# To mention all packages used in project with there versiona use this comman >>>>>    pip freeze > requirements.txt 


#Using the extarnal packages 
# Web requests
import requests

response = requests.get("https://api.github.com")
data = response.json()
print(data)

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)