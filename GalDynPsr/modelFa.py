
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.Excesspl import aplmod
from GalDynPsr.err_excesspl_Reid import err_Reid14
from GalDynPsr.galpyMWZfo import MWZfo



def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   b = bdeg*par.degtorad
   l = ldeg*par.degtorad
   excpl = aplmod(ldeg, sigl, bdeg, sigb, dkpc, sigd)*math.cos(b) #s^-1
   return excpl;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      errReid = err_Reid14(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errReid;


def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   exz = MWZfo(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
   return exz;


def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;
