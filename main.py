import numpy as np
import matplotlib.pyplot as plt
print('Prosze wpisac wspolczynniki zalamania z zakresu: [0.25; 1.75]')
n1=float(input('Wspolczynnik zalamania w osrodku 1:'))
if n1<0.25 or n1>1.75:
    raise IOError
n2=float(input('Wspolczynnik zalamania w osrodku 2:'))
if n2<0.25 or n2>1.75:
    raise IOError

#7.12.2021r.

x1=np.linspace(-20, 0, 50)
x=np.linspace(-20, 20, 100)

a=float(input('Prosze podac kat padania (w stopniach) :'))
#promien padajacy:
y1=x1*np.tan(a*np.pi/180)
y=np.zeros(100)

#14.12.2021r.
x2=np.linspace(0, 20, 50)
b=np.arccos((n1/n2)*np.cos((a*np.pi/180)))
#promien zalamany:
y2=np.tan(b)*x2
c=np.arctan(np.tan((180-a)*np.pi/180))
#promien odbity:
y3=np.tan(c)*x2
plt.plot(x, y, lw=8)
plt.plot(x1, y1, lw=2, color='b')
plt.plot(x2, y2, lw=2, color='g')
plt.plot(x2, y3, lw=2, color='b')
plt.text(-20, 17, '1')
plt.text(-20, -3, '2')
plt.show()