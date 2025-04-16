import matplotlib.pyplot as plt
import numpy as np
vector_1 = np.asarray([0,0,5,8])
vector_2 = np.asarray([0,0,-3,-6])
vector_3 = vector_1 + vector_2
print(vector_3)
plt.quiver(0,0,5,8,scale_units = 'xy', angles = 'xy', scale = 1, color='green')
plt.quiver(0,0,-3,-6,scale_units = 'xy', angles = 'xy', scale = 1, color='blue')
plt.quiver(0,0,2,2,scale_units = 'xy', angles = 'xy', scale =  1, color='purple')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()


matrix_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_b = np.array([[10,11,12], [13,14,15], [16,17,18]])
cross_product = np.cross(matrix_a,matrix_b)
print(cross_product)


temperature = np.array([100, 150, 200, 250, 300, 350, 400])
k = np.array([2.078e-4, 2.176e-4, 2.229e-4, 2.260e-4, 2.281e-4, 2.316e-4, 2.331e-4])
x = 1/temperature
y = np.log(k)

z = np.polyfit(x,y,1)
print(z)

f = np.poly1d(z)

plt.plot(x,y,'y*')
plt.plot((0,max(x)),(f(0),f(max(x))),"purple")
plt.show()

A = np.exp(z[0])
print(A)

Ea = -1*z[1]*1.38e-23
print(Ea)
