from math import pi
import numpy as np

def spherical_average(Sij,kk,dk):

	"""
	Compute the spherical average of the structure factor S(kx,ky).
	The structure factor is passed as a discrete matrix Sij as first argument.
	The second and third argoment should be the simulation box dimensions.
	Return an one dimensional array Sk.
	"""

	kmax = np.max(kk)
	knum = len(kk)

	Sk = np.zeros(knum)	# array for the spherical average
	count = np.zeros(knum)
	rad = np.zeros((knum,knum))

	for i in range(knum):
		for j in range(knum):
			rad[i,j] = np.sqrt(kk[i]*kk[i]+kk[j]*kk[j])
			if rad[i,j] < kmax:
				k = np.floor(rad[i,j]/dk).astype(int)
				Sk[k] += Sij[i,j]
				count[k] += 1
	
	Sk = Sk[1:] # the point at the origin is pathologic
	count = count[1:]

	Sk = np.divide(Sk,count, out=np.zeros_like(Sk), where=count!=0)
	kdist = np.linspace(dk,kmax,knum-1)
	
	return kdist,Sk

def first_moment(k,Sk,dk):
	
	"""
	Compute the first moment of the structure factor Sk 
	over the domain k and with an infinitesimal step dk. 
	"""

	I = np.sum(dk*np.abs(dk*k)*Sk)/np.sum(dk*Sk)
	return pi*I
	