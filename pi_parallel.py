from mpi4py import MPI
import random

def calculate_pi_parallel(nb):

 globCom = MPI.COMM_WORLD.Dup()
 size = globCom.size
 rank = globCom.rank
	
 points_local = 0

 for i in range(rank, nb, size):
   x,y = random.uniform(-1,1), random.uniform(-1,1)
   distance = x**2 + y**2
	
   if distance <= 1:
        points_local += 1
 points_total= globCom.reduce(points_local, op = MPI.SUM, root=0)
 if rank == 0:
   pi_approxi = 4* (points_total /nb)
   return pi_approxi

nb = 100000
pi_para = calculate_pi_parallel(nb)
print("approximation de pi en parallèle", pi_para)


