import numpy as np
import sys

float_t = '<f8'; int_t = '<i8'; complex_t = '<c16'
species = [('pion', 211), ('kaon', 321), ('proton', 2212), ('Lambda', 3122), ('Sigma0', 3212), ('Xi', 3312), ('Omega', 3334),]

dNchdeta_column_index = 0

====================================================================================
def load_files(file, nbins):
    events = np.fromfile(sys.argv[1], dtype=[\
                    ('initial_entropy', float_t),\
                    ('nsamples', int_t),\
                    ('dNch_deta', float_t),\
                    ('dET_deta', float_t),\
                    ('dN_dy', [(s, float_t) for (s, _) in species]),\
                    ('mean_pT', [(s, float_t) for (s, _) in species]),\
                    ('pT_fluct', [('N', int_t), ('sum_pT', float_t), ('sum_pTsq', float_t)]),\
                    ('flow', [('N', int_t), ('Qn', complex_t, 8)]),\
                ])
    
    vn = np.abs( events['flow']['Qn'].T / (events['flow']['N']+1e-100) )

    data = np.c_[ events['dNch_deta'], vn.T ]
    data = data[data[:,dNchdeta_column_index].argsort()]

    return np.array_split(data, nbins)


#====================================================================================
def v_n_2(vn):
    # evaluate and return the required observable in each bin as an array
    return np.sqrt(np.mean(vn**2))

#====================================================================================
def v_n_4(vn):
    # evaluate and return the required observable in each bin as an array
    return 2.0*np.mean(vn**2)**2 - np.mean(vn**4)

#====================================================================================
def v_n_6(vn):
    # evaluate and return the required observable in each bin as an array
    return 0.25*(np.mean(vn**6) - 9.0*np.mean(vn**2)*np.mean(vn**4) + 12.0*np.mean(vn**2)**3)

#====================================================================================
def v_n_8(vn):
    # evaluate and return the required observable in each bin as an array
    return ( 144.0*np.mean(vn**2)**4 - 144.0*np.mean(vn**2)**2*np.mean(vn**4) \
             + 18.0*np.mean(vn**4)**2 + 16.0*np.mean(vn**2)*np.mean(vn**6) - np.mean(vn**8) ) / 33.0

#====================================================================================
def get_v_n_2(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,dNchdeta_column_index]), v_n_2(bin[:,1:])] for bin in bins])

#====================================================================================
def get_v_n_4(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,dNchdeta_column_index]), v_n_4(bin[:,1:])] for bin in bins])

#====================================================================================
def get_v_n_6(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,dNchdeta_column_index]), v_n_6(bin[:,1:])] for bin in bins])

#====================================================================================
def get_v_n_8(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([[np.mean(bin[:,dNchdeta_column_index]), v_n_8(bin[:,1:])] for bin in bins])


#====================================================================================
if __name__ == "__main__":
    file = sys.argv[1]
    nbins = int(sys.argv[2])
    bins = load_files(file, nbins)
    print(bins.shape)
    #np.savetxt(collisionSpecies + "_v_n_2.dat", get_v_n_2(bins))
    #np.savetxt(collisionSpecies + "_v_n_4.dat", get_v_n_4(bins))
    #np.savetxt(collisionSpecies + "_v_n_6.dat", get_v_n_6(bins))
    #np.savetxt(collisionSpecies + "_v_n_8.dat", get_v_n_8(bins))










