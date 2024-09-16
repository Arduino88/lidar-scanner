import serial
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

s = serial.Serial('COM7',115200)

matrix = [[None for _ in range(151)] for _ in range(180)]
counter = 0
servo1 = 0
max_servo2 = 0

while servo1 < 130:
    line = s.readline(-1).decode('utf-8')
    #print(f'SERIAL OUTPUT: {line}')

    servo1 = int(line[:line.find(',')])
    line = line[line.find(', ') + 2:]

    servo2 = int(line[:line.find(',')])
    line = line[line.find(', ') + 2:]

    reading = float(line)

    print(f'counter: {counter} | servo1: {servo1}, servo2: {servo2}, reading: {reading}')
    matrix[servo1][servo2] = reading
    counter += 1
    max_servo2 = max(max_servo2, servo2)

print('done')

df = pd.DataFrame(matrix)
df = df.T

df.to_pickle("dataframe.pkl")

cmap = plt.get_cmap('plasma')
new_cmap = LinearSegmentedColormap.from_list("NewCmap", [(0, 0, 1), (1, 0, 0), (10, 0, 0)], N=20)

plt.pcolor(df, cmap=cmap)
plt.axis([0, servo1, max_servo2, 0])
plt.title("Heatmap of DataFrame")
plt.show()

print(df)

#print(matrix)
