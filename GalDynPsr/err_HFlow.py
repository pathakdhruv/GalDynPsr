#Partial derivative
import math
import numpy as np
from GalDynPsr import read_parameters as par
global bdeg, sigb, dkpc, sigd, alpha1, alpha2, alpha3, alpha4, alpha5, k, b, zkpc, D1, D2, A1, A2, A3


def errHFlo(ldeg, sigl, bdeg, sigb, dkpc, sigd):

    alpha1 = 0.471183
    alpha2 = 1.56477
    alpha3 = 0.409007 
    alpha4 = 0.00937683
    alpha5 = 0.178331

    k = -1.08100761142e-19

    b = bdeg*par.degtorad
    zkpc = dkpc*math.sin(b)
    D1 = zkpc*zkpc + alpha3
    D2 = zkpc*zkpc + alpha5
    A1 = alpha1
    A2 = alpha2/pow(D1,0.5)
    A3 = alpha4/pow(D2,1.5)

    def diffbyb():
        a1 = k*dkpc*math.sin(2.0*b)*(A1+A2+A3) 
        a2 = -k*(zkpc*zkpc)*dkpc*math.sin(2.0*b)*(alpha2/pow(D1,1.5) + 3.0*alpha4/pow(D2,2.5))/2.0
        a = a1+a2
        return a;

    def diffbyd():
        a1 = k*pow(math.sin(b),2.0)*(A1+A2+A3)
        a2 = -k*(zkpc*zkpc)*pow(math.sin(b),2.0)*(alpha2/pow(D1,1.5) + 3.0*alpha4/pow(D2,2.5))
        a = a1+a2 
        return a;


    err_HFlosq = pow(diffbyb(),2.0)*pow(sigb,2.0) + pow(diffbyd(),2.0)*pow(sigd,2.0)
    err_HFlo = pow(err_HFlosq,0.5) 
    return err_HFlo;



