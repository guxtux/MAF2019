import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import roots_chebyt as raiz
import warnings
warnings.simplefilter('ignore', np.RankWarning)

def f(x):
    return (x*800)/(x**2 + 54*x**4 + 3)

<<<<<<< HEAD
def puntos_equidistantes(n):
    x1 = 2./(n-1)
    x2 = np.arange(-1, 1.1, x1)
    return x2

def puntos_raices(n):
    raices = raiz(n)[0]
    return raices

def generapolinomio(puntos, grado):
    p = np.poly1d(np.polyfit(puntos, f(puntos), grado-1))
    return p

def integracion(x, p):
    def i1(x):
        return f(x)**2
    
    def i2(x):
        return p(x)**2

    def i3(x):
        return 2*f(x)*p(x)
    
    def evalua_int(g):
        valor = quad(g, -1, 1)[0]
        return valor
    
    norma = evalua_int(i1) + evalua_int(i2) - evalua_int(i3)
    return norma
    
def distancia(f, p):
    dist = 0
=======
def integrando(f,p):
    return (f - p)**2


x = np.linspace(-1,1)

n = 10
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
>>>>>>> master
    for i in x:
        dist = np.max(np.abs(f - p))
    
    return dist

def plotbase():
    plt.plot(x, f(x), ls='dashed', lw=0.7)
    plt.xlim((-1,1))

def plotpuntos(xpuntos, f_xpuntos, p):
    plt.plot(xpuntos, f_xpuntos, 'or')
    plt.plot(x, p, color='k')

def mensaje(tipo, D1, D2):
    if tipo == 1:
        print('El error obtenido con puntos equidistantes es: {0:.2f}'.format(D1))
    else:
        print('-'*40)
        print('El error obtenido con raíces de Chebychev es: {0:.2f}'.format(D1))
    
    print('La distancia máxima entre puntos es: {0:.2f}'.format(D2))

def puntosespaciados():
    npuntos = puntos_equidistantes(n)
    polinomio = generapolinomio(npuntos, n)
    val_integracion = integracion(x, polinomio)
    diferencia = distancia(f(x), polinomio(x))
    mensaje(1, val_integracion, diferencia)
    grafica(1, npuntos, polinomio(x), val_integracion, diferencia)

def puntosChebychev():
    npuntos = puntos_raices(n)
    polinomio = generapolinomio(npuntos, n)
    val_integracion = integracion(x, polinomio)
    diferencia = distancia(f(x), polinomio(x))
    mensaje(2, val_integracion, diferencia)
    grafica(2, npuntos, polinomio(x), val_integracion, diferencia)

def grafica(a, npuntos, p, D1, D2):
    plt.figure(a)
    plotbase()
    plotpuntos(npuntos, f(npuntos), p)
    if a == 1:
        plt.title('Ajuste con un polinomio con '+ str(n) + ' puntos equidistantes')
    else:
        plt.title('Ajuste con las raíces de $T_{n}$')
    plt.text(-0.85,40,'El error es: ' + str(round(D1, 2)))
    plt.text(-0.85,25,'El distancia máxima es: ' + str(round(D2, 2)))


<<<<<<< HEAD
x = np.linspace(-1,1)
n = 10
=======
plt.figure(2)
plotbase()
plt.plot(raices, f(raices), 'or')
plt.plot(t, p_raices(t), color='g')
plt.title('Ajuste con las raíces de $T_{n}$')
plt.text(-0.85,40,'El error es: ' + str(round(normaC, 2)))
plt.text(-0.85,25,'El distancia máxima es: ' + str(round(diferenciaC, 2)))
>>>>>>> master

puntosespaciados()
puntosChebychev()
plt.show()