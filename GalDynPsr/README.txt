# GalDynPsr Package

GalDynPsr is a package for calculating dynamical contributions in the period derivatives of pulsars in the Galactic field. It can calculate the fractional contributions or the excess terms, e.g. \dot{P}/P|_excess where P is either the orbital period or the spin period. Various dynamical contributions, including the Shklovskii effect (the contribution due to the proper motion) or due to the acceleration of the pulsar caused by the gravitational potential of the Galaxy, can be calculated. Various methods or models to perform these tasks are available in the package. Using the measured values of the periods and period derivatives, GalDynPsr can even compute the "intrinsic" values of the period derivatives, provided no other extra contribution exist. 

Details on various dynamical effects and various models to estimate those are available in Pathak and Bagchi (arXiv:1712.06590).

Brief outline of usage of GalDynPsr is given below.

# 1) Install GalDynPsr as pip3 install GalDynPsr or pip install GalDynPsr (assuming you have numpy, scipy, and galpy already installed and working)

### If wished, one can change the values of Rs (galactocentric cylindrical radius of the sun), Vs  (rotational speed of the sun) etc in parameters.in file that can be found inside the GalDynPsr (installed directory). 
## But remember that galpy also has these values defined in the file '$home/.galpyrc'. One can in principle change these values. 
# However, the Milky Way potential in galpy was fitted with Rs = 8 kpc and vs = 220 in galpy


# 2) Import GalDynPsr

import GalDynPsr

# 3) In all of the following modules, the ordering of the arguments of the functions are very important.

# 4) Calculate excess terms of modelX ** Very important, model names are case sensitive!

GalDynPsr.modelX.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) and GalDynPsr.modelX.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd)

The function Expl() calculates the excess term due to the relative acceleration of the pulsar parallel to the Galactic plane and the function Exz() calculates the excess term due to the relative acceleration of the pulsar perpendicular to the Galactic plane. Total dynamical contribution will be the sum of above two terms. Both of the above functions takes the arguments as the Galactic longitude in degrees (say ldeg), uncertainty in the Galactic longitude in degrees (say sigl), the Galactic latitude in degrees (say bdeg), uncertainty in the Galactic latitude in degrees (say sigb), the distance of the pulsar from the solar system barycenter in kpc (say dkpc), and the uncertainty in the distance in kpc (say sigd); strictly in this order. One needs to assign the values of ldeg, sigl, bdeg, sigb, dkpc, and sigd before calling the above functions.

The models that do not involve galpy can return uncertainities in the excess terms following standard error propagation method, like 

modelX.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) and modelX.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) 

where the function Errpl() returns the uncertainty in the excess terms due to the relative acceleration of the pulsar parallel to the Galactic plane and Errz() returns the uncertainty in the excess terms due to the relative acceleration of the pulsar perpendicular to the Galactic plane. The arguments are the same as before, and needs to be assigend values before using the functions.

Remeber to replace modelX by the model you  want to use, like modelA, modelLa, etc. Model names are case sensitive!

# 5) Calculate the Shklovskii term

The Shklovskii term can be calculated as GalDynPsr.Shk.Exshk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud) and the error in the Shklovskii term as GalDynPsr.Shk.errShk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)

where mu_alpha is the proper motion in the Right Ascesion direction (mas/yr), mu_delta is the proper motion in the Declination direction (mas/yr), sigmua is the uncertainty in mu_alpha, and sigmud is the uncertainty in mu_delta. dkpc is as usual the distance of the pulsar from the solar system barycenter in kpc and sigd is the uncertainty in dkpc. One needs to assign the values of these parameters first.


# 6) Print the basic parameters of the pulsars

GalDynPsr.read_parameters.Rskpc returns the Galactocentric cylindrical radius of the sun.

GalDynPsr.read_parameters.Vs returns the rotational speed of the sun.

GalDynPsr.read_parameters.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd) returns the value of Galactocentric cylindrical radius of the pulsar in kpc and GalDynPsr.read_parameters.z(ldeg, sigl, bdeg, sigb, dkpc, sigd) returns the verical height of the pulsar from the Galactic plane. The meaning of the arguments are as usual:

One can get the uncertainty in the Galactocentric cylindrical radius of the pulsar in kpc using GalDynPsr.read_parameters.ErrRpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd) and the uncertainty in the verical height as GalDynPsr.read_parameters.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd).

Obviously,  one first needs to assign the values of ldeg, sigl, bdeg, sigb, dkpc, and sigd.


# 7) For a pulsar in a globular cluster, one can read the cluster parameters, e.g. the Galactic longitude, latitude and the distance from the Harric catalogue (GC_harris.txt coming with GalDynPsr), and calculate crude values of the dynamical terms

One first needs to import the module to read Harris cataloge as:

import GalDynPsr.ReadGC as readgc

Then one can input the name of the cluster, e.g. readgc.gcinput("47Tuc")

Then the excess terms using modelX can be calculated as 

sigl=0.000001
sigb=0.000001
sigd=0.000001

GalDynPsr.modelX.Expl(readgc.ldeg,sigl,readgc.bdeg,sigb,readgc.dkpc,sigd) # the parallel component
GalDynPsr.modelX.Exz(readgc.ldeg,sigl,readgc.bdeg,sigb,readgc.dkpc,sig) # the perpendicular component

Note that the Harris catalogue does not provide uncertainties in ldeg, bdeg and dkpc. That is why we need to define them before calculating the excess terms. As the pulsar parameters differ from the cluster parameters as in Harris catalogue, it is meaningless to calculate uncetrainities. So, one SHOULD simply call the above functions as:

GalDynPsr.modelX.Expl(readgc.ldeg,0.0,readgc.bdeg,0.0,readgc.dkpc,0.0) # the parallel component
GalDynPsr.modelX.Exz(readgc.ldeg,0.0,readgc.bdeg,0.0,readgc.dkpc,0.0) # the perpendicular component

# 8) Calculation of instrinsic period. Ordering of the arguments is important.


First assign values of ldeg, sigl, bdeg, sigb, dkpc, sigd (meaning of the parameters are as usual) and calculate the excess terms as usual:

Ex_pl =  GalDynPsr.modelA.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) # excess term parallel to the Galactic plane

Ex_z =  GalDynPsr.modelA.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) # excess term perpendicular to the Galactic plane

errpl =  GalDynPsr.modelA.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) # uncertainty in the parallel term

errz =  GalDynPsr.modelA.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) # uncertainty in the parallel term

Ex_shk =  GalDynPsr.Shk.Exshk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud) # excess term due to the Shklovskii effect

errshk =  GalDynPsr.Shk.errShk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud) # uncertainties in the Shklovskii term


Now assign the values of the period 'P' in seconds, the uncertainy in period 'sigP' in seconds, the measured value of the period derivative 'Pdot_obs' in seconds/seconds and the uncertainty in the measured value of the period derivative 'sigPdot' in seconds/seconds; and calculate the dynamically caused values of the period derivatives (in seconds/seconds) as:

GalDynPsr.pdotint.PdotExpl(Ex_pl,P) # due to the parallel component of the acceleration

GalDynPsr.pdotint.PdotExz(Ex_z,P) # due to the perpendicular component of the acceleration

GalDynPsr.pdotint.PdotShk(Ex_shk,P) # due to the Shklovskii effect

The total dynamically caused value of Pdot is the addition of the above three terms. The intrinsic value of the period derivative can be calculated by subtracting that sum from the measured value of the period derivative. GalDynPsr can perform this task for us by:

GalDynPsr.pdotint.Pdotint(Ex_pl,Ex_z,Ex_shk,Pdot_obs,P) 

The total dynamical contribution in the period derivative, i.e. the sum of GalDynPsr.pdotint.PdotExpl(Ex_pl,P) and GalDynPsr.pdotint.PdotExz(Ex_z,P) can be printed as:
GalDynPsr.pdotint.PdotGal(Ex_pl,Ex_z,P)

One can calculate the uncertainity in the above period drivatives as:

GalDynPsr.pdotint.ErrPdotExpl(Ex_pl,errpl,P,sigP) # uncertainty in the planar contribution to the period derivative

GalDynPsr.pdotint.ErrPdotExz(Ex_z,errz,P,sigP) # uncertainty in the perpendicular contribution to the period derivative

GalDynPsr.pdotint.ErrPdotGal(Ex_pl,errpl,Ex_z,errz,P,sigP) # uncertainty in the sum of planar and perpendicular contributions to the period derivative
 
GalDynPsr.pdotint.ErrPdotShk(Ex_shk,errshk,P,sigP) # uncertainty in the Shklovskii term contribution to the period derivative

GalDynPsr.pdotint.ErrPdotint(Ex_pl,errpl,Ex_z,errz,Ex_shk,errshk,Pdot_obs,sigPdot_obs,P,sigP) # uncertainty in the intrinsic period derivative

* Remember the fact that GalDynPsr reads the value of the period in seconds. Orbital periods are usually measured in days (or sometimes in hours). One needs to convert those values in seconds before calling GalDynPsr modules.



### All the above points will be clearer from the following examples ################
#####  Instructions to use GalDynPsr #####  

# Call GalDynPsr as:-


import GalDynPsr




## Provide the following values in your code ###

# ldeg = Galactic logitude in degrees, bdeg = Galactic latitude in degrees, dkpc = distance to pulsar in kpc, sigl = error in ldeg, sigb = error in bdeg, sigd = error in dkpc

########### Example-1 #################
ldeg =20.0
sigl = 2.0

bdeg = 45.0
sigb = 0.2

dkpc = 1.2
sigd = 0.3



############# Extract important parameters say values of Rp (in kpc) and z (in kpc) and errors in them  ##########




Rpkpc = GalDynPsr.read_parameters.Rpkpc(ldeg, sigl, bdeg, sigb, dkpc, sigd)

zkpc = GalDynPsr.read_parameters.z(ldeg, sigl, bdeg, sigb, dkpc, sigd)

ErrRp = GalDynPsr.read_parameters.ErrRp(ldeg, sigl, bdeg, sigb, dkpc, sigd)

Errz = GalDynPsr.read_parameters.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd)


#################  Compute excess Shklovskii term. Here Exshk() calculates the dynamical contribution (or the excess term) due to Shklovskii effect and errShk() calculates the error in that #################################

#### We need to provide the values of proper motion in right ascesion direction (with the corresponding error) and proper motion in the declination direction (with the corresponding error)########

##mu_alpha = proper motion in Right Ascesion direction (mas/yr), mu_delta = proper motion in Declination direction (mas/yr), sigmua = error in mu_alpha, and sigmud = error in mu_delta



mu_alpha = 22.0
sigmua = 0.2
 
mu_delta = 1.2
sigmud = 0.3


ExcessSh = GalDynPsr.Shk.Exshk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)

sigmaExcessSh = GalDynPsr.Shk.errShk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)



### Example 1.1 ###

### Model A (can propagate error)######


Apl = GalDynPsr.modelA.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Az = GalDynPsr.modelA.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term


Aplsigma = GalDynPsr.modelA.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Azsigma = GalDynPsr.modelA.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term


totalA = Apl + Az

SigmatotalA = math.sqrt(Aplsigma*Aplsigma+Azsigma*Azsigma) # assuming no correlation between excepp_pl and excess_z


### Example 1.2 ###

### Model B (can propagate error)######


Bpl = GalDynPsr.modelB.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Bz = GalDynPsr.modelB.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term


Bplsigma = GalDynPsr.modelB.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Bzsigma = GalDynPsr.modelB.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term


totalB = Bpl + Bz

SigmatotalB = math.sqrt(Bplsigma*Bplsigma+Bzsigma*Bzsigma) # assuming no correlation between excepp_pl and excess_z



### Example 1.3 ###

### Model C (can propagate error)######


Cpl = GalDynPsr.modelC.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Cz = GalDynPsr.modelC.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term


Cplsigma = GalDynPsr.modelC.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Czsigma = GalDynPsr.modelC.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term


totalC = Cpl + Cz

SigmatotalC = math.sqrt(Cplsigma*Cplsigma+Czsigma*Czsigma) # assuming no correlation between excepp_pl and excess_z


### Example 1.4 ###

### Model D (can propagate error)######


Dpl = GalDynPsr.modelD.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Dz = GalDynPsr.modelD.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term


Dplsigma = GalDynPsr.modelD.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Dzsigma = GalDynPsr.modelD.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term


totalD = Dpl + Dz

SigmatotalD = math.sqrt(Dplsigma*Dplsigma+Dzsigma*Dzsigma) # assuming no correlation between excepp_pl and excess_z



### Example 1.5 ###

############  Model Ea (error only in parallel component)   ###############


Eapl = GalDynPsr.modelEa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

SigmaEapl = GalDynPsr.modelEa.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Eaz = GalDynPsr.modelEa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalEa = Eapl+Eaz


### Example 1.6 ###

############  Model Eb (error only in parallel component)   ###############


Ebpl = GalDynPsr.modelEb.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

SigmaEbpl = GalDynPsr.modelEb.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Ebz = GalDynPsr.modelEb.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalEb = Ebpl+Ebz


### Example 1.7 ###

############  Model Fa (error only in parallel component)   ###############



Fapl = GalDynPsr.modelFa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

SigmaFapl = GalDynPsr.modelFa.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Faz = GalDynPsr.modelFa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalFa = Fapl+Faz



### Example 1.8 ###

############  Model Fb (error only in parallel component)   ###############


Fbpl = GalDynPsr.modelFb.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

SigmaFbpl = GalDynPsr.modelFb.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the planar contribution to the excess term

Fbz = GalDynPsr.modelFb.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalFb = Fbpl+Fbz


### Example 1.9 ###

############  Model Ga (error in perpendicular component)   ###############


Gapl = GalDynPsr.modelGa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Gaz = GalDynPsr.modelGa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaGaz = GalDynPsr.modelGa.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalGa = Gapl+Gaz


### Example 1.10 ###

############  Model Gb (error in perpendicular component)  ###############


Gbpl = GalDynPsr.modelGb.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Gbz = GalDynPsr.modelGb.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaGbz = GalDynPsr.modelGb.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalGb = Gbpl+Gbz




### Example 1.11 ###

############  Model Ha (error in perpendicular component)   ###############


Hapl = GalDynPsr.modelHa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Haz = GalDynPsr.modelHa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaHaz = GalDynPsr.modelHa.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalHa = Hapl+Haz



### Example 1.12 ###

############  Model Hb (error in perpendicular component)   ###############


Hbpl = GalDynPsr.modelHb.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Hbz = GalDynPsr.modelHb.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaHbz = GalDynPsr.modelHb.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalHb = Hbpl+Hbz




### Example 1.13 ###

############  Model Ia (error in perpendicular component)  ###############


Iapl = GalDynPsr.modelIa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Iaz = GalDynPsr.modelIa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaIaz = GalDynPsr.modelIa.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalIa = Iapl+Iaz



### Example 1.14 ###

############  Model Ib (error in perpendicular component)   ###############


Ibpl = GalDynPsr.modelIb.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Ibz = GalDynPsr.modelIb.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaIbz = GalDynPsr.modelIb.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalIb = Ibpl+Ibz



### Example 1.15 ###

############  Model Ja (error in perpendicular component)   ###############


Japl = GalDynPsr.modelJa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Jaz = GalDynPsr.modelJa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaJaz = GalDynPsr.modelJa.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalJa = Japl+Jaz


### Example 1.16 ###

############  Model Jb (error in perpendicular component)  ###############


Jbpl = GalDynPsr.modelJb.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Jbz = GalDynPsr.modelJb.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

SigmaJbz = GalDynPsr.modelJb.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the error in the perpendicular contribution to the excess term

totalJb = Jbpl+Jbz



### Example 1.17 ###

############  Model Ka (full galpy, no error)  ###############


Kapl = GalDynPsr.modelLa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Kaz = GalDynPsr.modelLa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalKa = Kapl+Kaz



### Example 1.18 ###

############  Model Kb (full galpy, no error)   ###############


Kbpl = GalDynPsr.modelLa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Kbz = GalDynPsr.modelLa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalKb = Kbpl+Kbz




### Example 1.19 ###

############  Model La (full galpy, no error)   ###############



Lapl = GalDynPsr.modelLa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Laz = GalDynPsr.modelLa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalLa = Lapl+Laz



### Example 1.20 ###

############  Model Lb (full galpy, no error)   ###############



Lbpl = GalDynPsr.modelLa.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the planar contribution to the excess term

Lbz = GalDynPsr.modelLa.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd) #calculates the perpendicular contribution to the excess term

totalLb = Lbpl+Lbz



#############################

######### For a Globular Cluster Pulsar #############################

#Check names of Globular Clusters from GC_Harris.txt and write the name of the cluster. We do not include errors in this case.

### Example 2 ###

#Getting Excess_pl for model A for the GC 47Tuc:-

#GalDynPsr.ReadGC.gcinput("GC Name") finds the GC in the GC_Harris list and calculates the corresponding galactic coordinates and distance to the GC. Input the arguments to any model as:- (GalDynPsr.ReadGC.ldeg,0.,GalDynPsr.ReadGC.bdeg,0.,GalDynPsr.ReadGC.dkpc,0.)



GalDynPsr.ReadGC.gcinput("47Tuc")

Apl = GalDynPsr.modelA.Expl(GalDynPsr.ReadGC.ldeg,0.,GalDynPsr.ReadGC.bdeg,0.,GalDynPsr.ReadGC.dkpc,0.)

Az = GalDynPsr.modelA.Exz(GalDynPsr.ReadGC.ldeg,0.,GalDynPsr.ReadGC.bdeg,0.,GalDynPsr.ReadGC.dkpc,0.)


# Similarly for other models.



#############################

######################### For Intrinsic period derivative calculations ###############################

## Parameters required for spin period derivative calcuations:- P = period in seconds, sigP = error in P in second, Pdot_obs = measured period derivative in ss^-1, sigPdot_obs = error in Pdot_obs

#PdotExpl(Excess_pl,P) calculates the planar contribution to the period derivative 

#PdotExz(Excess_z,P) calculates the perpendicular contribution to the period derivative
 
#PdotGal(Excess_pl,Excess_z,P) calculates the sum of planar and perpendicular contributions to the period derivative

#PdotShk(Excess_shk,P) calculates the Shklovskii contribution to the period derivative

#Pdotint(Excess_pl,Excess_z,Excess_shk,Pdot_obs,P) calculates the intrinsic period derivative


#ErrPdotExpl(Excess_pl,error_Excess_pl,P,sigP) calculates the error in the planar contribution to the period derivative

#ErrPdotExz(Excess_z,error_Excess_z,P,sigP) calculates the error in the perpendicular contribution to the period derivative

#ErrPdotGal(Excess_pl,error_Excess_pl,Excess_z,error_Excess_z,P,sigP) calculates the error in the sum of planar and perpendicular contributions to the period derivative

#ErrPdotShk(Excess_shk,error_Excess_shk,P,sigP) calculates the error in the Shklovskii contribution to the spin period derivative

#ErrPdotint(Excess_pl,error_Excess_pl,Excess_z,error_Excess_z,Excess_shk,error_Excess_shk,Pdot_obs,sigPdot_obs,P,sigP) calculates the error in the intrinsic period derivative




### Example 3.1 ###

# Say using La


ldeg =20.0
sigl = 2.0

bdeg = 45.0
sigb = 0.2

dkpc = 1.2
sigd = 0.3

mu_alpha = 22.0
sigmua = 0.2
 
mu_delta = 1.2
sigmud = 0.3

# Example spin period and itsderivatives:-

#P = 0.003061844088094608
#sigP = 0.000000000000000015 

#Pdot_obs = 0.959013e-20
#sigPdot_obs = 0.000014e-20


#Example orbital period and its derivatives (convert the period and corresponding error in seconds):-

P = 1.198512575184*24.0*3600.0

sigP = 0.000000000013*24.0*3600.0


Pdot_obs = 4.8e-14
sigPdot_obs = 1.1e-14

##


Ex_pl = GalDynPsr.modelA.Expl(ldeg, sigl, bdeg, sigb, dkpc, sigd)

Ex_z = GalDynPsr.modelA.Exz(ldeg, sigl, bdeg, sigb, dkpc, sigd)

errpl = GalDynPsr.modelA.Errpl(ldeg, sigl, bdeg, sigb, dkpc, sigd)

errz = GalDynPsr.modelA.Errz(ldeg, sigl, bdeg, sigb, dkpc, sigd)

Ex_shk = GalDynPsr.Shk.Exshk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)

errshk = GalDynPsr.Shk.errShk(dkpc, sigd, mu_alpha, sigmua, mu_delta, sigmud)



PdotExpl =  GalDynPsr.pdotint.PdotExpl(Ex_pl,P)

PdotExz =  GalDynPsr.pdotint.PdotExz(Ex_z,P)

PdotGal =  GalDynPsr.pdotint.PdotGal(Ex_pl,Ex_z,P)

PdotShk =  GalDynPsr.pdotint.PdotShk(Ex_shk,P)

Pdotint = GalDynPsr.pdotint.Pdotint(Ex_pl,Ex_z,Ex_shk,Pdot_obs,P)


#Errors in spin period derivatives:-

ErrPdotExpl =  GalDynPsr.pdotint.ErrPdotExpl(Ex_pl,errpl,P,sigP)

ErrPdotExz = GalDynPsr.pdotint.ErrPdotExz(Ex_z,errz,P,sigP)

ErrPdotGal =  GalDynPsr.pdotint.ErrPdotGal(Ex_pl,errpl,Ex_z,errz,P,sigP)

ErrPdotShk = GalDynPsr.pdotint.ErrPdotShk(Ex_shk,errshk,P,sigP)

ErrPdotint =  GalDynPsr.pdotint.ErrPdotint(Ex_pl,errpl,Ex_z,errz,Ex_shk,errshk,Pdot_obs,sigPdot_obs,P,sigP)




#==========================================================================================
##### Contents of the Package ####

Datafiles:

parameters.in: Input file contains values of different constants which are subject to change with improvements in measurements. User can change the values of constants if the need be. These constants are Vs, sigVs (error in Vs), Rskpc (Rs in kpc units), sigRs (error in Rskpc), b0reid14 (dv/dR), sigb0r (error in dv/dR), b0dt91 (slope parameter), sigb0dt (error in slope parameter).

GC_Harris.txt: Names and Galactic coordinates of the Globular Clusters.

README.txt: Contents of this README.md file inside package along with code files.

Description of different codes:

read_parameters.py: Contains various constants used in the package as well as functions to calculate Rp(kpc) and z(kpc) and their corresponding errors. 


ExcessZ.py:  Calculates az/c, both Nice-Taylor (1995) expression as well as our fit of HF2004

Excesspl.py: Calculates apl/c. Can take any value of the slope parameter dv/dR from the parameter file. b0 = (Vs/Rs)*(dV/dR) = 0 is the conventional.

modelA.py: Model A - Calculates apl_old/c (i.e. b0 = 0; DT91) and az_NT95. 

modelB.py: Model B - Calculates apl_old/c (i.e. b0 = 0; DT91) and az_HF04.

modelC.py: Model C - Calculates apl_new/c (i.e. dv/dR = -0.2; Reid2014) and az_NT95.

modelD.py: Model D - Calculates apl_new/c (i.e. dv/dR = -0.2; Reid2014) and az_HF04.

modelEa.py: Model Ea - Calculates apl_old/c (i.e. b0 = 0; DT91) and ‘zforce’ in galpy (without BH)
modelEb.py: Model Eb - Calculates apl_old/c (i.e. b0 = 0; DT91) and ‘zforce’ in galpy (with BH)

modelFa.py: Model Fa - Calculates apl_new/c (i.e. dv/dR = -0.2; Reid2014) and ‘zforce’ in galpy (without BH)
modelFb.py: Model Fb - Calculates apl_new/c (i.e. dv/dR = -0.2; Reid2014) and ‘zforce’ in galpy (with BH)

modelGa.py: Model Ga - Calculates apl/c using Vp'/Vs from galpy (without BH) and az_NT95
modelGb.py: Model Gb - Calculates apl/c using Vp'/Vs from galpy (with BH) and az_NT95

modelHa.py: Model Ha - Calculates ‘Rforce’ in galpy (without BH) and az_NT95
modelHb.py: Model Hb - Calculates ‘Rforce’ in galpy (with BH) and az_NT95

modelIa.py: Model Ia - Calculates apl/c using Vp'/Vs from galpy (without BH) and az_HF04
modelIb.py: Model Ib - Calculates apl/c using Vp'/Vs from galpy (with BH) and az_HF04

modelJa.py: Model Ja - Calculates ‘Rforce’ in galpy (without BH) and az_HF04
modelJb.py: Model Jb - Calculates ‘Rforce’ in galpy (with BH) and az_HF04

modelKa.py: Model Ka - Calculates apl/c using Vp'/Vs from galpy (without BH) and ‘zforce’ in galpy (without BH)
modelKb.py: Model Kb - Calculates apl/c using Vp'/Vs from galpy (with BH) and ‘zforce’ in galpy (with BH)

modelLa.py: Model La - Calculates ‘Rforce’ in galpy (without BH) and ‘zforce’ in galpy (without BH)
modelLb.py: Model Lb - Calculates ‘Rforce’ in galpy (with BH) and ‘zforce’ in galpy (with BH)

Shk.py: Calculates the Shklovskii term d(mu_T*mu_T)/c. Takes user input of proper motion in right ascension and declination.

galpyMWpl.py: Using vcirc function in galpy to get Vp'(without BH) and eventually apl/c 

galpyMWBHpl.py: Using vcirc function in galpy to get Vp'(with BH) and eventually apl/c 

galpyMWRfo.py: Using evaluateRforces function in galpy(without BH) to get apl/c 

galpyMWBHRfo.py: Using evaluateRforces function in galpy(with BH) to get apl/c

err_excesspl_Damour.py: Calculates error for Excess_pl (DT91)

err_excesspl_Reid.py: Calculates error for Excess_pl (Reid2014)

err_HFhigh.py: Calculates error for Excess_z (our fit for HF04 data)

err_HFlow.py: Calculates error for Excess_z (our fit for HF04 data)

err_NT.py: Calculates error for Excess_z (NT95)

err_Shklovskii.py: Calculates error for Excess_Shk


#==========================================================================================================================================

Though the description of models is provided in the paper, for the sake of completeness we are still providing that here.

Description of Models:-
 
Model-A: apl_old/c (i.e. b0 = 0; DT91) and Z_NT95
Model-B: apl_old/c (i.e. b0 = 0; DT91) and Z_HF04
Model-C: apl_new/c (i.e. dv/dR = -0.2; Reid2014) and Z_NT95
Model-D: apl_new/c (i.e. dv/dR = -0.2; Reid2014) and Z_HF04

Model-Ea: apl_old/c (i.e. b0 = 0; DT91) and ‘zforce’ in galpy (without BH)
Model-Eb: apl_old/c (i.e. b0 = 0; DT91) and ‘zforce’ in galpy (with BH)

Model-Fa: apl_new/c (i.e. dv/dR = -0.2; Reid2014) and ‘zforce’ in galpy (without BH)
Model-Fb: apl_new/c (i.e. dv/dR = -0.2; Reid2014) and ‘zforce’ in galpy (with BH)

Model-Ga: Using Vp'/Vs from galpy (without BH) and Z_NT95
Model-Gb: Using Vp'/Vs from galpy (with BH) and Z_NT95

Model-Ha: ‘Rforce’ in galpy (without BH) and Z_NT95
Model-Hb: ‘Rforce’ in galpy (with BH) and Z_NT95

Model-Ia: Using Vp'/Vs from galpy (without BH) and Z_HF04
Model-Ib: Using Vp'/Vs from galpy (with BH) and Z_HF04

Model-Ja: ‘Rforce’ in galpy (without BH) and Z_HF04
Model-Jb: ‘Rforce’ in galpy (with BH) and Z_HF04

Model-Ka: Using Vp'/Vs from galpy (without BH) and ‘zforce’ in galpy (without BH)
Model-Kb: Using Vp'/Vs from galpy (with BH) and ‘zforce’ in galpy (with BH)

Model-La: ‘Rforce’ in galpy (without BH) and ‘zforce’ in galpy (without BH)
Model-Lb: ‘Rforce’ in galpy (with BH) and ‘zforce’ in galpy (with BH)



Reid2014: Reid M. J., Menten K. M., Brunthaler A., Zheng X. W., Dame T. M., 2014, ApJ, 783, 130.

DT91: Damour T., Taylor J.H., 1991, ApJ, 366, 501.

NT95: Nice D.J., Taylor J.H., 1995, ApJ, 441, 429.

HF04: Holmberg J., Flynn C., 2004, MNRAS, 352, 440.


############################################################

