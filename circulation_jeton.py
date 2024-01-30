from mpi4py import MPI

globCom = MPI.COMM_WORLD
size = globCom.size
rank= globCom.Get_rank()

#initialisation du jeton par le processus de rang 0
if rank == 0:
 jeton = 1
globCom.Barrier()

#circulation du jeton dans l'anneau
jeton = jeton+1
globCom.send(jeton, dest=(rank+1) % size)
jeton = jeton +1


#affichage du jeton par le processus de rang 0
print("Le jeton a parcouru l'anneau et est maintenant égal à :",jeton)
  


