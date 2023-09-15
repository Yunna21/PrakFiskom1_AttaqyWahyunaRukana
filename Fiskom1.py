import numpy as np
from printSoln import *
from euler import *
import matplotlib.pyplot as plt

g=9.8

def F(x,y):
    F = np.zero(2)
    F[0] = y(1)
    F[1] = g
    return F

x = 0.0
xStop = 10.0
y = np.array([0.0,0.0])
h = 0.1
freq = 1

X,Y = integrate(F,x,y,xStop,h)

Yexact = (1/2)*g^X*X;

print("--Solusi PDB Menggunakan Metode Euler--")
print("---------------------------------------")
printSoln(X,Y,freq)
print("---------------------------------------")

plt.plot(X,Y[:0],'o',X,Yexact,'-')
plt.grid(True)
plt.title('Grafik Gerak Jatuh Bebas tanpa Gesekan Udara')
plt.xlabel('Waktu(s)');plt.ylabel('Posisi, y(m)')
plt.show()
input("Please Return to exit")
