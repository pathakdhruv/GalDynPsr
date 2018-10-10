import math
from galpy.potential import MWPotential2014
from galpy.util import bovy_conversion
from astropy import units
from galpy.potential import KeplerPotential
from galpy.potential import vcirc
from GalDynPsr import read_parameters as par

#MWPotential2014.append(KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(Vs,Rskpc)))

def VpratioMWBH(Rpkpc):
    MWPotential2014.append(KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc)))
    a = vcirc(MWPotential2014,Rpkpc/par.Rskpc)
    return a;

def MWBHpl(ldeg, sigl, bdeg, sigb, dkpc, sigd):

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    c = par.c
    Rskpc = par.Rskpc
    kpctom = par.kpctom
    Vs = par.Vs
    Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
    Vprat = VpratioMWBH(Rpkpc)
    Vp = Vprat*Vs
    zkpc = dkpc*math.sin(b)

    Vsms = 1000.0*Vs #m/s
    Rs = Rskpc*kpctom
    be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
    t0 = math.sin(l)*math.sin(l) + be*be

    t2 = (-1.0)*(math.cos(l) + Vprat*Vprat*(be/t0))  #dimensionless         
    t3 = (Vsms*Vsms)/(Rs) #in SI
    adr = t2*t3*math.cos(b)  #m sec^-2 (divide by c to get in s^-1)
    Excpl = adr/c #sec^-1
    return Excpl;
