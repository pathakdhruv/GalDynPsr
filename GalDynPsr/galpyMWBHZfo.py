import math
from galpy.potential import MWPotential2014
from galpy.util import bovy_conversion
from galpy.potential import evaluatezforces
from astropy import units
from galpy.potential import KeplerPotential
from GalDynPsr import read_parameters as par



def MWBHZfo(ldeg, sigl, bdeg, sigb, dkpc, sigd):

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
    zkpc = dkpc*math.sin(b)

    MWPotential2014.append(KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(Vs,Rskpc)))
    zf1 = evaluatezforces(MWPotential2014, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)
    Excz = zf1*conversion*math.sin(b)#s-1

    return Excz;
