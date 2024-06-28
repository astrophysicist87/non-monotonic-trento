import numpy as np
import sys

float_t = '<f8'; int_t = '<i8'; complex_t = '<c16'
species = [('pion', 211), ('kaon', 321), ('proton', 2212), ('Lambda', 3122), ('Sigma0', 3212), ('Xi', 3312), ('Omega', 3334),]

dNchdeta_column_index = 0

#====================================================================================
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
    mean_pT = np.abs( events['pT_fluct']['sum_pT'].T / (events['pT_fluct']['N']+1e-100) )

    #print(np.expand_dims(events['dNch_deta'],-1).shape)
    #print(vn.T.shape)
    #print(np.expand_dims(mean_pT,-1).shape)
    #data = np.c_[ np.expand_dims(events['dNch_deta'],-1), vn.T, np.expand_dims(mean_pT,-1) ]
    data = np.c_[ np.expand_dims(events['dNch_deta'],-1), vn.T ]
    #data = np.hstack((np.expand_dims(events['dNch_deta'],-1), vn.T, np.expand_dims(events['mean_pT'],-1)))
    #print(data.shape)
    #try:
    #    print("hstack: ", np.hstack((np.expand_dims(events['dNch_deta'],-1), vn.T)).shape)
    #except:
    #    print("hstack failed.")
    #try:
    #    print("vstack: ", np.vstack((np.expand_dims(events['dNch_deta'],-1), vn.T)).shape)
    #except:
    #    print("vstack failed.")
    #try:
    #    print("dstack: ", np.dstack((np.expand_dims(events['dNch_deta'],-1), vn.T)).shape)
    #except:
    #    print("dstack failed.")
    #exit(0)
    data = data[data[:,dNchdeta_column_index].argsort()]

    return np.array_split(data, nbins)

#====================================================================================
def avg(x):
    # compute mean over axis = 0
    return np.mean(x, axis=0)

#====================================================================================
def v_n_2(vn):
    # evaluate and return the required observable in each bin as an array
    return np.sqrt(avg(vn**2))

#====================================================================================
def v_n_4(vn):
    # evaluate and return the required observable in each bin as an array
    return 2.0*avg(vn**2)**2 - avg(vn**4)

#====================================================================================
def v_n_6(vn):
    # evaluate and return the required observable in each bin as an array
    return 0.25*(avg(vn**6) - 9.0*avg(vn**2)*avg(vn**4) + 12.0*avg(vn**2)**3)

#====================================================================================
def v_n_8(vn):
    # evaluate and return the required observable in each bin as an array
    return ( 144.0*avg(vn**2)**4 - 144.0*avg(vn**2)**2*avg(vn**4) \
             + 18.0*avg(vn**4)**2 + 16.0*avg(vn**2)*avg(vn**6) - avg(vn**8) ) / 33.0

#====================================================================================
def get_v_n_2(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([np.hstack((np.mean(bin[:,dNchdeta_column_index]), v_n_2(bin[:,1:]))) for bin in bins])

#====================================================================================
def get_v_n_4(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([np.hstack((np.mean(bin[:,dNchdeta_column_index]), v_n_4(bin[:,1:]))) for bin in bins])

#====================================================================================
def get_v_n_6(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([np.hstack((np.mean(bin[:,dNchdeta_column_index]), v_n_6(bin[:,1:]))) for bin in bins])

#====================================================================================
def get_v_n_8(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([np.hstack((np.mean(bin[:,dNchdeta_column_index]), v_n_8(bin[:,1:]))) for bin in bins])

#====================================================================================
def get_rho(bins):    
    # evaluate and return the required observable in each bin as an array
    return np.array([np.hstack((np.mean(bin[:,dNchdeta_column_index]), rho(bin[:,1:]))) for bin in bins])


#====================================================================================
if __name__ == "__main__":
    file = sys.argv[1]
    collisionSpecies = sys.argv[2]
    nbins = int(sys.argv[3])
    bins = load_files(file, nbins)
    #for i, bin in enumerate(bins):
    #    print(i, ':', bin.shape)
    np.savetxt(collisionSpecies + "_v_n_2.dat", get_v_n_2(bins))
    np.savetxt(collisionSpecies + "_v_n_4.dat", get_v_n_4(bins))
    np.savetxt(collisionSpecies + "_v_n_6.dat", get_v_n_6(bins))
    np.savetxt(collisionSpecies + "_v_n_8.dat", get_v_n_8(bins))










