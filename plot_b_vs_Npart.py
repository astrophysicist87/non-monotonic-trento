import matplotlib.pyplot as plt
import numpy as np
import sys

x_axis_column_index = int(sys.argv[2])
y_axis_column_index = int(sys.argv[3])

#====================================================================================
def load_file(file):
    # columns for Npart and integrated S, respectively
    data = np.loadtxt(file, usecols=(x_axis_column_index, y_axis_column_index))
    
    # sort by Npart (or plotting quantity)
    data = data[data[:,0].argsort()]
    
    # find Npart values corresponding to different percentiles
    inds = np.digitize(data[:,0], np.percentile(data[:,0], percentiles)[::-1])
    
    # the indices at which the bins are split
    binlimits = np.where(np.diff(inds))[0]+1
    
    # split the data array accordingly
    bins = np.split(data, binlimits)
    
    print(np.array(bins).shape)
    exit(0)

    return bins



#====================================================================================
def plot_histogram():
    data = np.loadtxt(sys.argv[1], usecols=(int(sys.argv[2]), int(sys.argv[3])))

    fig, ax = plt.subplots(nrows=1, ncols=1)

    bxw, byw = 0.1, 0.1
    nbx = int(np.amax(data[:,0])/bxw)
    nby = int(np.amax(data[:,1])/byw)
    ax.hist2d(data[:,0], data[:,1], bins=[nbx,nby])

    fig.tight_layout()

    plt.show()


#====================================================================================
def plot_curves(bins):
    fig, ax = plt.subplots(nrows=1, ncols=1)

    x = np.array([ np.mean(bin) for bin in bins ])
    ax.hist2d(data[:,0], data[:,1], bins=[nbx,nby])

    fig.tight_layout()

    plt.show()
    
    
    




#====================================================================================
if __name__ == "__main__":
    bins = load_file(sys.argv[1])
    #np.savetxt(collisionSpecies + "_uptick.dat", get_uptick(bins))
    plot_curves(bins)