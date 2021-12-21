from matplotlib import pyplot
import random

x = [0]
y = [0]

for term in range(10**5):
  z = random.uniform(0,1)
  x_len = int(len(x))-1
  y_len = int(len(y))-1
  if 0 <= z <= 0.02:
    new_x = random.uniform(-0.005,0.005)
    new_y = y[y_len]
  if 0.02 < z <= 0.09:
    new_x = 0.05*x[x_len]-0.2*y[y_len]
    new_y = 0.2*x[x_len]+0.05*y[y_len]
  if 0.09 < z <= 0.16:
    new_x = -0.05*x[x_len]+0.2*y[y_len]
    new_y = 0.2*x[x_len]+0.05*y[y_len]
  if 0.16 < z <= 1:
    new_x = 0.93*x[x_len]
    new_y = 0.93*y[y_len]+0.5
  x.append(new_x)
  y.append(new_y)

pyplot.scatter(x,y,color = "r",s = 0.00005)
pyplot.savefig("hi")
pyplot.show()
