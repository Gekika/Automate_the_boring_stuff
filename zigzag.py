import time,sys
indent = 0
indentIncrease = True

try:
    while True:
        print('' * indent, end='')
        print('************')
        time.sleep(0.5)
        
        if indentIncrease:
            indent = indent + 1
            if indent == 5:
                indentIncreasing = False
        
        else:
            indent = indent - 1
            if indent == 0:
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()            