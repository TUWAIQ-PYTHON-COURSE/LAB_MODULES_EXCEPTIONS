
import dateOP

from dateOP import *

print(dt)


## Below you have a code that raises an exception , using what you learned do the following:
#1- Find what type of exception is raised.
#2- Hanlde the exception in try..except 
#3- If operation successful , print "the operation is successful"
#4- if operation fails, handle the specific exception that is raised , and print a relevant message.



def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)
try:
    additoin(10, 20)
except NameError :
 print("error")
else:
    print("the operation is successful")  

finally:
    print("end of program")
