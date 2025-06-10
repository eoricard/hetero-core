import numpy as np
from scipy.special import jv, kv
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import time
inicio = time.time()
# Define constants
c = [0.0684043, 0.1162414, 9.896161]
d = [0.6961663, 0.4079426, 0.8974794]

# Load data
csvH1 = pd.read_csv('dispersionHE11.csv', sep=',')
dataframeH1 = pd.DataFrame(csvH1)
dataframeH1.columns = ['WavelengthH1', 'BetaH1']
lamb = dataframeH1["WavelengthH1"]
betaH1 = dataframeH1["BetaH1"]
csvH2 = pd.read_csv('dispersionHE12.csv', sep=',')
dataframeH2 = pd.DataFrame(csvH2)
dataframeH2.columns = ['WavelengthH2', 'BetaH2']
lamb = dataframeH2["WavelengthH2"]
betaH2 = dataframeH2["BetaH2"]

Inter = np.zeros(1100, float)
Lambda = np.zeros(1100, float)
for i in range(0, 1100,20):
   lambda_ = lamb.iloc[i]  # primer valor
   beta_H1 = betaH1.iloc[i]
   beta_H2 = betaH2.iloc[i]



   # Define functions
   def n1(lambda_):
    return np.sqrt(n2(lambda_)**2 + 0.275)
   def n2(lambda_):
    return np.sqrt(1 + sum((d[i] * lambda_**2) / (lambda_**2 - c[i]**2) for i in range(3)))
   def n3(lambda_):
    return 1
   def k(lambda_):
    return 2 * np.pi / lambda_

   def P_H1(lambda_):
    return np.sqrt((n2(lambda_) * k(lambda_))**2 - beta_H1**2)

   def Q_H1(lambda_):
    return np.sqrt(beta_H1**2 - (n3(lambda_)*k(lambda_))**2)

   def P_H2(lambda_):
    return np.sqrt((n2(lambda_) * k(lambda_))**2 - beta_H2**2)

   def Q_H2(lambda_):
    return np.sqrt(beta_H2**2 - (n3(lambda_)*k(lambda_))**2)

   def r(x, y):
    return np.sqrt(x**2 + y**2)

   def Psi_H1(x, y, z, lambda_):
      radius = r(x, y)
      PH1 = P_H1(lambda_)
      QH1 = Q_H1(lambda_)
      core_radius = 62.5  # μm

      if radius < core_radius:
        return (jv(0, PH1 * radius) / jv(0, PH1 * core_radius)) * np.exp(1j * beta_H1 * z)
      else:
        return (kv(0, QH1 * radius) / kv(0, QH1 * core_radius)) * np.exp(1j * beta_H1 * z)
    
   def Psi_H2(x, y, z, lambda_):
       radius = r(x, y)
       PH2 = P_H2(lambda_)
       QH2 = Q_H2(lambda_)
       core_cladding = 62.5  # μm

       if radius < core_cladding:
         return (jv(0, PH2 * radius) / jv(0, PH2 * core_cladding)) * np.exp(1j * beta_H2 * z)
       else:
        return (kv(0, QH2 * radius) / kv(0, QH2 * core_cladding)) * np.exp(1j * beta_H2 * z)

   # Vectorizar la función para aplicar en malla
   Psi_H1_vectorized = np.vectorize(Psi_H1, otypes=[np.complex128])
   Psi_H2_vectorized = np.vectorize(Psi_H2, otypes=[np.complex128])
   # Definir la malla
   x_vals = np.linspace(-75, 75, 200)
   y_vals = np.linspace(-75, 75, 200)
   X, Y = np.meshgrid(x_vals, y_vals)
   dx = x_vals[1] - x_vals[0]
   dy = y_vals[1] - y_vals[0]
   
   def Integral(X, Y, Z, lambda_):
        field_H1 = Psi_H1_vectorized(X, Y, Z, lambda_)
        field_H2 = Psi_H2_vectorized(X, Y, Z, lambda_)
        density_HE1 = np.abs(field_H1)
        density_HE2 = np.abs(field_H2)
        integralH1 = np.sum(density_HE1) * dx * dy
        integralH2 = np.sum(density_HE2) * dx * dy

        # Crear máscara para dentro del núcleo
        radius_matrix = r(X, Y)
        mask = radius_matrix < 32.5

        # Campo combinado dentro del núcleo
        combined_field = np.zeros_like(field_H1, dtype=np.complex128)
        combined_field[mask] = (field_H1[mask] / integralH1) + (field_H2[mask] / integralH2)

        return combined_field
   result = Integral(X, Y, 7000, lambda_)
   Inter[i] = np.sum(np.abs(result)) * dx * dy
   Lambda[i]=lambda_
fin = time.time()
print(fin-inicio) 
plt.plot(Lambda[:1100],Inter[:1100],'o')     # Muestra primeros dos valores
plt.axis((.6, 1.7, 0, 1))
plt.title("A_1=A_2=1,L=7mm")
plt.xlabel("Wavelength")
plt.ylabel("I")
plt.grid()
plt.show()