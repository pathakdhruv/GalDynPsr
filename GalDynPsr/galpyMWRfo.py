import math
from galpy.potential import MWPotential2014
from galpy.util import bovy_conversion
from astropy import units
from galpy.potential import evaluateRforces
from GalDynPsr import read_parameters as par




def MWRfo(ldeg, sigl, bdeg, sigb, dkpc, sigd):


    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
    zkpc = dkpc*math.sin(b)
    be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
    coslam =  be*(Rskpc/Rpkpc)

    rforce1 = evaluateRforces(MWPotential2014, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    rfsun = evaluateRforces(MWPotential2014, Rskpc/Rskpc,0.0/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)
    
    rf0 = rforce1*coslam + rfsun*math.cos(l) 
    rf = rf0*conversion*math.cos(b) # s-1
    
    return rf;




