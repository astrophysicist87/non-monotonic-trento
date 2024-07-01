import matplotlib.pyplot as plt
import numpy as np
import sys

columns_to_plot = sys.argv[2:]
data = np.loadtxt(sys.argv[1], usecols=columns_to_plot)

fig, ax = plt.subplots(nrows=1, ncols=1)

bxw, byw = 0.1, 1.0
nbx = int(np.amax(data[:,0])/bxw)
nby = int(np.amax(data[:,1])/byw)
ax.hist2d(data[:,0], data[:,1], bins=[nbx,nby])

fig.tight_layout()

plt.show()