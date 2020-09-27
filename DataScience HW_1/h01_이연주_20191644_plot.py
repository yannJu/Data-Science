import sys
import matplotlib.pyplot as plt
import numpy as np

def calCS(n_F, n_E, k_F, k_E):
	s =  -((n_E - n_F) / (k_E - k_F))
	c = np.exp(n_F + (s * k_F))

	return s, c

x_line = list()
y_line = list()
cnt = 1
for line in sys.stdin:
	lst = line.split("\t")
	x_line.append(float(cnt))
	y_line.append(float(lst[1]))
	cnt += 1

S, C = calCS(np.log(y_line[0]), np.log(y_line[-1]), np.log(x_line[0]), np.log(x_line[-1]))
print("C : ", C, " S : " , S)

plt.figure(1)
plt.plot(x_line, y_line)
plt.savefig("HW3_plotsave")
plt.show()
