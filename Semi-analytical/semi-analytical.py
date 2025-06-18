import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo CSV

dataframe = pd.read_csv('HE11_2d.csv', sep='\s+', engine='python')
dataframe2 = pd.read_csv('HE12_2d.csv', sep='\s+', engine='python')

c1=0.175061
c2=0.085634
c3=-0.10259

# Renombrar las columnas
dataframe.columns = ['Wavelength1', '1n1', '1n1p1', '1n1p2', '1n1p3', '1n1p4']
dataframe2.columns = ['Wavelength2', '2n1', '2n1p1', '2n1p2', '2n1p3', '2n1p4']

# Extraer columnas individuales para graficar
w1 = dataframe['Wavelength1']
n11 = dataframe['1n1']
n21 = dataframe['1n1p1']
n31 = dataframe['1n1p2']
n41 = dataframe['1n1p3']
n51 = dataframe['1n1p4']

w2 = dataframe2['Wavelength2']
n12 = dataframe2['2n1']
n22 = dataframe2['2n1p1']
n32 = dataframe2['2n1p2']
n42 = dataframe2['2n1p3']
n52 = dataframe2['2n1p4']


m1, b1 = np.polyfit(w1, n12-n11, 1)
m2, b2 = np.polyfit(w1, n22-n21, 1)
m3, b3 = np.polyfit(w1, n32-n31, 1)
m4, b4 = np.polyfit(w1, n42-n41, 1)
m5, b5 = np.polyfit(w1, n52-n51, 1)


print(2*np.pi/(m1*28000),2*np.pi/(m2*28000),2*np.pi/(m3*28000),2*np.pi/(m4*28000),2*np.pi/(m5*28000))
print(4*np.pi/(m1*28000),4*np.pi/(m2*28000),4*np.pi/(m3*28000),4*np.pi/(m4*28000),4*np.pi/(m5*28000))
fig1 = plt.figure("Filtro")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)


ax=fig1.add_subplot(2, 3, 1)
ax.plot(w1,np.sqrt(c1+c2+2*c3*np.cos((m1*w1+b1)*28000)),'r',w1,np.sqrt(c1+c2+2*c3*np.cos((m2*w1+b2)*28000)),'g',w1,np.sqrt(c1+c2+2*c3*np.cos((m3*w1+b3)*28000)),'b',w1,np.sqrt(c1+c2+2*c3*np.cos((m4*w1+b4)*28000)),'k',w1,np.sqrt(c1+c2+2*c3*np.cos((m5*w1+b5)*28000)),'m')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.6,1.7)
ax.set_ylim(.2, .8)

ax=fig1.add_subplot(2, 3, 2)
ax.plot(w1,np.sqrt(c1+c2+2*c3*np.cos((m1*w1+b1)*28000)),'r',w1,np.sqrt(c1+c2+2*c3*np.cos((m2*w1+b2)*28000)),'g',w1,np.sqrt(c1+c2+2*c3*np.cos((m3*w1+b3)*28000)),'b',w1,np.sqrt(c1+c2+2*c3*np.cos((m4*w1+b4)*28000)),'k',w1,np.sqrt(c1+c2+2*c3*np.cos((m5*w1+b5)*28000)),'m')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.7, .85)
ax.set_ylim(0.225, .325)


ax=fig1.add_subplot(2, 3, 3)
ax.plot(w1,np.sqrt(c1+c2+2*c3*np.cos((m1*w1+b1)*28000)),'r',w1,np.sqrt(c1+c2+2*c3*np.cos((m2*w1+b2)*28000)),'g',w1,np.sqrt(c1+c2+2*c3*np.cos((m3*w1+b3)*28000)),'b',w1,np.sqrt(c1+c2+2*c3*np.cos((m4*w1+b4)*28000)),'k',w1,np.sqrt(c1+c2+2*c3*np.cos((m5*w1+b5)*28000)),'m')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(1.5, 1.65)
ax.set_ylim(0.225, .325)

ax=fig1.add_subplot(2, 3, 5)
# Valores del eje x (índice de refracción) y del eje y (beta)
n_values = [1.0, 1.1, 1.2, 1.3, 1.4]
m_values = [-m1, -m2, -m3, -m4, -m5]
colors = ['r', 'g', 'b', 'k', 'm']

for n, m, c in zip(n_values, m_values, colors):
    beta = 2 * np.pi / (m * 28000)
    ax.plot(n, beta, color=c, marker='o')  # Usamos marcador para mostrar los puntos

# Etiquetas y ajustes del gráfico
ax.set_xlabel("Index of refraction n₃")
ax.set_ylabel("$L_{min,1}$")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.95, 1.45)
ax.set_ylim(.75, .81)

ax = fig1.add_subplot(2, 3, 6)

# Valores del eje x (índice de refracción) y del eje y (beta)
n_values = [1.0, 1.1, 1.2, 1.3, 1.4]
m_values = [-m1, -m2, -m3, -m4, -m5]
colors = ['r', 'g', 'b', 'k', 'm']

for n, m, c in zip(n_values, m_values, colors):
    beta = 4 * np.pi / (m * 28000)
    ax.plot(n, beta, color=c, marker='o')  # Usamos marcador para mostrar los puntos

# Etiquetas y ajustes del gráfico
ax.set_xlabel("Index of refraction n₃")
ax.set_ylabel("$L_{min,2}$")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.95, 1.45)
ax.set_ylim(1.54, 1.6)

plt.show()
