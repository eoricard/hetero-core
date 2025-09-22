import numpy as np
from scipy.special import jv, kv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
from scipy.interpolate import interp1d

def plot_propagation(H1,H2, wavelength,lim,L,fig_name):

 filepathL = f"data/beta_HE1{H1}.csv"
 dataframeL = pd.read_csv(filepathL, sep=',', engine='python')
 # Load data
 dataframeL.columns = ['col1', 'col2']
 lambL = dataframeL["col1"]
 bH1 = dataframeL["col2"]
 bH2 = interp1d(lambL, bH1, kind='linear')
 BetaH1 = bH2(wavelength)

 filepathH = f"data/beta_HE1{H2}.csv"
 dataframeH = pd.read_csv(filepathH, sep=',', engine='python')
 dataframeH.columns = ['col3', 'col4']
 lambH = dataframeH["col3"]
 betaH1 = dataframeH['col4']
 betaH2 = interp1d(lambH, betaH1, kind='linear')
 BetaH2 = betaH2(wavelength)

 
 c = [0.0684043, 0.1162414, 9.896161]
 d = [0.6961663, 0.4079426, 0.8974794]
 n3=1
 def n1(wavelength):
    return np.sqrt(n2(wavelength)**2 + 0.275)
 def n2(wavelength):
    return np.sqrt(1 + sum((d[i] * wavelength**2) / (wavelength**2 - c[i]**2) for i in range(3)))

 def k(wavelength):
    return 2 * np.pi / wavelength

 def P_H1(wavelength):
    return np.sqrt((n2(wavelength) * k(wavelength))**2 - BetaH1**2)

 def Q_H1(wavelength):
    return np.sqrt(BetaH1**2 - (n3*k(wavelength))**2)

 def P_H2(wavelength):
    return np.sqrt((n2(wavelength) * k(wavelength))**2 - BetaH2**2)

 def Q_H2(wavelength):
    return np.sqrt(BetaH2**2 - (n3*k(wavelength))**2)

 def r(x, y):
    return np.sqrt(x**2 + y**2)

 def Psi_H1(x, y, z, wavelength):
    radius = r(x, y)
    PH1 = P_H1(wavelength)
    QH1 = Q_H1(wavelength)
    core_radius = 62.5  # μm

    if radius < core_radius:
        return (jv(0, PH1 * radius) / jv(0, PH1 * core_radius)) * np.exp(1j * BetaH1*z)
    else:
        return (kv(0, QH1 * radius) / kv(0, QH1 * core_radius)) * np.exp(1j * BetaH1*z)
    

 def Psi_H2(x, y, z, wavelength):
    radius = r(x, y)
    PH2 = P_H2(wavelength)
    QH2 = Q_H2(wavelength)
    core_cladding = 62.5  # μm

    if radius < core_cladding:
        return (jv(0, PH2 * radius) / jv(0, PH2 * core_cladding)) * np.exp(1j * BetaH2*z)
    else:
        return (kv(0, QH2 * radius) / kv(0, QH2 * core_cladding)) * np.exp(1j * BetaH2*z)

 # Vectorizar la función para aplicar en malla
 Psi_H1_vectorized = np.vectorize(Psi_H1, otypes=[np.complex128])
 Psi_H2_vectorized = np.vectorize(Psi_H2, otypes=[np.complex128])
 # Definir la malla
 x_vals = np.linspace(-lim, lim, 200)
 y_vals = np.linspace(-lim, lim, 200)
 z_vals = np.linspace(0, L, 300)
 X, Y = np.meshgrid(x_vals, y_vals)

 # Calcular campo
 field_H1 = Psi_H1_vectorized(X, Y, L, wavelength)
 field_H2 = Psi_H2_vectorized(X, Y, L, wavelength)
 Z, X2 = np.meshgrid(z_vals, x_vals)

 # Calcular densidad
 density_HE1=np.abs(field_H1)
 density_HE2=np.abs(field_H2)
 dx = x_vals[1] - x_vals[0]
 dy = y_vals[1] - y_vals[0]
 integralH1 = np.sum(density_HE1) * dx * dy
 integralH2 = np.sum(density_HE2)* dx * dy
 density_total = np.abs(field_H1/integralH1+field_H2/integralH2)
 fieldz = Psi_H1_vectorized(X2, 1 , Z , wavelength)/integralH1 + Psi_H2_vectorized(X2, 1 , Z , wavelength)/integralH2
 density_totalz=np.abs(fieldz)
 dx = x_vals[1] - x_vals[0]
 dy = y_vals[1] - y_vals[0]

 
 # Primera figura: plano XY
 fig1 = plt.figure(fig_name)
 fig1.suptitle(fig_name)

 plt.pcolormesh(X, Y, density_total, cmap="viridis", shading='auto')
 plt.colorbar(label="Density")
 plt.xlabel("x [μm]", fontsize=14) 
 plt.ylabel("y [μm]", fontsize=14)
 plt.title(r"$E_{II}(z=" + str(L) + r"\, [\mu m])$", fontsize=16)
 plt.tight_layout()

 # Segunda figura: plano ZY (o ZX dependiendo de tus ejes)
 fig2 = plt.figure(figsize=(6, 6))

 plt.pcolormesh(Z, X2, density_totalz, cmap="viridis", shading='auto')
 plt.colorbar(label="Density")
 plt.xlabel("z [μm]", fontsize=14)
 plt.ylabel("y [μm]", fontsize=14)
 plt.title(r"$E_{II}(z,y)$", fontsize=16)
 plt.tight_layout()
 
 return fig1

