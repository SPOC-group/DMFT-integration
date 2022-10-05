import utils_plot as utp
import matplotlib.pyplot as plt
import utils as ut


parameters = ut.read_parameters("parameters.json")

utp.plot_magnetisation_simulations(parameters)
for iteration in range(20, 30):
    utp.plot_magnetisation(parameters, iteration)


plt.legend()
plt.xlabel("Time")
plt.ylabel("Magnetisation")
plt.xscale("log")
plt.savefig("Long_times.png")
plt.show()


utp.plot_magnetisation_simulations(parameters)
for iteration in range(0, 10):
    utp.plot_magnetisation(parameters, iteration)


plt.legend()
plt.xlabel("Time")
plt.ylabel("Magnetisation")
plt.xscale("log")
plt.xlim(0.05, 2.0)
plt.ylim(0.1, 1.5)
plt.savefig("Short_times.png")
plt.show()
