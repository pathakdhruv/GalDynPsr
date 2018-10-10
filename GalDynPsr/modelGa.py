
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.ExcessZ import g
from GalDynPsr.err_NT import errNT
from GalDynPsr.galpyMWpl import MWpl


def Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   excpl = MWpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
   return excpl;

def Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   b = bdeg*par.degtorad
   zkpc = dkpc*math.sin(b)
   exz = g(zkpc)*math.sin(b) #s^-1
   return exz;

def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
      errnt = errNT(ldeg, sigl, bdeg, sigb, dkpc, sigd) #s^-1
      return errnt;


def Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):
   print ("Error calculation can not be done as this model uses galpy")
   return 0.0;
