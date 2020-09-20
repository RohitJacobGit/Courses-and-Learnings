from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

if rank == 0:
    data_to_send = 41
    communicator.send(data_to_send, dest=1) #1

    received_value = communicator.recv(source=1) #4
    print('Received Value: ', received_value)

elif rank ==1:
    received_value = communicator.recv(source=0) #2
    new_value = received_value+1
    communicator.send(new_value, dest=0) #3