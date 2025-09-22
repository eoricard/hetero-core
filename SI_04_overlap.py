import numpy as np
from scipy.special import jv, kv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.interpolate import interp1d

# Define constants

def calculate_overlap(P,H, wavelength,lim, fig_name):

 filepathL = f"data/beta_LP0{P}.csv"
 dataframeL = pd.read_csv(filepathL, sep=',', engine='python')
 # Load data
 dataframeL.columns = ['col1', 'col2']
 lambL = dataframeL["col1"]
 betaL1 = dataframeL["col2"]
 betaL2 = interp1d(lambL, betaL1, kind='linear')
 BetaL = betaL2(wavelength)

 filepathH = f"data/beta_HE1{H}.csv"
 dataframeH = pd.read_csv(filepathH, sep=',', engine='python')
 dataframeH.columns = ['col3', 'col4']
 lambH = dataframeH["col3"]
 betaH1 = dataframeH['col4']
 betaH2 = interp1d(lambH, betaH1, kind='linear')
 BetaH = betaH2(wavelength)

 
 c = [0.0684043, 0.1162414, 9.896161]
 d = [0.6961663, 0.4079426, 0.8974794]
 n3=1
 # Define functions
 def n1(wavelength):
    return np.sqrt(n2(wavelength)**2 + 0.275)
 def n2(wavelength):
    return np.sqrt(1 + sum((d[i] * wavelength**2) / (wavelength**2 - c[i]**2) for i in range(3)))
 
 def k(wavelength):
    return 2 * np.pi / wavelength

 def P_L(wavelength):
    return np.sqrt((n1(wavelength) * k(wavelength))**2 - BetaL**2)

 def Q_L(wavelength):
    return np.sqrt(BetaL**2 - (n2(wavelength)*k(wavelength))**2)

 def P_H(wavelength):
    return np.sqrt((n2(wavelength) * k(wavelength))**2 - BetaH**2)

 def Q_H(wavelength):
    return np.sqrt(BetaH**2 - (n3*k(wavelength))**2)

 def r(x, y):
    return np.sqrt(x**2 + y**2)

 def Psi_L(x, y, z, wavelength):
    radius = r(x, y)
    PL = P_L(wavelength)
    QL = Q_L(wavelength)
    core_radius = 31.25  # μm

    if radius < core_radius:
        return (jv(0, PL * radius) / jv(0, PL * core_radius)) * np.exp(1j * BetaL * z)
    else:
        return (kv(0, QL * radius) / kv(0, QL * core_radius)) * np.exp(1j * BetaL * z)
    

 def Psi_H(x, y, z, wavelength):
    radius = r(x, y)
    PH = P_H(wavelength)
    QH = Q_H(wavelength)
    core_cladding = 62.5  # μm

    if radius < core_cladding:
        return (jv(0, PH * radius) / jv(0, PH * core_cladding)) * np.exp(1j * BetaH * z)
    else:
        return (kv(0, QH * radius) / kv(0, QH * core_cladding)) * np.exp(1j * BetaH * z)

 # Vectorizar la función para aplicar en malla
 Psi_L_vectorized = np.vectorize(Psi_L, otypes=[np.complex128])
 Psi_H_vectorized = np.vectorize(Psi_H, otypes=[np.complex128])
 # Definir la malla
 x_vals = np.linspace(-lim, lim, 200)
 y_vals = np.linspace(-lim, lim, 200)
 X, Y = np.meshgrid(x_vals, y_vals)

 # Calcular campo
 field_L = Psi_L_vectorized(X, Y, 1, wavelength)
 field_H = Psi_H_vectorized(X, Y, 1, wavelength)

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
 #pd.DataFrame(density/np.sqrt(integral)).to_csv("mode_LP04_com.csv", index=False)
 #pd.DataFrame(field/np.sqrt(integral)).to_csv("mode_LP04_com.csv", index=False)
 # Graficar
 # Plotting
 fig1 = plt.figure(fig_name)
 fig1.suptitle(fig_name)

 # Subplot 1: LP0P
 ax1 = fig1.add_subplot(1,3,1)
 pcm1 = ax1.pcolormesh(X, Y, density_L / np.sqrt(integralL), cmap="viridis", shading='auto')
 fig1.colorbar(pcm1, ax=ax1, label="Density")
 ax1.set_xlabel("x [μm]", fontsize=14)
 ax1.set_ylabel("y [μm]", fontsize=14)
 ax1.set_title(f"LP0{P}", fontsize=16)


 # Subplot 2: HE1H
 ax2 = fig1.add_subplot(1,3,2)
 pcm2 = ax2.pcolormesh(X, Y, density_H / np.sqrt(integralH), cmap="viridis", shading='auto')
 fig1.colorbar(pcm2, ax=ax2, label="Density")
 ax2.set_xlabel("x [μm]", fontsize=14)
 ax2.set_ylabel("y [μm]", fontsize=14)
 ax2.set_title(f"HE1{H}", fontsize=16)

 # Subplot 3: overlap
 ax3 = fig1.add_subplot(1,3,3)
 pcm3 = ax3.pcolormesh(X, Y, density_LH / (np.sqrt(integralH) * np.sqrt(integralL)), cmap="viridis", shading='auto')
 fig1.colorbar(pcm3, ax=ax3, label="Density")
 ax3.set_xlabel("x [μm]", fontsize=14)
 ax3.set_ylabel("y [μm]", fontsize=14)
 ax3.set_title(f"n{P}{H} = {overlap:.4f}", fontsize=16)

 return fig1

