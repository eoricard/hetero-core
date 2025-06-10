import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV

dataframe = pd.read_csv('HE11_2d.csv', sep='\s+', engine='python')


# Renombrar las columnas
dataframe.columns = ['Wavelength', 'n1', 'n1p1', 'n1p2', 'n1p3', 'n1p4']

# Extraer columnas individuales para graficar
w = dataframe['Wavelength']
n1 = dataframe['n1']
n2 = dataframe['n1p1']
n3 = dataframe['n1p2']
n4 = dataframe['n1p3']
n5 = dataframe['n1p4']


fig1 = plt.figure("Filtro")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)


ax=fig1.add_subplot(2, 1, 1)
ax.plot(w,n1, 'r-', w, n2, 'g-', w, n3, 'b-', w, n4, 'k-', w, n5, 'm-')
ax.set_xlabel("wavelength [nm]")
ax.set_ylabel("beta")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)

ax=fig1.add_subplot(2, 1, 2)
ax.plot(w,n1-n1, 'r-', w, n2-n1, 'g-', w, n3-n1, 'b-', w, n4-n1, 'k-', w, n5-n1, 'm-')
ax.set_xlabel("wavelength [nm]")
ax.set_ylabel("beta(n3)-beta(n3=1)")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)
ax.set_xlim(0.6, 1.7)
ax.set_ylim(0, .0000026)

plt.show()
# Graficar n1 en función de la longitud de onda
plt.plot(w, n1, w, n2, w, n3, w, n4, w, n5)

# Opcional: agregar título, etiquetas, y leyenda
plt.title('n1 vs Wavelength')
plt.xlabel('Wavelength')
plt.ylabel('n1')
plt.legend()
plt.grid(True)
plt.plot(w, n1, w, n2, w, n3, w, n4, w, n5)

# Mostrar la gráfica
plt.show()
