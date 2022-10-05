from mpi4py import MPI
import utils as ut
import DMFT_iteration as it

if __name__ == "__main__":
    # Setup the MPI pool
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Fix a seed for reproducibility
    ut.set_seed(comm)

    # Read the parameters from the parameter file
    parameters = ut.read_parameters("parameters.json")

    # Clean the log output file
    ut.clean_log(comm)

    ut.printMPI(f"Initialising...", comm)

    # Compute the starting ansatz
    if rank == 0:
        it.init(parameters)
    comm.Barrier()

    # Perform the DMFT iterations
    n_iterations = int(parameters["n_iterations"])
    for iteration in range(n_iterations):
        ut.printMPI(f"Iteration {iteration+1} of {n_iterations}", comm)
        it.iterate(comm, iteration, parameters)
        comm.Barrier()
