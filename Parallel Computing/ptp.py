from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

if rank == 0:
    data = {'a':1,'b':2}
    communicator.send(data, dest=1)
elif rank == 1:
    data = communicator.recv(source=0)
    print('Core number: 1, data = ', data)