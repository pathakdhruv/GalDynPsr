import math
from GalDynPsr import read_parameters as par



def Vprat(Rpkpc):
     b0reid14=par.b0reid14     
     Rskpc=par.Rskpc
     Rs = Rskpc*par.kpctom
     Vs= par.Vs
     Vp=Vs+b0reid14*(Rpkpc - Rskpc) # in km s^-1
     Vpratio = Vp/Vs     
     return Vpratio

def aplmod(ldeg, sigl, bdeg, sigb, dkpc, sigd):

     b0reid14=par.b0reid14
     c=par.c

     Rskpc=par.Rskpc
     Rs = Rskpc*par.kpctom
     Vs= par.Vs
     Vsms = 1000.0*Vs 

     l = ldeg*par.degtorad
     b = bdeg*par.degtorad

     
     Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
     be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
     t0 = math.sin(l)*math.sin(l) + be*be

     Vpratio = Vprat(Rpkpc)
     vp_rat_square= Vpratio*Vpratio

     t2 = (-1.0)*(math.cos(l) + vp_rat_square*(be/t0))  #dimensionless         

     t3 = (Vsms*Vsms)/(Rs) #in SI

     adr = t2*t3  #m sec^-2 (divide by c to get in s^-1)
     adrc = adr/c #sec^-1
     return adrc;


def aplold(ldeg, sigl, bdeg, sigb, dkpc, sigd):
  
     b0dt91=par.b0dt91
     c=par.c

     Rskpc=par.Rskpc
     Rs = Rskpc*par.kpctom
     Vs= par.Vs
     Vsms = 1000.0*Vs 

     l = ldeg*par.degtorad
     b = bdeg*par.degtorad

     
     Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
     be = (dkpc/Rskpc)*math.cos(b) - math.cos(l)
     t0 = math.sin(l)*math.sin(l) + be*be
   
     vp=Vs+b0dt91*(Rpkpc - Rskpc) # in km s^-1
   
     vp_rat_square=(vp*vp)/(Vs*Vs)

     t2 = (-1.0)*(math.cos(l) + vp_rat_square*(be/t0))  #dimensionless         

     t3 = (Vsms*Vsms)/(Rs) #in SI

     adr = t2*t3  #m sec^-2 (divide by c to get in s^-1)
     adrc = adr/c #sec^-1
     return adrc;
