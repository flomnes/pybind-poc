import example as ex
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()



if rank == 0:
    pick=ex.Pickleable("Hello")
    comm.send(pick, dest=1, tag=11)
    print(f"rank={rank}, sent data={pick}")
elif rank == 1:
    data=comm.recv(source=0, tag=11)
    print(f"rank={rank}, received data={data}")

