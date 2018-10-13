import math
from galpy.potential import MWPotential2014
from galpy.potential import PowerSphericalPotentialwCutoff
from galpy.potential import MiyamotoNagaiPotential
from galpy.potential import NFWPotential
from galpy.util import bovy_conversion
from astropy import units
from galpy.potential import KeplerPotential
from galpy.potential import vcirc
from GalDynPsr import read_parameters as par



global MWBH
 


def VpratioMWBH(Rpkpc):
    #MWPotential2014.append(KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc)))
    #a = vcirc(MWPotential2014,Rpkpc/par.Rskpc)
    '''
    bp= PowerSphericalPotentialwCutoff(alpha=1.8,rc=1.9/8.,normalize=0.05)
    mp= MiyamotoNagaiPotential(a=3./8.,b=0.28/8.,normalize=.6)
    np= NFWPotential(a=16./8.,normalize=.35)
    kp = KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc))
    MWBH = [bp,mp,np,kp]
    a = vcirc(MWBH,Rpkpc/par.Rskpc)
    '''
    MWPotential2014wBH= [MWPotential2014,KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(par.Vs,par.Rskpc))]
    a = vcirc(MWPotential2014wBH,Rpkpc/par.Rskpc)
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



