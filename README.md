# Structure Factor for 2D particles 

Compute the structure factor of a 2D system of particles. The structure factor is defined as the fourier transform of the spatial correlation function of the system (see https://en.wikipedia.org/wiki/Structure_factor for ref.).  
In order to compute this quantity, first a coarse-grained density matrix `hist` is computed from the position of the particles. Then the Fourier transform is applied on this matrix and the array of the norm of the matrix returned. This array can be shown in a 2d countor plot and gives information about the typical lenght scale of the system.   
The program accept as input a file with two columns with the x and y positions and return the contour plot of the structure factor. Moreover, if the system is a square box, compute the spherical average of the structure factor and the first moment of the distribution.

## Installation and usage

To install the program, it is just needed to clone this repository on your local machine. You need to have python3 installed in the system with numpy and matplotlib package installed. You can run the program then as   
`python3 strfactor.py dataset.dat`   
where dataset is a file with the xy positions of the particles in the format   
```
x1 y1  
x2 y2
x3 y3
... 
```   
A test dataset is given in the file `xy.dat`, so the command `python3 strfactor.py xy.dat` should give an example of the expected output.   

