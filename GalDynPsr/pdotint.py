import math




def PdotExpl(Ex_pl,P):
   return Ex_pl*P;


def PdotExz(Ex_z,P):
   return Ex_z*P;


def PdotGal(Ex_pl,Ex_z,P):
   a = (Ex_pl + Ex_z)*P
   return a;


def PdotShk(Ex_shk,P):
   return Ex_shk*P;


def Pdotint(Ex_pl,Ex_z,Ex_shk,Pdot_obs,P):
   a1 = (Ex_pl + Ex_z + Ex_shk)*P
   a2 = Pdot_obs - a1
   return a2;





def ErrPdotExpl(Ex_pl,errpl,P,sigP):
   Err_Pdot_Expl = ((P*errpl)**2. + (Ex_pl*sigP)**2.)**0.5
   return Err_Pdot_Expl;


def ErrPdotExz(Ex_z,errz,P,sigP):
   Err_Pdot_Exz =  ((P*errz)**2. + (Ex_z*sigP)**2.)**0.5
   return Err_Pdot_Exz;


def ErrPdotGal(Ex_pl,errpl,Ex_z,errz,P,sigP):
   err_ab = ((errpl)**2.+(errz)**2.)**0.5
   Err_Pdot_Gal = ((P*err_ab)**2.+((Ex_pl + Ex_z)*sigP)**2.)**0.5   
   return Err_Pdot_Gal;


def ErrPdotShk(Ex_shk,errshk,P,sigP):
   Err_Pdot_Shk = ((P*errshk)**2. + (Ex_shk*sigP)**2.)**0.5
   return Err_Pdot_Shk;


def ErrPdotint(Ex_pl,errpl,Ex_z,errz,Ex_shk,errshk,Pdot_obs,sigPdot_obs,P,sigP):
   err_pdotbypdyn = ((errpl)**2.+(errz)**2.+(errshk)**2.)**0.5
   err_pdotbypdynP = ((P*err_pdotbypdyn)**2.+((Ex_pl + Ex_z + Ex_shk)*sigP)**2.)**0.5
   Err_Pdot_int = ((err_pdotbypdynP)**2.+(sigPdot_obs )**2.)**0.5
   return Err_Pdot_int;



