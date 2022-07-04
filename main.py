#[1]
from dateOP import printDate

printDate()

#[2]

def additoin(x, y):
          x = 10
          y = 20
          print("Addition:", x + b)
try:
    additoin(10,20)
except NameError:
    print("You have undefined variable/s")
else:
    print("The operation is successful")