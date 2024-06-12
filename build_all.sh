#! /bin/bash

rm -rf build                                          \
  && mkdir -p build                                   \
  && cd build &&                                      \
  HDF5_ROOT=                                          \
    cmake -DCMAKE_PREFIX_PATH=~/hdf5-1.10.5/src .. && \
  make install &&                                     \
  cd ..
