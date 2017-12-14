"""Test numpy AoS v SoA for H layout"""

#todo: Clean this up - very quickly knocked up.

import numpy as np
import time

def numpy_SoA_v_AoS(L=10000):
  """
  Compare reading and writing from/to numpy dataset using Array of Structures v Strucure of Arrays
  """

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

  print("Writing numpy array values:")

  start = time.time()

  # Compute AoS as numpy array ---------------------------
  H['sim_id'][:len(H)] = 1
  #H['given'][:len(H)] = 1
  #H['given_time'][:len(H)] = 1.5
  #H['paused'][:len(H)] = 1

  end = time.time()
  time_AoS = end-start
  print("Write Time AoS = %.8f" % time_AoS)

  #Check
  #print(H)


  # Compute SoA as sep. numpy arrays ---------------------
  #First sep structures
  SoA_sim_id=np.zeros(L, dtype=int)
  SoA_given=np.zeros(L, dtype=bool)
  SoA_given_time=np.zeros(L, dtype=float)
  SoA_lead_rank=np.zeros(L, dtype=int)
  SoA_returned=np.zeros(L, dtype=bool)
  SoA_paused=np.zeros(L, dtype=bool)

  start = time.time()
  SoA_sim_id[:L]=1
  #SoA_given[:L]=1
  #SoA_given_time[:L]=1.5
  #SoA_paused[:L]=1

  end = time.time()
  time_SoA = end - start

  print("Write Time SoA = %.8f" % time_SoA)

  #Check
  #print(SoA_sim_id)
  #print(SoA_given)
  #print(SoA_given_time)
  #print(SoA_lead_rank)
  #print(SoA_returned)
  #print(SoA_paused)

  print("Write Time Speedup = %.2f" % (time_AoS/time_SoA) )


  # Repeat ---------------------------------------------------------------
  print('\nRepeat to account for potential paging issues.....')
  print("Writing numpy array values 2:")

  start = time.time()
  H['sim_id'][:len(H)] = 2
  end = time.time()

  time_AoS = end-start
  print("Write Time AoS 2 = %.8f" % time_AoS)

  start = time.time()
  SoA_sim_id[:L]=2
  end = time.time()

  time_SoA = end - start
  print("Write Time SoA 2 = %.8f" % time_SoA)

  print("Write Time Speedup 2 = %.2f" % (time_AoS/time_SoA) )





  # Accessing --------------------------------------------------------

  print("\nReading numpy array values:")
  #Time for appending to list might be significant???

  #AoS---------------------------------------------------
  list_AoS = []
  start = time.time()
  for i in range(L):
    list_AoS.append(H['sim_id'][i])

  #print(list_AoS)
  end = time.time()
  time_AoS = end-start
  print("Read sim_id Time AoS = %.8f" % time_AoS)

  #SoA---------------------------------------------------
  list_SoA=[]
  start = time.time()
  for i in range(L):
    list_SoA.append(SoA_sim_id[i])

  #print(list_SoA)
  end = time.time()
  time_SoA = end-start
  print("Read sim_id Time SoA = %.8f" % time_SoA)

  print("Read Time Speedup = %.2f" % (time_AoS/time_SoA) )


  #Try with pre-initialised list [*Update - looks like its the same perf.]
  #AoS---------------------------------------------------
  print("\nReading numpy array values with pre-initialised list:")
  plist_AoS = list(range(L))
  start = time.time()
  for i in range(L):
    plist_AoS[i]=(H['sim_id'][i])

  #print(plist_AoS)
  end = time.time()
  time_AoS = end-start
  print("Read sim_id Time AoS = %.8f" % time_AoS)

  #SoA---------------------------------------------------
  plist_SoA = list(range(L))
  start = time.time()
  for i in range(L):
    plist_SoA[i]=(SoA_sim_id[i])

  #print(plist_SoA)
  end = time.time()
  time_SoA = end-start
  print("Read sim_id Time SoA = %.8f" % time_SoA)

  print("Read Time Speedup = %.2f" % (time_AoS/time_SoA) )
  print("")


if __name__ == "__main__":
  numpy_SoA_v_AoS()
  
