import matplotlib.pyplot as plt
import numpy as np
import sys

x_axis_column_index = int(sys.argv[-2])
y_axis_column_index = int(sys.argv[-1])

bw          = 1 # in %
percentiles = np.linspace(0,100,1+100//bw)[1:-1]


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
    
    #print(np.array(bins).shape)
    #exit(0)

    return bins

#====================================================================================
def plot_curves(fig, ax, bins, plotstyle):
    x = np.array([ np.mean(bin[:,0]) for bin in bins ])
    y = np.array([ np.mean(bin[:,1]) for bin in bins ])
    ax.plot(x, y, plotstyle)


#====================================================================================
if __name__ == "__main__":
    # initialize figure
    fig, ax = plt.subplots(nrows=1, ncols=1)
    plotstyles = ['-r', '--b', ':g']
    
    # load and process files, one at a time
    for i, file in enumerate(sys.argv[1:-2]): # all but last two command-line args
        print("Processing file:", file)
        bins = load_file(file)
        plot_curves(fig, ax, bins, plotstyles[i])
        
    fig.tight_layout()

    plt.show()


