import numpy as np
import sys

bw          = int(sys.argv[1]) # in %
percentiles = np.linspace(0,100,1+100//bw)[1:-1]

#====================================================================================
def load_files(files):
    # columns for Npart and integrated S, respectively
    data = np.vstack([np.loadtxt(file, usecols=(2,3)) for file in files])
    
    # sort by Npart
    data = data[data[:,0].argsort()]
    
    # find Npart values corresponding to different percentiles
    inds = np.digitize(data[:,0], np.percentile(data[:,0], percentiles)[::-1])
    print('Npart bin limits:', inds)
    
    # the indices at which the bins are split
    binlimits = np.where(np.diff(inds))[0]+1
    
    # split the data array accordingly
    bins = np.split(data, binlimits)

    return bins

#====================================================================================
def e_2_2(e2):
    # evaluate and return the required observable in each bin as an array
    return np.sqrt(np.mean(e2**2))

#====================================================================================
def e_2_4(e2):
    # evaluate and return the required observable in each bin as an array
    return 2.0*np.mean(e2**2)**2 - np.mean(e2**4)

#====================================================================================
def e_2_6(e2):
    # evaluate and return the required observable in each bin as an array
    return 0.25*(np.mean(e2**6) - 9.0*np.mean(e2**2)*np.mean(e2**4) + 12.0*np.mean(e2**2)**3)

#====================================================================================
def e_2_8(e2):
    # evaluate and return the required observable in each bin as an array
    return ( 144.0*np.mean(e2**2)**4 - 144.0*np.mean(e2**2)**2*np.mean(e2**4) \
             + 18.0*np.mean(e2**4)**2 + 16.0*np.mean(e2**2)*np.mean(e2**6) - np.mean(e2**8) ) / 33.0

#====================================================================================
def get_uptick(bins):
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), 2.0*np.mean(bin[:,1])/np.mean(bin[:,0])] for bin in bins])

#====================================================================================
def get_e_2_2(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), e_2_2(bin[:,1])] for bin in bins])

#====================================================================================
def get_e_2_4(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), e_2_4(bin[:,1])] for bin in bins])

#====================================================================================
def get_e_2_6(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), e_2_6(bin[:,1])] for bin in bins])

#====================================================================================
def get_e_2_8(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,0]), e_2_8(bin[:,1])] for bin in bins])


#====================================================================================
if __name__ == "__main__":
    collisionSpecies = sys.argv[2]
    files = sys.argv[3:]
    bins = load_files(files)
    np.savetxt(collisionSpecies + "_uptick.dat", get_uptick(bins))
    np.savetxt(collisionSpecies + "_e_2_2.dat", get_e_2_2(bins))
    np.savetxt(collisionSpecies + "_e_2_4.dat", get_e_2_4(bins))
    np.savetxt(collisionSpecies + "_e_2_6.dat", get_e_2_6(bins))
    np.savetxt(collisionSpecies + "_e_2_8.dat", get_e_2_8(bins))
