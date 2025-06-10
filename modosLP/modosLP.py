import numpy as np
from scipy.special import jv, kv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
# Define constants
c = [0.0684043, 0.1162414, 9.896161]
d = [0.6961663, 0.4079426, 0.8974794]

# Load data
csv = pd.read_csv('dispersion_Lp04.csv', sep=',')
dataframe = pd.DataFrame(csv)
dataframe.columns = ['Wavelength', 'Beta']
lamb = dataframe["Wavelength"]
beta = dataframe["Beta"]
lambda_ = lamb.iloc[0]  # primer valor
beta_HE11o = beta.iloc[0]
order=1
print(lambda_)
# Define functions
def n2(lambda_):
    return np.sqrt(1 + sum((d[i] * lambda_**2) / (lambda_**2 - c[i]**2) for i in range(3)))
def n1(lambda_):
    return np.sqrt(n2(lambda_)**2 + 0.275)
def k(lambda_):
    return 2 * np.pi / lambda_

def P_01(lambda_):
    return np.sqrt((n1(lambda_) * k(lambda_))**2 - beta_HE11o**2)

def Q_01(lambda_):
    return np.sqrt(beta_HE11o**2 - (n2(lambda_)*k(lambda_))**2)

def r(x, y):
    return np.sqrt(x**2 + y**2)

def Psi_11(x, y, z, lambda_):
    radius = r(x, y)
    P = P_01(lambda_)
    Q = Q_01(lambda_)
    core_radius = 31.25  # μm

    if radius < core_radius:
        return (jv(0, P * radius) / jv(0, P * core_radius)) * np.exp(1j * beta_HE11o * z)
    else:
        return (kv(0, Q * radius) / kv(0, Q * core_radius)) * np.exp(1j * beta_HE11o * z)

# Vectorizar la función para aplicar en malla
Psi_11_vectorized = np.vectorize(Psi_11, otypes=[np.complex128])

# Definir la malla
x_vals = np.linspace(-75, 75, 200)
y_vals = np.linspace(-75, 75, 200)
X, Y = np.meshgrid(x_vals, y_vals)

# Calcular campo
field = Psi_11_vectorized(X, Y, 1, lambda_)

# Calcular densidad
density = np.abs(field)
dx = x_vals[1] - x_vals[0]
dy = y_vals[1] - y_vals[0]
integral = np.sum(density) * dx * dy
pd.DataFrame(density/np.sqrt(integral)).to_csv("mode_LP04_com.csv", index=False)
pd.DataFrame(field/np.sqrt(integral)).to_csv("mode_LP04_com.csv", index=False)
# Graficar
plt.figure(figsize=(6, 6))
plt.pcolormesh(X, Y, density/np.sqrt(integral), cmap="viridis", shading='auto')
plt.colorbar(label="Density")
plt.xlabel("x [μm]", fontsize=14)
plt.ylabel("y [μm]", fontsize=14)
plt.title("$M_{04}f_{04}(x,y)\ \ LP_{04}$", fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()
