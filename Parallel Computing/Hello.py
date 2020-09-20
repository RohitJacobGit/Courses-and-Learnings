
# https://rabernat.github.io/research_computing/parallel-programming-with-mpi-for-python.html
from mpi4py import MPI

# world_size = MPI.COMM_WORLD.Get_size()
# world_rank = MPI.COMM_WORLD.Get_rank()

# print('Hello from {0} out of {1} processes'.format(world_size, world_rank))

communicator = MPI.COMM_WORLD
size = communicator.Get_size()
rank = communicator.Get_rank()

print('Cores: {0} and core number:{1}'.format(size, rank))