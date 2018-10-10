import math
import numpy as np


global K,dkpc,muT,sigd,mu_alpha, sigmua, mu_delta, sigmud


def err_Shkl(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud):
    mu_T = pow((mu_alpha*mu_alpha + mu_delta*mu_delta),0.5) # mas/yr
    K = 2.42924681374e-21
    def Ex_shkbyd():
        a = K*mu_T*mu_T
        return a;

    def Ex_shkbymua():
        a = 2.0*K*dkpc*mu_alpha
        return a;

    def Ex_shkbymud():
        a = 2.0*K*dkpc*mu_delta
        return a;

    err_shksq = pow(Ex_shkbyd(),2.0)*pow(sigd,2.0) + pow(Ex_shkbymua(),2.0)*pow(sigmua,2.0) + pow(Ex_shkbymud(),2.0)*pow(sigmud,2.0) 
    err_Shk = pow(err_shksq,0.5)
    return err_Shk;

