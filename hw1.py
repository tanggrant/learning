import numpy as np

file = open('hw1_15_train.dat','r')
x = []
y = []
for line in file.readlines():
    data = [float(i) for i in line.split(" ")]
    xt, yt = data[:-1], data[-1]
    x.append(xt)
    y.append(yt)
print(y)
