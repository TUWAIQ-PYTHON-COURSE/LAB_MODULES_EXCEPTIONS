def addition(x, y):
    x = 10
    y = 20
    print("Addition:", x + b)

try:
    addition(10, 20)
except NameError:
    print("you have undefined variable")
else:
    print("The operation is successful")