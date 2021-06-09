#!/usr/bin/env python3

from math import pi
from typing import Type
from sf_utils import spherical_average, first_moment     # file sf_utils.py needs to be in the same folder

import numpy as np
import matplotlib.pyplot as plt
import sys

"""
Computation of the structure factor
accepts as input a file with the particles' positions arranged as rows x0 y0
the other parameters are the dimesnion of the box and the dimension of the coarse grain 

Input: filename sim_box_size_x sim_box_size_y grid_size

Claudio B. Caporusso 
Physics PhD Student - XXXVI ciclo
Bari University
"""

try:
    filename = sys.argv[1]
    isinstance(filename,str)
except:
    print("Error: first input not a string")
    print("Exiting...")
    sys.exit(1)

try:
    Lx = float(sys.argv[2])
    Ly = float(sys.argv[3])
    grid = float(sys.argv[4])
    #if not (isinstance(Lx,float) or isinstance(Ly,float) or isinstance(grid,float)):
except:
    print("Error: some input is not a float")
    print("Exiting...")
    sys.exit(1)

try:
    data = np.loadtxt(filename)
except:
    print("Impossible to read data, check if file exist")
    print("Exiting...")
    sys.exit(1)

#   definition of some quantities  

Nbeads = len(data)
L=np.array((Lx,Ly))
div = np.ceil(L/grid).astype(int)
ind=np.floor(data/grid).astype(int)
kmax = 2*pi/grid

#   histogramming density matrix
dens = np.zeros(div)
for i in range(Nbeads):
    dens[ind[i,0],ind[i,1]] += 1

dens = dens/4/grid/grid*pi  #   here we use the density formula for particles with diameter 1sigma
dens = np.where(dens<.7,-1,1)   # 0.7 is a cutoff density to distinguish between dense phase (particle aggregates) and dilute phase 
plt.imshow(dens)
plt.show()
dens = dens - np.average(dens)

Sij = np.fft.fft2(dens)
Sij = np.fft.fftshift(Sij)
Sij = (np.real(Sij)**2 + np.imag(Sij)**2)/Nbeads    # structure factor formula S = < rho_-k rho_k > / N

kx = np.linspace(-kmax/2.,kmax/2.,div[0])
ky = np.linspace(-kmax/2.,kmax/2.,div[1])
KX,KY = np.meshgrid(kx,ky)

#plt.pcolormesh(KX,KY,np.log(Sij))
plt.pcolormesh(KX,KY,Sij)
plt.show()

try:
    if (L[0]!=L[1]): #the spherical average must be done on a square lattice of frequencies
        raise Exception("Error: Not a sqared box. Spherical average must be computed only on a perfectly squared box.")
except Exception as e:
    print(e)
    sys.exit(1)

#   this part is executed only if the system is perfectly squared

dk = 2*pi/L[0]
kdist,Sk = spherical_average(Sij,kx,dk)
plt.plot(kdist,Sk)
plt.show()

Sk_avg = first_moment(kdist,Sk,dk)
print("First moment of the structure factor is: ", Sk_avg)