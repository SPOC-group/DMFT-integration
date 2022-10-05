# Rigorous-dynamical-mean-field-theory
Code for integrating the DMFT equation as in [ADD ARXIV LINK]

![Pretty DMFT picture] (Long_times.png)

# Dependencies
- Numpy version 1.22.2
- Scipy version 1.7.1
- MPI4PY version 3.0.3
- Matplotlib version 3.5.1
- Pandas version 1.3.2

Note that MPI4PY also requires a MPI implementation. The code has been tested with MPICH. We refer to the MPI4PY documentation for further information.

A convinient way to setup the enviroment is by using conda and environment.yml

# How to integrate the equations
The first place to look at is the loss_functions.py file. It contains the definition of the loss functions and the sample selection process (so you can specify the loss and the algorithm).

The next step is to specify the parameters in the file parameters.json. We list all the parameters and their meaning here:

- m_0: starting overlap with the optimal weights
- alpha: ratio of number of samples and dimension of the weights
- b: fraction of the number of samples to be included in each batch
- dt: learning rate
- T: number of gradient descent iterations
- n_samples: number of stochastic processes sampled
- n_iterations: number of iterations in the DMFT fixed point scheme
- damping: weight to average the current guess of the kernels with the previous one. 1 ignores the previous one, 0 ignores the previous one.

You can compute the DMFT fixed point iteration by running main.py. 

It's necessary to have a folder caller 'data' (the script will not return an error if it's not there).

We believe it's possible to use the code without modifying the main.py file and simply changing the parameters.json configuration file. Changing main.py can be usefull to define custom iterations.


# How view the results
A convenient plotting script is provided. Running plot.py will visualise the last steps of the iteration. We also provided a numerical simulation, which can be used to compare the results of the DMFT procedure. Any personal computer should reproduce comparison.png in approximately 1 minute using a single core.
