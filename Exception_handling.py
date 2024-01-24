def geo(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Kuna kashida kiasi")
        
print(geo(0))
# we can use the try clause to try and test some parts of code that may cause errors