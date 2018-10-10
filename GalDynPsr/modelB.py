
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.ExcessZ import fhigh
from GalDynPsr.ExcessZ import flow
from GalDynPsr.Excesspl import aplold
from GalDynPsr.err_HFhigh import errHFhi
from GalDynPsr.err_HFlow import errHFlo
from GalDynPsr.err_excesspl_Damour import err_DT91


def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   b = bdeg*par.degtorad
   l = ldeg*par.degtorad
   adrcold = aplold(ldeg, sigl, bdeg, sigb, dkpc, sigd)*math.cos(b) #s^-1
   return adrcold;

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

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   errDT91 = err_DT91(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
   return errDT91;

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

