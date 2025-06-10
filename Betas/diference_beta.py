import pandas as pd
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


fig1 = plt.figure("Filtro")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)


ax=fig1.add_subplot(1, 3, 1)
ax.plot(w1,n11-n12, 'r-', w1,n21-n22, 'g-', w1,n31-n32, 'b-', w1,n41-n42, 'k-',w1,n51-n52, 'm-')
ax.set_xlabel("wavelength [nm]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(0.6, 1.7)
ax.set_ylim(0.00018, .00056)
ax=fig1.add_subplot(1, 3, 2)
ax.plot(w1,n11-n12, 'r-', w1,n21-n22, 'g-', w1,n31-n32, 'b-', w1,n41-n42, 'k-',w1,n51-n52, 'm-')
ax.set_xlabel("wavelength [nm]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(1.5, 1.6)
ax.set_ylim(0.000425, .00047)
ax=fig1.add_subplot(1, 3, 3)
ax.plot(w1,(n11-n12)*28000, 'r-', w1,(n21-n22)*28000, 'g-', w1,(n31-n32)*28000, 'b-', w1,(n41-n42)*28000, 'k-',w1,(n51-n52)*28000, 'm-')
ax.set_xlabel("wavelength [$\mu$m]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(.6, 1.7)
ax.set_ylim(4, 14)
plt.show()
