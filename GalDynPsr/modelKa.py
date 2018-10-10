
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.galpyMWZfo import MWZfo
from GalDynPsr.galpyMWpl import MWpl



def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   excpl = MWpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1 
   return excpl;

def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   excz = MWZfo(ldeg, sigl, bdeg, sigb, dkpc, sigd)#s^-1 
   return excz;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;

def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;
