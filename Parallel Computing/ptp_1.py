from mpi4py import MPI
import numpy as np


communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

if rank == 0:
    
    data_size_sent = 9
    communicator.send(data_size_sent, dest=1)  # int not caps 'send'

    data_sent = np.linspace(0,2,data_size_sent)
    communicator.Send(data_sent, dest=1) # numpy array CAPS 'Send'

elif rank == 1:

    data_size_received = communicator.recv(source=0)  # int not caps 'recv'
    print('Size of data to receive: ', data_size_received)

    # Allocation of data in empty array
    data_received = np.empty(data_size_received, dtype='d')
    communicator.Recv(data_received, source=0)  # numpy array CAPS 'Recv'
    print('Data Received and allocated: ', data_received)
