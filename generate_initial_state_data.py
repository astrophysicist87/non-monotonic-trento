import numpy as np
import sys

#====================================================================================
def get_uptick(files):
    # columns for Npart and integrated S, respectively
    data = np.vstack([np.loadtxt(file, usecols=(2,3)) for file in files])
    
    # sort by Npart
    data = data[data[:,0].argsort()]
    
    # find Npart values corresponding to different percentiles
    inds = np.digitize(data[:,0], np.percentile(data[:,0], np.linspace(10,90,9))[::-1])
    
    # split the data array accordingly
    bins=np.split(data, np.where(np.diff(inds))[0]+1)

    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), 2.0*np.mean(bin[:,1])/np.mean(bin[:,0])] for bin in bins])

#====================================================================================
def get_eps2rms(files):
    # columns for Npart and integrated S, respectively
    data = np.vstack([np.loadtxt(file, usecols=(2,4)) for file in files])
    
    # sort by Npart
    data = data[data[:,0].argsort()]
    
    # find Npart values corresponding to different percentiles
    inds = np.digitize(data[:,0], np.percentile(data[:,0], np.linspace(10,90,9))[::-1])
    
    # split the data array accordingly
    bins=np.split(data, np.where(np.diff(inds))[0]+1)
    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), np.sqrt(np.mean(bin[:,1]**2))] for bin in bins])


#====================================================================================
if __name__ == "__main__":
    files = sys.argv[1:]
    #print(get_uptick(files))
    print(get_eps2rms(files))