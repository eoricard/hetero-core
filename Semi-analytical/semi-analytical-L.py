import numpy as np
import matplotlib.pyplot as plt

# Constantes
c1 = 0.175061
c2 = 0.085634
c3 = -0.10259
m1 = 0.00029002955514556263
b1 = -1.8133393933132395e-06  # Notación científica

# Definición de la función Inter
def Inter(lam, L):
    return np.sqrt(c1 + c2 + 2 * c3 * np.cos((m1 * lam + b1) * L))

# Rango de valores
lambda_vals = np.linspace(0.6, 1.7, 300)
L_vals = np.linspace(0, 60000, 300)
Lambda, L = np.meshgrid(lambda_vals, L_vals)

# Evaluar la función sobre la malla
Z = Inter(Lambda, L)

# Crear el gráfico tipo DensityPlot
plt.figure(figsize=(8, 6))
plt.contourf(lambda_vals, L_vals, Z, levels=100, cmap='viridis')
plt.colorbar(label='I(λ, L)')
plt.xlabel('λ')
plt.ylabel('L')
plt.title('DensityPlot de I(λ, L)')
plt.show()
