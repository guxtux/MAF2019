
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import roots_chebyt as raiz
import warnings
warnings.simplefilter('ignore', np.RankWarning)

def f(x):
    return (x*800)/(x**2 + 54*x**4 + 3)

def integrando(f,p):
    return (f - p)**2


x = np.linspace(-1,1)

n = 3
x1 = 2./(n-1)

x2 = np.arange(-1,1.1,x1)


p = np.poly1d(np.polyfit(x2, f(x2), n-1))

t = np.linspace(-1,1)

def p2(x):
    return p(x)**2

def f2(x):
    return f(x)**2

def dosveces(x):
    return 2*f(x)*p(x)

def p2C(x):
    return p_raices(x)**2

def dosveces(x):
    return 2*f(x)*p(x)

def dosvecesC(x):
    return 2*f(x)*p_raices(x)

raices = raiz(n)[0]
p_raices = np.poly1d(np.polyfit(raices, f(raices), n-1))

i1 = quad(f2,-1,1)[0]
i2 = quad(p2,-1,1)[0]
i3 = quad(dosveces,-1,1)[0]

i2C = quad(p2C,-1,1)[0]
i3C = quad(dosvecesC,-1,1)[0]


dist = 0
def distancia(x):
    for i in x:
        dist = np.max(np.abs(f(x) - p(x)))
        return dist

def distanciaC(x):
    for i in x:
        distC = np.max(np.abs(f(x) - p_raices(x)))
        return distC

norma = i1-i3+i2
diferencia = distancia(x)

normaC = i1-i3C+i2C
diferenciaC = distanciaC(x)

print('El error obtenido es: {0:.2f}'.format(norma))
print('La distancia máxima entre puntos es: {0:.2f}'.format(diferencia))

print('El error obtenido con raíces de Chebychev es: {0:.2f}'.format(normaC))
print('La distancia máxima entre puntos con raíces Chebychev es: {0:.2f}'.format(diferenciaC))

def plotbase():
    plt.plot(x, f(x), ls='dashed', lw=0.7)
    plt.xlim((-1,1))


plt.figure(1)
plotbase()
plt.plot(x2, f(x2), 'or')
plt.plot(t, p(t), color='k')

#plt.title('Función $f(x)$ a interpolar')
plt.title('Ajuste con un polinomio con '+ str(n) + ' puntos')
plt.text(-0.85,40,'El error es: ' + str(round(norma, 2)))
plt.text(-0.85,25,'El distancia máxima es: ' + str(round(diferencia, 2)))

plt.figure(2)
plotbase()
plt.plot(raices, f(raices), 'or')
plt.plot(t, p_raices(t), color='r')
plt.title('Ajuste con las raíces de $T_{n}$')
plt.text(-0.85,40,'El error es: ' + str(round(normaC, 2)))
plt.text(-0.85,25,'El distancia máxima es: ' + str(round(diferenciaC, 2)))

plt.show()