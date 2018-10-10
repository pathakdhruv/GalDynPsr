
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.ExcessZ import fhigh
from GalDynPsr.ExcessZ import flow
from GalDynPsr.Excesspl import aplmod
from GalDynPsr.err_HFhigh import errHFhi
from GalDynPsr.err_HFlow import errHFlo
from GalDynPsr.err_excesspl_Reid import err_Reid14



def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      adrc = aplmod(ldeg, sigl, bdeg, sigb, dkpc, sigd)*math.cos(b) #s^-1
      return adrc;

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
      errReid = err_Reid14(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errReid;

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

