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



fig, ax1 = plt.subplots()
plt.plot(w,label=r'$\beta_{11}$', c="red", lw=2)
ax1.set_xlabel('wavelength [$\mu$ m]')
ax1.set_ylabel('$\beta$')
ax1.tick_params(labelsize=11, pad=8)
fig.suptitle('plot  constants of propagation ', fontsize=12)



fig, ax2 = plt.subplots()
plt.plot(w,b-b2,label=r'$\beta_{11}-\beta_{12}$', c="red", lw=2)
ax2.set_xlabel('wavelength [$\mu$ m]')
ax2.set_ylabel('$beta_{11}-beta_{12}$')
plt.legend()
ax2.tick_params(labelsize=11, pad=8)
fig.suptitle('plot  constants of propagation ', fontsize=12)


fig, ax3 = plt.subplots()
plt.plot(w,(b-b2)*28000,label=r'$(\beta_{11}-\beta_{12})28000$', c="red", lw=2)
ax3.set_xlabel('wavelength [$\mu$ m]')
ax3.set_ylabel('$(beta_{11}-beta_{12})L$')
ax3.tick_params(labelsize=11, pad=8)
fig.suptitle('plot  constants of propagation ', fontsize=12)
plt.show()
