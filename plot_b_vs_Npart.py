import matplotlib.pyplot as plt
import numpy as np
import sys

data = np.loadtxt(sys.argv[1], usecols=(0,1))

fig, ax = plt.subplots(nrows=1, ncols=1)

ax.hist2d(data[:,0], data[:,1], bins=100)

fig.tight_layout()

plt.show()