#Script to graph the characteristic equation as a function of the refractive index n3 and the radius of the heterocore fiber r2
#plot_characteristic(n3,r2,"Figure1") 

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, kv

# Coeficients for fused silica 
#https://refractiveindex.info/?shelf=glass&book=fused_silica&page=Malitson

a1 = 0.6961663
b1 = 0.06840432
a2 = 0.4079426
b2 = 0.11624142
a3 = 0.8974794
b3 = 9.8961612

# sellmeier for fused silica
def n_fs(lamb):
    return np.sqrt(1 + (a1 * lamb**2) / (lamb**2 - b1**2) + 
                   (a2 * lamb**2) / (lamb**2 - b2**2) + 
                   (a3 * lamb**2) / (lamb**2 - b3**2))
# refracction index for coreless fiber 
def n1(lamb):
    return n_fs(lamb)

def k(lamb):
    return (2 * np.pi) / lamb

def q(lamb,n3, h):
    return np.sqrt(k(lamb)**2 * (n1(lamb)**2 - n3**2) - h**2)

def beta(lamb, h):
    return np.sqrt((n1(lamb) * k(lamb))**2 - h**2)


# Definition of funtions  a, b, c, d
def a(nu, lamb,n3, r2, h):
    return ((1/2 * (jv(nu - 1, r2 * h) - jv(nu + 1, r2 * h))) /
            (r2 * h * jv(nu, r2 * h)) +
            (-kv(nu - 1, r2 * q(lamb,n3, h)) - nu / (r2 * q(lamb,n3, h)) *
             kv(nu, r2 * q(lamb,n3, h))) /
            (r2 * q(lamb,n3, h) * kv(nu, r2 * q(lamb,n3, h))))

def b(nu, lamb,n3, r2, h):
    return ((n1(lamb)**2 * 1/2 * (jv(nu - 1, r2 * h) - jv(nu + 1, r2 * h))) /
            (r2 * h * jv(nu, r2 * h)) +
            (n3**2 * (-kv(nu - 1, r2 * q(lamb,n3, h)) - nu / (r2 * q(lamb,n3, h)) *
                            kv(nu, r2 * q(lamb,n3, h)))) /
            (r2 * q(lamb,n3, h) * kv(nu, r2 * q(lamb,n3, h))))

def c(nu, lamb,n3, r2, h):
    return (nu**2 * ((1 / (r2 * q(lamb,n3, h)))**2 + (1 / (r2 * h))**2)**2 *
            (beta(lamb, h) / k(lamb))**2)

def d(nu, lamb,n3, r2, h):
    return a(nu, lamb,n3, r2, h) * b(nu, lamb,n3, r2, h) - c(nu, lamb,n3, r2, h)

# plot function
def plot_characteristic(n3, r2,fig_name="Figure1"):
    # ranges 
    range1 = np.linspace(0.0815, 0.08256, 500)
    range2 = np.linspace(0.01, 0.2, 500)
    range3 = np.linspace(0.038, 0.039, 500)

    # Crear la figura con subgráficos
    fig1 = plt.figure(fig_name) 
    fig1.subplots_adjust(hspace=0.5, wspace=0.5)

    # Primer subgráfico
    ax = fig1.add_subplot(2, 2, 3)
    ax.plot(range3, d(1, 0.6 , n3, r2, range3), 'r-', 
            range3, d(1, 1.2 , n3, r2, range3), 'g-', 
            range3, d(1, 1.5, n3, r2, range3), 'b-')
    ax.set_xlabel("h")
    ax.set_ylabel("RE-LE")
    ax.set_title(fr"$n_3 = {n3}$")
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
    ax.axhline(0, color='black', linewidth=0.5)

    # Segundo subgráfico
    ax = fig1.add_subplot(2, 2, 1)
    ax.plot(range2, d(1, 0.6, n3, r2, range2), 'r-', 
            range2, d(1, 1.2, n3, r2, range2), 'g-', 
            range2, d(1, 1.5, n3, r2, range2), 'b-')
    ax.set_xlabel("h")
    ax.set_ylabel("RE-LE")
    ax.set_title(fr"$n_3 = {n3}$")
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_ylim(-1, 1)

    # Tercer subgráfico
    ax = fig1.add_subplot(2, 2, 4)
    ax.plot(range1, d(1, 0.6 , n3, r2, range1), 'r-', 
            range1, d(1, 1.2, n3, r2, range1), 'g-', 
            range1, d(1, 1.5, n3, r2, range1), 'b-')
    ax.set_xlabel("h")
    ax.set_ylabel("RE-LE")
    ax.set_title(fr"$n_3 = {n3}$")
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
    ax.axhline(0, color='black', linewidth=0.5)

    # Cuarto subgráfico
    ax = fig1.add_subplot(2, 2, 2)
    ax.plot(range2, d(1, 0.6, n3, r2, range2), 'r-', 
            range2, d(1, 1.2, n3, r2, range2), 'g-', 
            range2, d(1, 1.5, n3, r2, range2), 'b-')
    ax.set_xlabel("h")
    ax.set_ylabel("RE-LE")
    ax.set_title(fr"$n_3 = {n3}$")
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.set_ylim(-1, 1)
    return fig1


