import pandas as pd
import matplotlib.pyplot as plt

csv=pd.read_csv('dispersionHE11.csv',sep=',')

dataframe=pd.DataFrame(csv)
dataframe.columns = ['Wavelength','Beta'] # renombra las columna!
w=dataframe["Wavelength"]
b=dataframe["Beta"]

csv2=pd.read_csv('DispersionHE12.csv',sep=',')
dataframe2=pd.DataFrame(csv2)
dataframe2.columns = ['Wavelength2','Beta2'] # renombra las columna!
w2=dataframe2["Wavelength2"]
b2=dataframe2["Beta2"]


fig1 = plt.figure("Filtro")
fig1.subplots_adjust(hspace=0.5, wspace=0.5)


ax=fig1.add_subplot(2, 2, 1)
ax.plot(w,b,label=r'$\beta_{11}$', c="red", lw=2)
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)

ax=fig1.add_subplot(2, 2, 2)
ax.plot(w,b2,label=r'$\beta_{11}-\beta_{12}$')
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)


ax=fig1.add_subplot(2, 2, 3)
ax.plot(w,(b-b2)*28000,label=r'$(\beta_{11}-\beta_{12})28000$', c="red", lw=2)
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)

ax=fig1.add_subplot(2, 2, 4)
ax.plot(w,w)
ax.set_xlabel("h")
ax.set_ylabel("RE-LE")
ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
ax.axhline(0, color='black', linewidth=0.5)


plt.show()
