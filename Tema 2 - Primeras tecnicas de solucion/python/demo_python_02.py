from matplotlib import rc
import matplotlib.pylab as plt

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

x = plt.linspace(0,5)
plt.plot(x,plt.sin(x))
plt.ylabel(r"This is $\sin(x)$", size=20)
plt.show()