#
# Authors: MoHan Zhang and Dhananjay Bhaskar
# Last Modified: 29 Jun, 2017
#

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_data = pd.read_csv('data.csv')
shape_data = pd.read_csv('shape_data.csv')
neighbour_data = pd.read_csv('neighbour_data.csv')

'''
plt.figure(0)
x = csv_data['# TimeStamp']
y = csv_data['Total_Number_Of_Cells']
# plt.plot(x,y, marker='.',linestyle='-', color='r')
plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Total Number Of Cells")
plt.title("Change in Total Number Of Cells Over Time")
plt.savefig('NumCells.png')
'''

plt.figure(1)
x = csv_data['# TimeStamp']
y = csv_data['Average_Area']
plt.plot(x, y, label="Average Area")
plt.xlabel("Time")
plt.gca().legend(loc="upper right")
plt.title("Average Area")
plt.ylim([0.5, 1.0])
plt.savefig('AvgArea.png')

plt.figure(2)
x = csv_data['# TimeStamp']
z = csv_data['Average_Perimeter']
plt.plot(x, z, label="Average Perimeter")
plt.xlabel("Time")
plt.gca().legend(loc="upper right")
plt.title("Average Perimeter")
plt.ylim([2.5, 3.5])
plt.savefig('AvgPerimeter.png')

'''
plt.figure(3)
x = shape_data['# TimeStamp']
plt.plot(x, shape_data['Triangle'], label="Triangle")
plt.plot(x, shape_data['Quadrilateral'], label="Quadrilateral")
plt.plot(x, shape_data['Pentagon'], label="Pentagon")
plt.plot(x, shape_data['Hexagon'], label="Hexagon")
plt.plot(x, shape_data['Heptagon'], label="Heptagon")
plt.title("Number of Cells of each Cell Shape Over Time")
plt.xlabel("Time")
plt.gca().legend(loc="upper left")
plt.savefig('CellShapes.png')

plt.figure(4)
x = neighbour_data['# TimeStamp']
plt.xlabel("Time")
plt.plot(x, neighbour_data['1Neighbour'], label="Cells With 1 Neighbour")
plt.plot(x, neighbour_data['2Neighbours'], label="Cells with 2 Neighbours")
plt.plot(x, neighbour_data['3Neighbours'], label="Cells with 3 Neighbours")
plt.plot(x, neighbour_data['4Neighbours'], label="Cells with 4 Neighbours")
plt.title("Number of Neighbours of Cells Over Time")
plt.gca().legend(loc="upper left")
plt.savefig('NumNeighboursPlot1.png')

plt.figure(5)
x = neighbour_data['# TimeStamp']
plt.xlabel("Time")
plt.plot(x, neighbour_data['5Neighbours'], label="Cells with 5 Neighbours")
plt.plot(x, neighbour_data['6Neighbours'], label="Cells with 6 Neighbours")
plt.plot(x, neighbour_data['7Neighbours'], label="Cells with 7 Neighbours")
plt.title("Number of Neighbours of Cells Over Time")
plt.gca().legend(loc="upper left")
plt.savefig('NumNeighboursPlot2.png')
'''
