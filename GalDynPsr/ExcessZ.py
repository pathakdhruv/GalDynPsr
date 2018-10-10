import math
import numpy as np
from GalDynPsr import read_parameters as par





def g(x):
      return (-1.08100761142e-19)*((0.58*x) + (1.25*x)/((x*x + 0.0324)**(0.5)))

def fhigh(x):
    p1 = 0.541428 
    q1 = 1.42607 
    r1 = 0.046727
    a = p1*x + q1*x/((x*x + r1)**(0.5))
    return -a;

def flow(x):
    p4 = 0.471183
    q4 = 1.56477
    r4 = 0.409007 
    s4 = 0.00937683
    t4 = 0.178331
    a = p4*x + q4*x/((x*x + r4*r4)**(0.5)) + s4*x/((x*x + t4*t4)**(1.5))
    return -a;




