import math
import pkg_resources



global pi,degtorad,dtoyr,c,kpctom,yrts,Vs,Rskpc,conversion,Vs,sigVs,Rskpc,sigRs,b0reid14,sigb0r,b0dt91,sigb0dt
pi = math.pi
degtorad= pi/180.0
dtoyr = 1.0/365.25
c = 299792458.0 #m/s
kpctom = 3.0856775814913675e+19
yrts = 365.25*24.0*3600.0
conversion = 1000.0/(c*yrts*pow(10.0,6.0))




DB_FILE = pkg_resources.resource_filename(__name__, 'parameters.in')

inp = open(DB_FILE,'r')
x=[]
for line in inp:
   s=line.split() 
   x.append(s)

Vs = float(x[0][2])
sigVs = float(x[1][2])

Rskpc = float(x[2][2])
sigRs = float(x[3][2]) 


b0reid14 = float(x[4][2])
sigb0r = float(x[5][2])

b0dt91 = float(x[6][2])
sigb0dt = float(x[7][2])



def Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd):
     l = ldeg*degtorad
     b = bdeg*degtorad     
     a = Rskpc*Rskpc + dkpc*math.cos(b)*dkpc*math.cos(b) - 2.0*Rskpc*dkpc*math.cos(b)*math.cos(l)
     asqrt = pow(a,0.5)
     return asqrt;


def z(ldeg, sigl, bdeg, sigb, dkpc, sigd):
    b = bdeg*degtorad
    zkpc = dkpc*math.sin(b)
    return zkpc;

def ErrRp(ldeg, sigl, bdeg, sigb, dkpc, sigd):
    Rs = Rskpc*kpctom
    b = bdeg*degtorad
    l = ldeg*degtorad   
    Rp_kpc = Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)

    beta  = (dkpc*math.cos(b)/Rskpc) - math.cos(l)
    t0 = math.sin(l)*math.sin(l) + beta*beta
    t1 = pow(t0,0.5)


    def betabyd():
        a = math.cos(b)/Rskpc
        return a;

    def betabyb():
        a = -dkpc*math.sin(b)/Rskpc
        return a;

    def betabyl():
        a = math.sin(l)
        return a;

    def betabyRs():
        a = -dkpc*math.cos(b)/(Rskpc*Rskpc)
        return a;

    def Rpbyd():
        a = (Rskpc*beta*betabyd())/pow(t0,0.5)
        return a;

    def Rpbyb():
        a = (Rskpc*beta*betabyb())/pow(t0,0.5)
        return a;

    def Rpbyl():
        a = (Rskpc*(math.sin(l)*math.cos(l) + beta*betabyl()))/pow(t0,0.5)
        return a;

    def RpbyRs():
        a = pow(t0,0.5) + (Rskpc*beta*betabyRs())/pow(t0,0.5)
        return a;

    err_Rpsq = pow(Rpbyb(),2.0)*pow(sigb,2.0) + pow(Rpbyl(),2.0)*pow(sigl,2.0) + pow(Rpbyd(),2.0)*pow(sigd,2.0) + pow(RpbyRs(),2.0)*pow(sigRs,2.0)

    err_Rp = pow(err_Rpsq,0.5)
    return err_Rp;
    


def Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd):
    b = bdeg*degtorad    
    err_zkpcsq = pow(dkpc*math.cos(b),2.0)*pow(sigb,2.0) + pow(math.sin(b),2.0)*pow(sigd,2.0)
    err_zkpc = pow(err_zkpcsq,0.5) 
    return err_zkpc;    



inp.close()




