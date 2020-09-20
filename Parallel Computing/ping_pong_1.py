
from mpi4py import MPI

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

if rank == 0:
    data_to_send = 41
    communicator.send(data_to_send, dest=1)  # 1

    received_value = communicator.recv(source=1)  # 4
    print('Received Value: ', received_value)

    communicator.send(received_value, dest=1) #5
    
    updated_received_value = communicator.recv(source=1) #8
    print('Updated Received Value: ', updated_received_value)

elif rank == 1:
    received_value = communicator.recv(source=0)  # 2
    new_value = received_value+1
    communicator.send(new_value, dest=0)  # 3

    received_value_to_update = communicator.recv(source=0) #6
    updated_new_value = received_value_to_update+1
    communicator.send(updated_new_value, dest=0) #7
