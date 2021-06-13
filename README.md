# Structure Factor for 2D particles 

Compute the structure factor of a 2D system of particles. 
The program accept as input a file with two columns with the x and y positions and return the contour plot of the structure factor.
Moreover, if the system is a square box, compute the spherical average of the structure factor

## Installation and usage

To install the program, you just need to clone this repository on your local PC. You need to have python3 installed in the system with numpy and matplotlib package installed.  
You can run the program then as
`python3 strfactor.py dataset.dat`
where dataset is a file with the xy positions of the particles in the format
`x1 y1
 x2 y2
 ...  `

