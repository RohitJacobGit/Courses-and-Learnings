from mpi4py import MPI
import csv

communicator = MPI.COMM_WORLD
rank = communicator.Get_rank()

def read_vec_from_file(file_name, comm):
    M = sum(1 for line in open(file_name))
    local_M = int(M / comm.Get_size())
    rank = comm.Get_rank()

    x = [0.0] * local_M

    with open(file_name, 'r') as f:
        for _ in range(local_M*rank):
            next(f)
        i = 0
        for row in csv.reader(f, delimiter=','):
            x[i] = float(row[0])
            i = i + 1
            if i >= local_M:
                break

    return x, M

y1, M = read_vec_from_file('y1.csv', communicator)
print(M)