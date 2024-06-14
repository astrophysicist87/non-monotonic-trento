import numpy as np
import sys

bw          = int(sys.argv[1]) # in %
percentiles = np.linspace(0,100,1+100//bw)[1:-1]

#====================================================================================
def get_uptick(files):
    # columns for Npart and integrated S, respectively
    data = np.vstack([np.loadtxt(file, usecols=(2,3)) for file in files])
    
    # sort by Npart
    data = data[data[:,0].argsort()]
    
    # find indices corresponding to different percentiles
    inds = np.digitize(data[:,0], np.percentile(data[:,0], percentiles)[::-1])
    
    # the Npart values at which the bins are split
    binlimits = np.where(np.diff(inds))[0]+1
    print('Bin limits:', binlimits)
    
    # split the data array accordingly
    bins = np.split(data, binlimits)

    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), 2.0*np.mean(bin[:,1])/np.mean(bin[:,0])] for bin in bins])

#====================================================================================
def get_eps2rms(files):
    # columns for Npart and integrated S, respectively
    data = np.vstack([np.loadtxt(file, usecols=(2,4)) for file in files])
    
    # sort by Npart
    data = data[data[:,0].argsort()]
    
    # find Npart values corresponding to different percentiles
    inds = np.digitize(data[:,0], np.percentile(data[:,0], percentiles)[::-1])
    
    # the Npart values at which the bins are split
    binlimits = np.where(np.diff(inds))[0]+1
    print('Bin limits:', binlimits)
    
    # split the data array accordingly
    bins = np.split(data, binlimits)
    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), np.sqrt(np.mean(bin[:,1]**2))] for bin in bins])


#====================================================================================
if __name__ == "__main__":
    collisionSpecies = sys.argv[2]
    files = sys.argv[3:]
    np.savetxt(collisionSpecies + "_uptick.dat", get_uptick(files))
    np.savetxt(collisionSpecies + "_eps2rms.dat", get_eps2rms(files))