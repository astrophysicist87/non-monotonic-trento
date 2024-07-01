import matplotlib.pyplot as plt
import numpy as np
import sys

data = np.loadtxt(sys.argv[1], usecols=(int(sys.argv[2]), int(sys.argv[3])))

fig, ax = plt.subplots(nrows=1, ncols=1)

bxw, byw = 0.1, 1.0
nbx = int(np.amax(data[:,0])/bxw)
nby = int(np.amax(data[:,1])/byw)
ax.hist2d(data[:,0], data[:,1], bins=[nbx,nby])

fig.tight_layout()

plt.show()