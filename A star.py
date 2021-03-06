# import packages

##############################################################################

 

import numpy as np

import heapq

import random

import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

# plot grid

##############################################################################

 
grid = np.zeros((10,10), dtype=int)

boulder = [(9,7), (8,7), (6,7), (6,8)]

# start point and goal
start = (0,0)
goal = (9,9)
my_tuples = []

#create all tuples
for i in range(0,10):
    for k in range(0,10):
        my_tuples.append((i,k))
# print(my_tuples[:5])

#remove unwanted tuples
for boulder_tuple in boulder:
    my_tuples.remove(boulder_tuple)
my_tuples.remove(start)
my_tuples.remove(goal)
# print(my_tuples[:5])

#select X number of random tuples from list 
UpdatedList = random.choices(my_tuples, k = 21)
# print(UpdatedList)

boulder.extend(UpdatedList)


for i in boulder:
    grid[i] = 1
    
# print(grid)

# heuristic function for path scoring

##############################################################################

 

def heuristic(a, b): #euclidean distance

    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

# def heuristic(a, b): #manhattan distance

#     return abs(b[0] - a[0]) + abs(b[1] - a[1])

 
# path finding function

##############################################################################

 

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    close_set = set()

    came_from = {}

    gscore = {start:0}

    fscore = {start:heuristic(start, goal)}

    oheap = []

    heapq.heappush(oheap, (fscore[start], start))
 

    while oheap:

        current = heapq.heappop(oheap)[1]

        if current == goal:

            data = []

            while current in came_from:

                data.append(current)

                current = came_from[current]

            return data

        close_set.add(current)

        for i, j in neighbors:

            neighbor = current[0] + i, current[1] + j

            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < array.shape[0]:

                if 0 <= neighbor[1] < array.shape[1]:                

                    if array[neighbor[0]][neighbor[1]] == 1:

                        continue

                else:

                    # array bound y walls

                    continue

            else:

                # array bound x walls

                continue
 

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):

                continue
 

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:

                came_from[neighbor] = current

                gscore[neighbor] = tentative_g_score

                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                heapq.heappush(oheap, (fscore[neighbor], neighbor))
 

    return False

route = astar(grid, start, goal)

route = route + [start]

route = route[::-1]

print(f'Path taken: {route}')
print(f'Number of steps taken: {len(route) -1}')

# plot the path

##############################################################################

 

#extract x and y coordinates from route list

x_coords = []

y_coords = []

for i in (range(0,len(route))):

    x = route[i][0]

    y = route[i][1]

    x_coords.append(x)

    y_coords.append(y)

# plot map and path

fig, ax = plt.subplots(figsize=(20,20))

ax.imshow(grid, cmap=plt.cm.coolwarm)

ax.scatter(start[1],start[0], marker = "d", color = "springgreen", s = 200)

ax.scatter(goal[1],goal[0], marker = "X", color = "red", s = 200)

ax.plot(y_coords,x_coords, color = "black")

plt.show()