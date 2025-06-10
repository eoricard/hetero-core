import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, kv

# Definición de los coeficientes
a1 = 0.6961663
b1 = 0.06840432
a2 = 0.4079426
b2 = 0.11624142
a3 = 0.8974794
b3 = 9.8961612



#https://refractiveindex.info/?shelf=glass&book=fused_silica&page=Malitson
def n_fs(lamb):
    return np.sqrt(1+ (a1*lamb**2)/(lamb**2-b1**2) + (a2*lamb**2)/(lamb**2-b2**2)+(a3*lamb**2)/(lamb**2-b3**2))

def n1(lamb):
    return n_fs(lamb)

def n2(lamb):
    return 1.4  

def r1(r):
    return r

def k(lamb):
    return (2 * np.pi) / lamb

def q(lamb, h):
    return np.sqrt(k(lamb)**2 * (n1(lamb)**2 - n2(lamb)**2) - h**2)

def beta(lamb, h):
    return np.sqrt((n1(lamb) * k(lamb))**2 - h**2)

def a(nu, lamb, r, h):
    return ((1/2 * (jv(nu - 1, r1(r) * h) - jv(nu + 1, r1(r) * h))) /
            (r1(r) * h * jv(nu, r1(r) * h)) +
            (-kv(nu - 1, r1(r) * q(lamb, h)) - nu / (r1(r) * q(lamb, h)) *
             kv(nu, r1(r) * q(lamb, h))) /
            (r1(r) * q(lamb, h) * kv(nu, r1(r) * q(lamb, h))))

def b(nu, lamb, r, h):
    return ((n1(lamb)**2 * 1/2 * (jv(nu - 1, r1(r) * h) - jv(nu + 1, r1(r) * h))) /
            (r1(r) * h * jv(nu, r1(r) * h)) +
            (n2(lamb)**2 * (-kv(nu - 1, r1(r) * q(lamb, h)) - nu / (r1(r) * q(lamb, h)) *
                            kv(nu, r1(r) * q(lamb, h)))) /
            (r1(r) * q(lamb, h) * kv(nu, r1(r) * q(lamb, h))))

def c(nu, lamb, r, h):
    return (nu**2 * ((1 / (r1(r) * q(lamb, h)))**2 + (1 / (r1(r) * h))**2)**2 *
            (beta(lamb, h) / k(lamb))**2)

def d(nu, lamb, r, h):
    return a(nu, lamb, r, h) * b(nu, lamb, r, h) - c(nu, lamb, r, h)

# Gráfico
h_values = np.linspace(0.0815, .08256, 500)
h_values2 = np.linspace(0.01, .2, 500)
h_values3 = np.linspace(0.038, .039, 500)
fig1 = plt.figure("Filtro")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)


ax=fig1.add_subplot(2, 2, 2)
ax.plot(h_values3, d(1, 1.5, 62.5, h_values3), 'r-', h_values3, d(1, 1.2, 62.5, h_values3), 'g-', h_values3, d(1, .6, 62.5, h_values3), 'b-')
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)

ax=fig1.add_subplot(2, 2, 1)
ax.plot(h_values2, d(1, 1.5, 62.5, h_values2), 'r-', h_values2, d(1, 1.2, 62.5, h_values2), 'g-', h_values2, d(1, .6, 62.5, h_values2), 'b-')
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_ylim(-1, 1)

ax=fig1.add_subplot(2, 2, 4)
ax.plot(h_values, d(1, 1.5, 62.5, h_values), 'r-', h_values, d(1, 1.2, 62.5, h_values), 'g-', h_values, d(1, .6, 62.5, h_values), 'b-')
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)

ax=fig1.add_subplot(2, 2, 3)
ax.plot(h_values2, d(1, 1.5, 62.5, h_values2), 'r-', h_values2, d(1, 1.2, 62.5, h_values2), 'g-', h_values2, d(1, .6, 62.5, h_values2), 'b-')
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_ylim(-1, 1)

plt.show()
