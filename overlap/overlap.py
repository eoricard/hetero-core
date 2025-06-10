import numpy as np
from scipy.special import jv, kv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
# Define constants
c = [0.0684043, 0.1162414, 9.896161]
d = [0.6961663, 0.4079426, 0.8974794]

# Load data
csvL = pd.read_csv('dispersion_Lp01.csv', sep=',')
dataframeL = pd.DataFrame(csvL)
dataframeL.columns = ['WavelengthL', 'BetaL']
lamb = dataframeL["WavelengthL"]
betaL = dataframeL["BetaL"]
lambda_ = lamb.iloc[0]  # primer valor
beta_L = betaL.iloc[0]

csvH = pd.read_csv('dispersionHE11.csv', sep=',')
dataframeH = pd.DataFrame(csvH)
dataframeH.columns = ['WavelengthH', 'BetaH']
lamb = dataframeH["WavelengthH"]
betaH = dataframeH["BetaH"]
beta_H = betaH.iloc[0]

# Define functions
def n1(lambda_):
    return np.sqrt(n2(lambda_)**2 + 0.275)
def n2(lambda_):
    return np.sqrt(1 + sum((d[i] * lambda_**2) / (lambda_**2 - c[i]**2) for i in range(3)))
def n3(lambda_):
    return 1
def k(lambda_):
    return 2 * np.pi / lambda_

def P_L(lambda_):
    return np.sqrt((n1(lambda_) * k(lambda_))**2 - beta_L**2)

def Q_L(lambda_):
    return np.sqrt(beta_L**2 - (n2(lambda_)*k(lambda_))**2)

def P_H(lambda_):
    return np.sqrt((n2(lambda_) * k(lambda_))**2 - beta_H**2)

def Q_H(lambda_):
    return np.sqrt(beta_H**2 - (n3(lambda_)*k(lambda_))**2)

def r(x, y):
    return np.sqrt(x**2 + y**2)

def Psi_L(x, y, z, lambda_):
    radius = r(x, y)
    PL = P_L(lambda_)
    QL = Q_L(lambda_)
    core_radius = 31.25  # μm

    if radius < core_radius:
        return (jv(0, PL * radius) / jv(0, PL * core_radius)) * np.exp(1j * beta_L * z)
    else:
        return (kv(0, QL * radius) / kv(0, QL * core_radius)) * np.exp(1j * beta_L * z)
    

def Psi_H(x, y, z, lambda_):
    radius = r(x, y)
    PH = P_H(lambda_)
    QH = Q_H(lambda_)
    core_cladding = 62.5  # μm

    if radius < core_cladding:
        return (jv(0, PH * radius) / jv(0, PH * core_cladding)) * np.exp(1j * beta_H * z)
    else:
        return (kv(0, QH * radius) / kv(0, QH * core_cladding)) * np.exp(1j * beta_H * z)

# Vectorizar la función para aplicar en malla
Psi_L_vectorized = np.vectorize(Psi_L, otypes=[np.complex128])
Psi_H_vectorized = np.vectorize(Psi_H, otypes=[np.complex128])
# Definir la malla
x_vals = np.linspace(-75, 75, 200)
y_vals = np.linspace(-75, 75, 200)
X, Y = np.meshgrid(x_vals, y_vals)

# Calcular campo
field_L = Psi_L_vectorized(X, Y, 1, lambda_)
field_H = Psi_H_vectorized(X, Y, 1, lambda_)

# Calcular densidad
density_L = np.abs(field_L)
density_H = np.abs(field_H)
density_LH = np.abs(field_L * np.conjugate(field_H))
dx = x_vals[1] - x_vals[0]
dy = y_vals[1] - y_vals[0]
integralLH = np.abs(np.sum(field_L * np.conjugate(field_H)) * dx * dy)
integralL = np.sum(np.abs(field_L * np.conjugate(field_L))) * dx * dy
integralH = np.sum(np.abs(field_H * np.conjugate(field_H)))* dx * dy

overlap=((integralLH)**2)/(integralL*integralH)
print(overlap)
print(integralL)
print(integralH)
#pd.DataFrame(density/np.sqrt(integral)).to_csv("mode_LP04_com.csv", index=False)
#pd.DataFrame(field/np.sqrt(integral)).to_csv("mode_LP04_com.csv", index=False)
# Graficar
plt.figure(figsize=(6, 6))
plt.pcolormesh(X, Y, density_L/np.sqrt(integralL), cmap="viridis", shading='auto')
plt.colorbar(label="Density")
plt.xlabel("x [μm]", fontsize=14)
plt.ylabel("y [μm]", fontsize=14)
plt.title("$M_{01}f_{01}(x,y)\ \ LP_{01}$", fontsize=16)
plt.axis('equal')
plt.tight_layout()

plt.figure(figsize=(6, 6))
plt.pcolormesh(X, Y, density_H/np.sqrt(integralH), cmap="viridis", shading='auto')
plt.colorbar(label="Density")
plt.xlabel("x [μm]", fontsize=14)
plt.ylabel("y [μm]", fontsize=14)
plt.title("$M_{11}f_{11}(x,y)\ \ HE_{11}$", fontsize=16)
plt.axis('equal')
plt.tight_layout()


plt.figure(figsize=(6, 6))
plt.pcolormesh(X, Y, density_LH/(np.sqrt(integralH)*np.sqrt(integralL)), cmap="viridis", shading='auto')
plt.colorbar(label="Density")
plt.xlabel("x [μm]", fontsize=14)
plt.ylabel("y [μm]", fontsize=14)
plt.title("$n_{11}=0.5154$", fontsize=16)
plt.axis('equal')
plt.tight_layout()

plt.show()
