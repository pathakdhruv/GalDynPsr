
import math
import numpy as np
import pkg_resources
from GalDynPsr import read_parameters as par



def readGCfunc():
   global n1,dat,name,aname,gl,gb,dd,b1,dkpc1,zkpc1,bdeg,ldeg
   dat = []
   name = []
   aname = []
   gl = []
   gb = []
   dd = []
   b1 = []
   dkpc1 = [] 
   zkpc1 = []
   DB_FILE1 = pkg_resources.resource_filename(__name__, 'GC_harris.txt')
   f1 = open(DB_FILE1,'r')
   n1 = 0
   for line in f1:
      s = line.split()
      dat.append(s)
      n1 = n1 +1  

   for j in range(0,n1):
      name.append(dat[j][0])
      aname.append(dat[j][1])
      gl.append(float(dat[j][2]))
      gb.append(float(dat[j][3])) 
      dd.append(float(dat[j][4]))
      b1=gb[j]*par.degtorad
      dkpc1=dd[j]
      zkpc1=dkpc1*math.sin(b1)
     
   f1.close()
   return None;




def gcinput(ans):
    readGCfunc()
    global flag, bdeg, ldeg, dkpc
    flag = 0
    for i in range(0,n1):
      if ans == dat[i][0] or ans == dat[i][1] and ans != 'NA':
         flag = 1
         print ("Found !")
         print (dat[i][0], dat[i][1])
         ldeg = float(dat[i][2])
         bdeg = float(dat[i][3])
         dkpc = float(dat[i][4])
        
        
      elif i==156 and flag ==0:
         print ("Cluster Not Found. Check name again.")
    return None;








