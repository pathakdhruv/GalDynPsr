
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.Excesspl import aplold
from GalDynPsr.err_excesspl_Damour import err_DT91
from GalDynPsr.galpyMWBHZfo import MWBHZfo


def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   b = bdeg*par.degtorad
   l = ldeg*par.degtorad
   excpl = aplold(ldeg, sigl, bdeg, sigb, dkpc, sigd)*math.cos(b) #s^-1
   return excpl;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   errDT91 = err_DT91(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
   return errDT91;


def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   exz = MWBHZfo(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
   return exz;

def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;
