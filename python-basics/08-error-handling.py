#try and except blocks just like the try catch block 
try:
    results = 10/6
    print(results)     #  will be print as no error
    results = 10/0
    print(results)   #  will not get print instead will get caught in the except block
except:
    print("Hey error caught!!")