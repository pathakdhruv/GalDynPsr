#Error for Excess_pl
import math
import numpy as np
from GalDynPsr import read_parameters as par



global b0reid14,c,Rskpc,Rpkpc,Vp,Vs,vp_rat_square,beta,t0,t1,t2,dkpc,b,l

def err_Reid14(ldeg, sigl, bdeg, sigb, dkpc, sigd):


    sigVs = par.sigVs*1000.0#SI
    sigRs = par.sigRs*par.kpctom  #SI  
    sigb0r = par.sigb0r*1000.0/par.kpctom #SI    

    b0reid14=par.b0reid14*1000.0/par.kpctom #SI
    c=par.c
    Rskpc=par.Rskpc
    Rs = Rskpc*par.kpctom #SI
    Vs= par.Vs
    Vsms = 1000.0*Vs #SI
    b = bdeg*par.degtorad
    l = ldeg*par.degtorad   
    Rpkpc = par.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)
    Vp=Vs+par.b0reid14*(Rpkpc - Rskpc) # in km s^-1
    Vpms = 1000.0*Vp #SI
    Rp = Rpkpc*par.kpctom #SI
    d = dkpc*par.kpctom #SI
    beta  = (dkpc*math.cos(b)/Rskpc) - math.cos(l)
    t0 = math.sin(l)*math.sin(l) + beta*beta
    


    def betabyd():
        a = math.cos(b)/Rs
        return a;

    def betabyb():
        a = -d*math.sin(b)/Rs
        return a;

    def betabyl():
        a = math.sin(l)
        return a;

    def betabyRs():
        a = -d*math.cos(b)/(Rs*Rs)
        return a;



    def Rpbyd():
        a = (Rs*beta*betabyd())/pow(t0,0.5)
        return a;

    def Rpbyb():
        a = (Rs*beta*betabyb())/pow(t0,0.5)
        return a;

    def Rpbyl():
        a = (Rs*(math.sin(l)*math.cos(l) + beta*betabyl()))/pow(t0,0.5)
        return a;

    def RpbyRs():
        a = pow(t0,0.5) + (Rs*beta*betabyRs())/pow(t0,0.5)
        return a;


    def Vpbyd():
        a = b0reid14*Rpbyd()
        return a;

    def Vpbyb():
        a = b0reid14*Rpbyb()
        return a;

    def Vpbyl():
        a = b0reid14*Rpbyl()
        return a;

    def VpbyRs():
        a = b0reid14*(RpbyRs() - 1.0)
        return a;

    def VpbyVs():
        a = 1.0
        return a;

    def Vpbyb0reid():
        a = Rp-Rs
        return a;



    def diffbyb():
        term1 = math.cos(l)*math.sin(b)*Vsms*Vsms/(c*Rs)
        term2 = math.sin(b)*beta*Vpms*Vpms/(c*Rs*t0)
        term3 = -math.cos(b)*Vpms*Vpms*betabyb()/(c*Rs*t0)
        term4 =  2.0*math.cos(b)*beta*beta*Vpms*Vpms*betabyb()/(c*Rs*t0*t0)
        term5 = -2.0*math.cos(b)*beta*Vpms*Vpbyb()/(c*Rs*t0)
        a = term1+term2+term3+term4+term5
        return a;

    def diffbyl():
        term1 = math.sin(l)*math.cos(b)*Vsms*Vsms/(c*Rs)
        term2 = -math.cos(b)*Vpms*Vpms*betabyl()/(c*Rs*t0)
        term3 = -2.0*math.cos(b)*beta*Vpms*Vpbyl()/(c*Rs*t0)
        t4a = math.sin(l)*math.cos(l)
        t4b = beta*betabyl()
        term4 = 2.0*math.cos(b)*beta*Vpms*Vpms*(t4a + t4b)/(c*Rs*t0*t0)
        a = term1 +term2 + term3 + term4
        return a;

    def diffbyd():
        term1 = -math.cos(b)*Vpms*Vpms*betabyd()/(c*Rs*t0)
        term2 = -2.0*math.cos(b)*beta*Vpms*Vpbyd()/(c*Rs*t0)
        term3 = 2.0*math.cos(b)*beta*beta*Vpms*Vpms*betabyd()/(c*Rs*t0*t0)
        a = term1 + term2 + term3
        return a;

    def diffbyRs():
        term1 = math.cos(l)*math.cos(b)*Vsms*Vsms/(c*Rs*Rs)
        term2 = math.cos(b)*beta*Vpms*Vpms/(c*Rs*Rs*t0)
        term3 = -math.cos(b)*Vpms*Vpms*betabyRs()/(c*Rs*t0)
        term4 = 2.0*math.cos(b)*beta*beta*Vpms*Vpms*betabyRs()/(c*Rs*t0*t0)
        term5 = -2.0*math.cos(b)*beta*Vpms*VpbyRs()/(c*Rs*t0)
        a = term1 + term2 + term3 + term4 + term5
        return a;

    def diffbyVs():
        term1 = -2.0*math.cos(b)*math.cos(l)*Vsms/(c*Rs)
        term2 = -2.0*math.cos(b)*beta*Vpms*VpbyVs()/(c*Rs*t0)
        a = term1+term2
        return a;

    def diffbyb0reid():
        a = -2.0*math.cos(b)*beta*Vpms*Vpbyb0reid()/(c*Rs*t0)
        return a;

    err_plsq = pow(diffbyb(),2.0)*pow(sigb,2.0) + pow(diffbyl(),2.0)*pow(sigl,2.0) + pow(diffbyd(),2.0)*pow(sigd,2.0) + pow(diffbyVs(),2.0)*pow(sigVs,2.0) + pow(diffbyRs(),2.0)*pow(sigRs,2.0) + pow(diffbyb0reid(),2.0)*pow(sigb0r,2.0) 

    err_pl = pow(err_plsq,0.5)
    return err_pl;

