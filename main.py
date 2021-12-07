import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
print('Prosze wpisac wspolczynniki zalamania z zakresu: [0.25;1.75]')
n1=float(input('Wspolczynnik zalamania w osrodku 1:'))
if n1<0.25 or n1>1.75:
    raise IOError
n2=float(input('Wspolczynnik zalamania w osrodku 2:'))
if n2<0.25 or n2>1.75:
    raise IOError

root=tk.Tk()
x=np.linspace(-20, 20)
'''a=tk.Scale(root, from_=-5, to=5, resolution=0.01, orient='horizontal')
a.pack()'''
a1=float(input('Prosze podac kat padania:'))
y1=x*np.tan(a1*np.pi/180)
y2=np.zeros(50)
plt.plot(x, y1, lw=2)
plt.plot(x, y2, lw=8)
plt.text(-20,20, '1')
plt.text(-20, -3, '2')
plt.show()