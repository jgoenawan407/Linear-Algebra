import copy
import matplotlib.pyplot as plt
from matrix_arithmetic import *

# transition matrix
T = [[0.75, 0.25, 0, 0, 0, 0, 0, 0],
	[0.25, 0.5, 0.25, 0, 0, 0, 0, 0],
	[0, 0.25, 0.5, 0.25, 0, 0, 0, 0],
	[0, 0, 0.25, 0.5, 0.25, 0, 0, 0],
	[0, 0, 0, 0.25, 0.5, 0.25, 0, 0],
	[0, 0, 0, 0, 0.25, 0.5, 0.25, 0],
	[0, 0, 0, 0, 0, 0.25, 0.5, 0.25],
	[0, 0, 0, 0, 0, 0, 0.25, 0.75]]

# initial velocities
v = [[1.5], [1.6], [1.7], [1.8], [1.75], [1.65], [1.55], [1.45]]
# v_2 = [[1.8], [1.75], [1.70], [1.65], [1.73], [1.78], [1.83], [1.86]], even when highest speeds aren't in the middle, system still smooths out

print('Original velocity vector: \n' + str(v))

iterations = 40 # no. of times we operate on velocities

state = mult(T, v) # velocities after 1 transformation
x_coords = [0 for i in range(iterations + 1)] # 0 - 40
all_velocities = [([0] * (iterations + 1)) for i in range(len(v))] # 8 arrays, one for each lane

for i in range(len(v)):
	all_velocities[i][0] = v[i][0] # initial velocities

for i in range(iterations):

	x_coords[i] = i # populating the 0 - 40
	state = mult(T, state) # next velocity vector

	for j in range(len(v)):
		all_velocities[j][i + 1] = state[j][0] # putting velocities into corresponding spot in complete matrix

x_coords[iterations] = iterations

plt.xlabel('Iterations (3/4 seconds)')
plt.ylabel('Velocity (m/s)')
plt.title('Velocity over 30 Seconds')

colors = ['b', 'r', 'g', 'c', 'm', 'y', 'black', 'orange']

for i in range(len(v)):
	
	plt.plot(x_coords, all_velocities[i], color = colors[i], marker = 'o') 

plt.show()