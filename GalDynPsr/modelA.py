
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.ExcessZ import g
from GalDynPsr.Excesspl import aplold
from GalDynPsr.err_NT import errNT
from GalDynPsr.err_excesspl_Damour import err_DT91


def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      adrcold = aplold(ldeg, sigl, bdeg, sigb, dkpc, sigd)*math.cos(b) #s^-1
      return adrcold;

def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      b = bdeg*par.degtorad
      zkpc = dkpc*math.sin(b)
      azbcnt = g(zkpc)*math.sin(b) #s^-1
      return azbcnt;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      errDT91 = err_DT91(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errDT91;

def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      errnt = errNT(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errnt;


