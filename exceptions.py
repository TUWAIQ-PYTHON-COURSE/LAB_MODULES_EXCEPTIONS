def additoin(x, y):
    try:
        x = 10
        y = 20
        print("Addition:", x + y)
    except Exception as e:
        print('The operation failed. error is : ',e.__class__)
    else:
        print("the operation is successful")

additoin(10, 20)