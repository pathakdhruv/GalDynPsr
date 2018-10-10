
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.galpyMWBHZfo import MWBHZfo
from GalDynPsr.galpyMWBHpl import MWBHpl



def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   excpl = MWBHpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1 
   return excpl;

def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   exz = MWBHZfo(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1 
   return exz;

def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;

def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;
