
import math
import numpy as np
from GalDynPsr import read_parameters as par
from GalDynPsr.err_Shklovskii import err_Shkl


def Exshk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud):
  c= par.c
  mu_T = pow((mu_alpha*mu_alpha + mu_delta*mu_delta),0.5) # mas/yr
  Pshk = (dkpc*(mu_T*mu_T))/c #kpc*(mass yr-1)/(m/s)
  Pshks = (2.42924681374e-21)*dkpc*(mu_T*mu_T) #s^-1
  return Pshks;

def errShk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud):
  errshkl = err_Shkl(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)
  return errshkl;
