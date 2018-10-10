
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.ExcessZ import g
from GalDynPsr.Excesspl import aplmod
from GalDynPsr.err_NT import errNT
from GalDynPsr.err_excesspl_Reid import err_Reid14




def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      b = bdeg*par.degtorad
      l = ldeg*par.degtorad
      adrc = aplmod(ldeg, sigl, bdeg, sigb, dkpc, sigd)*math.cos(b) #s^-1
      return adrc;


def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      b = bdeg*par.degtorad
      zkpc = dkpc*math.sin(b)
      azbcnt = g(zkpc)*math.sin(b) #s^-1
      return azbcnt;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      errReid = err_Reid14(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errReid;


def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      errnt = errNT(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errnt;





