import math
from galpy.potential import MWPotential2014
from galpy.potential import PowerSphericalPotentialwCutoff
from galpy.potential import MiyamotoNagaiPotential
from galpy.potential import NFWPotential
from galpy.util import bovy_conversion
from astropy import units
from galpy.potential import KeplerPotential
from galpy.potential import evaluateRforces
from GalDynPsr import read_parameters as par

global MWBH
 


def MWBHRfo(ldeg, sigl, bdeg, sigb, dkpc, sigd):

    b = bdeg*par.degtorad
    l = ldeg*par.degtorad
    Rskpc = par.Rskpc
    Vs = par.Vs
    conversion = par.conversion
    Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
    zkpc = dkpc*math.sin(b)
    be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
    coslam =  be*(Rskpc/Rpkpc)

    '''
    bp= PowerSphericalPotentialwCutoff(alpha=1.8,rc=1.9/8.,normalize=0.05)
    mp= MiyamotoNagaiPotential(a=3./8.,b=0.28/8.,normalize=.6)
    np= NFWPotential(a=16./8.,normalize=.35)
    kp = KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc))
    MWBH = [bp,mp,np,kp]

    rforce1 = evaluateRforces(MWBH, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    rfsun = evaluateRforces(MWBH, Rskpc/Rskpc,0.0/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)
    '''

    #MWPotential2014.append(KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(Vs,Rskpc)))

    #rforce1 = evaluateRforces(MWPotential2014, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    #rfsun = evaluateRforces(MWPotential2014, Rskpc/Rskpc,0.0/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)


    MWPotential2014wBH= [MWPotential2014,KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc))]
    rforce1 = evaluateRforces(MWPotential2014wBH, Rpkpc/Rskpc,zkpc/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    rfsun = evaluateRforces(MWPotential2014wBH, Rskpc/Rskpc,0.0/Rskpc)*bovy_conversion.force_in_kmsMyr(Vs,Rskpc)

    #rf = (rforce1-rfsun)*conversion*math.cos(b) # s-1
    rf0 = rforce1*coslam + rfsun*math.cos(l) 
    rf = rf0*conversion*math.cos(b) # s-1
    return rf;


