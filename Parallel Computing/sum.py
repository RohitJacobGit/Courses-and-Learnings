from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

if rank == 0:
    received_source_1 = communicator.recv(source=1) #2
    received_source_2 = communicator.recv(source=2) #4

    summed = received_source_1 + received_source_2 #5

    communicator.send(summed, dest=1) #6
    communicator.send(summed, dest=2) #8

elif rank == 1:
    communicator.send(3, dest = 0) #1

    print('The sum is: ', communicator.recv(source=0)) #7
    
elif rank == 2:
    communicator.send(2, dest = 0) #3

    print('The sum is: ', communicator.recv(source=0)) #9
