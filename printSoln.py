def printSoln (X,Y,freq):

    def printHead(n):
        print ("\n         x  ",end=" ")
        for i in range (n):
            print ("\n         y[",i,"] ",end=" ")
            print()


    def printLine(x,y,n):
        print("%13.4e"% x,end=" ")
        for i in range (n):
            print("%13.4e"% y[i],end=" ")
        print()

    m = len(Y)
    try: n = len(Y[0])
    except TypeError: n = 1
    if freq == 0: freq = m
    printHead(n)
    for i in range (0,m,freq):
        printLine(X[i],Y[i],n)
    if 1 != m - 1:printLine(X[m - 1],Y[m - 1],n)
