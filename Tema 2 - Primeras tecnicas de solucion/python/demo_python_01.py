import numpy as np
import matplotlib.pyplot as plt
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


# Example data
t = np.arange(0.0, 1.0 + 0.01, 0.01)
s = np.cos(4 * np.pi * t) + 2
def secuencia01(n, x):
    phi_nx = n/np.pi * (1 / (1 + (n**2 * x**2)))
    return phi_nx

n = 1

x = np.linspace(-10, 10, 200)




#plt.plot(t, s)
for i in [1,2,3]:
    plt.plot(x, secuencia01(i, x), label="n = " + str(i))

#plt.xlabel(r'\textbf{time} (s)')
#plt.ylabel(r'\textit{voltage} (mV)',fontsize=16)
plt.title(r"Secuencia delta $\phi_{n}(x)$", fontsize=16)
plt.text(-9.75,0.5,r"$\phi_{n} = \dfrac{n}{\pi} \, \dfrac{1}{(1 + x^{2}) \, n^{2}}$", fontsize=16)
plt.legend(loc=1)
# Make room for the ridiculously large title.
#plt.subplots_adjust(top=0.8)

#plt.savefig('tex_demo')
plt.show()