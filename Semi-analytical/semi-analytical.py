import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Leer el archivo CSV

dataframe = pd.read_csv('HE11_2d.csv', sep='\s+', engine='python')
dataframe2 = pd.read_csv('HE12_2d.csv', sep='\s+', engine='python')



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
m2, b2 = np.polyfit(w1, n21-n22, 1)
m3, b3 = np.polyfit(w1, n31-n32, 1)
m4, b4 = np.polyfit(w1, n41-n42, 1)
m5, b5 = np.polyfit(w1, n51-n52, 1)

fig1 = plt.figure("Filtro")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)


ax=fig1.add_subplot(1, 3, 1)
ax.plot(w1,2-2*np.cos((m1*w1+b1)*28000),'r',w1,2-2*np.cos((m2*w1+b2)*28000),'g',w1,2-2*np.cos((m3*w1+b3)*28000),'b',w1,2-2*np.cos((m4*w1+b4)*28000),'k',w1,2-2*np.cos((m5*w1+b5)*28000),'m')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.6,1.7)
ax.set_ylim(0, 4)

ax=fig1.add_subplot(1, 3, 2)
ax.plot(w1,2-2*np.cos((m1*w1+b1)*28000),'r',w1,2-2*np.cos((m2*w1+b2)*28000),'g',w1,2-2*np.cos((m3*w1+b3)*28000),'b',w1,2-2*np.cos((m4*w1+b4)*28000),'k',w1,2-2*np.cos((m5*w1+b5)*28000),'m')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.7, .85)
ax.set_ylim(0, .25)


ax=fig1.add_subplot(1, 3, 3)
ax.plot(w1,2-2*np.cos((m1*w1+b1)*28000),'r',w1,2-2*np.cos((m2*w1+b2)*28000),'g',w1,2-2*np.cos((m3*w1+b3)*28000),'b',w1,2-2*np.cos((m4*w1+b4)*28000),'k',w1,2-2*np.cos((m5*w1+b5)*28000),'m')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(1.5, 1.65)
ax.set_ylim(0, .25)
plt.show()
