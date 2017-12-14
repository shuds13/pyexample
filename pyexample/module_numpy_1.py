"""Test: Compare numpy v Python list of explicit objects (both AoS)"""

#todo: Clean this up - very quickly knocked up.

import numpy as np
import time

def numpy_v_lists(L=10000):

  #L = 10000

  libE_fields = [('sim_id',int),
                ('given',bool),	    
                ('given_time',float), 
                ('lead_rank',int),    
                ('returned',bool),    
                ('paused',bool),    
                ]


  H = np.zeros(L, dtype=libE_fields) 

  print(__doc__)
  print("Array length = %s \n" % L)

  print("Writing array values:")
  start = time.time()
  H['sim_id'][:len(H)] = 1
  end = time.time()

  time_AoS = end-start
  print("Write Time numpy AoS = %.8f" % time_AoS)

  #Check
  #print(H)


  #Array of obects
  class Point_field(object):
    """Values for a point inherit from object or tuple."""

    def __init__(self,sim_id=0,given=False,given_time=0.0,lead_rank=0,returned=False,paused=False):
        self.sim_id     = sim_id
        self.given      = given
        self.given_time = given_time
        self.lead_rank  = lead_rank
        self.returned   = returned
        self.paused     = paused

    def __repr__(self):
        return "(%s, %s, %s, %s, %s, %s)" % (
                self.sim_id,self.given,self.given_time,self.lead_rank,self.returned,self.paused)

    def __str__(self):
        return "<Point_field sim_id:%s given:%s given_time:%s lead_rank:%s returned:%s paused:%s>" % (
                self.sim_id,self.given,self.given_time,self.lead_rank,self.returned,self.paused)


  listH=[]

  for i in range(L):
    x = Point_field()
    listH.append(x)  
    #print (repr(x))

  start = time.time()
  for i in range(L):
    listH[i].sim_id = 1
  end = time.time()
  time_H = end-start
  print("Write Time List  AoS = %.8f" % time_H)

  print("Numpy Time Speedup = %.2f" % (time_H/time_AoS))



  # Repeat ---------------------------------------------------------------
  print('\nRepeat to account for potential paging issues.....')
  print("Writing array values 2:")

  start = time.time()
  H['sim_id'][:len(H)] = 2
  end = time.time()

  time_AoS = end-start
  print("Write Time numpy AoS 2 = %.8f" % time_AoS)

  start = time.time()
  for i in range(L):
    listH[i].sim_id = 2
  end = time.time()
  time_H = end-start
  print("Write Time List  AoS 2 = %.8f" % time_H)

  print("Numpy Time Speedup = %.2f" % (time_H/time_AoS))


if __name__ == "__main__":
  numpy_v_lists()
