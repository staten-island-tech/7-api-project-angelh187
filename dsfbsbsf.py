def divide(a,b):
    try:
        result = a/ b
    except ZeroDivisionError:
        print("Cannot divided by 0")
    else:
        print(result)
divide(10,0)