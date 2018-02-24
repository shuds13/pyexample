"""
Test: Manager sends messages to workers which print they have received.

Run on at least two processors:
eg. For 4 processors:
mpiexec -np 2 module_mpi4py_1.py
"""

from __future__ import division
from __future__ import absolute_import

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def man_wrk_test():
    """
    Determine if current process is manager or worker
    """
    
    if rank==0:
        manager_main(comm)
    else:
        worker_main(comm)
      
def manager_main(comm):
    """
    Send simulation specs to each worker
    """
    
    sim_specs = {'in': 'x', 'out': 'y'}
    workers = range(1,comm.Get_size())
    for w in workers:
        print("Manager sending to worker %d" % w)
        comm.send(obj=sim_specs, dest=w)
        
def worker_main(comm):
    """
    Receive simulation specs from manager and print
    """
    
    my_specs = comm.recv(buf=None, source=0)   
    print("Worker %d:  specs: %s" % (rank, my_specs['in']))

if __name__ == "__main__":
  man_wrk_test()
