# Video of NeuralNine
# https://youtu.be/9yuqqpetreA?si=UAy_fOTfD0jgWfke

import matplotlib.pyplot as plt
import math
import numpy as np
# r = 20
# theta = math.pi / 2

# plt.figure(figsize=(6,6))
# ax = plt.subplot(111,polar=True)
# ax.scatter(theta,r)
# plt.show()






# x = 20
# y = 30

# plt.scatter(x,y)
# plt.xlim(0,40)
# plt.ylim(0,40)
# plt.grid()
# plt.show()

# r = math.sqrt(x**2 + y**2)
# theta = math.atan(y/x)

# plt.figure(figsize=(6,6))
# ax = plt.subplot(111, polar = True)
# ax.scatter(theta, r)
# plt.show()




theta = np.linspace(0, 2 *math.pi, 1000)
r = np.exp(np.sin(theta)) - 2 * np.cos(4 * theta) + np.sin((2*theta -np.pi) / 24)**5

plt.figure(figsize=(6,6))
ax = plt.subplot(111,polar=True)
ax.plot(theta, r)
plt.show()

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x,y)
plt.show()