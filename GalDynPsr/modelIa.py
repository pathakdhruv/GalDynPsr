
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.ExcessZ import fhigh
from GalDynPsr.ExcessZ import flow
from GalDynPsr.err_HFhigh import errHFhi
from GalDynPsr.err_HFlow import errHFlo
from GalDynPsr.galpyMWpl import MWpl



def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   excpl = MWpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1 
   return excpl;


def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
    b = bdeg*par.degtorad
    zkpc = dkpc*math.sin(b)
    if zkpc<0.0:
      zkpcm = -zkpc
    else:
      zkpcm = zkpc
    azbchfh = fhigh(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
    azbchfl = flow(zkpc)*math.sin(b)*1.08100761142e-19 #s^-1
    if zkpcm<=1.5:
       exz = azbchfl
    else:
       exz = azbchfh
    return exz;


def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
    b = bdeg*par.degtorad
    zkpc = dkpc*math.sin(b)
    if zkpc<0.0:
       zkpcm = -zkpc
    else:
       zkpcm = zkpc
    errhi = errHFhi(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
    errlo = errHFlo(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
    if zkpcm<=1.5:
       errz = errlo
    else:
       errz = errhi
    return errz;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;

