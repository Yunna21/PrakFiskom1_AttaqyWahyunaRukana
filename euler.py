import numpy as np
def integrate (F,x,y,xStop,h):

    def euler(F,x,y,h):
        K0 = h*F(x,y)
        return K0

    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x <xStop:
        h = min(h,xStop - x)
        y = y + euler(F,x,y,h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X),np.array(Y)
