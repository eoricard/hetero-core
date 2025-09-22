#Script to graph the progation constant as a function of the refractive index n3 
#plot_characteristic(n3,r2,"Figure1") 
import pandas as pd
import matplotlib.pyplot as plt

# read CSV file

def plot_betaLP(csvfile,fig_name):
 filepath = f"data/{csvfile}.csv"
 dataframe = pd.read_csv(filepath, sep=',', engine='python')
 # Rename columns
 dataframe.columns = ['column1', 'column2']

 # Extraer columnas individuales para graficar
 wavelength = dataframe['column1']
 beta = dataframe['column2']

 fig1 = plt.figure(fig_name)
 fig1.suptitle(fig_name)  # Optional: adds title to the figure

 # Create Axes (subplot)
 ax = fig1.add_subplot(1, 1, 1)  # 1 row, 1 column, 1st plot
 ax.plot(wavelength,beta, 'r-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel(fr"{csvfile}")
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)
 return fig1

def plot_betaHE(csvfile,fig_name):
 filepath = f"data/{csvfile}.csv"
 dataframe = pd.read_csv(filepath, sep=',', engine='python')
 # Rename columns
 dataframe.columns = ['column1', 'column2']

 # Extraer columnas individuales para graficar
 wavelength = dataframe['column1']
 beta = dataframe['column2']


 fig1 = plt.figure(fig_name)
 fig1.suptitle(fig_name)  # Optional: adds title to the figure

 # Create Axes (subplot)
 ax = fig1.add_subplot(1, 1, 1)  # 1 row, 1 column, 1st plot
 ax.plot(wavelength,beta, 'r-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel(fr"{csvfile}")
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)
 return fig1

def plot_diference_beta(csvfile1,csvfile2,fig_name):
 filepath1 = f"data/{csvfile1}.csv"
 dataframe1 = pd.read_csv(filepath1, sep=',', engine='python')
 filepath2 = f"data/{csvfile2}.csv"
 dataframe2 = pd.read_csv(filepath2, sep=',', engine='python')
 # Rename columns
 dataframe1.columns = ['column1', 'column2']
 dataframe2.columns = ['column3', 'column4']
 # Extraer columnas individuales para graficar
 wavelength = dataframe1['column1']
 beta1 = dataframe1['column2']
 beta2 = dataframe2['column4']

 fig1 = plt.figure(fig_name)
 fig1.suptitle(fig_name)  # Optional: adds title to the figure

 # Create Axes (subplot)
 ax = fig1.add_subplot(3, 1, 1)  # 1 row, 1 column, 1st plot
 ax.plot(wavelength,beta1, 'r-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel(fr"{csvfile1}")
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)
 
 ax = fig1.add_subplot(3, 1 , 2)  # 1 row, 1 column, 1st plot
 ax.plot(wavelength,beta2, 'r-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel(fr"{csvfile2}")
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)
 
 ax = fig1.add_subplot(3, 1, 3)  # 1 row, 1 column, 1st plot
 ax.plot(wavelength,beta1-beta2, 'b-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel(fr"{csvfile1}-{csvfile2}")
 ax.set_ylim(0.00015, .0006)
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)
 return fig1

def plot_betaHE_2d(csvfile,fig_name):
 filepath = f"data/{csvfile}.csv"
 dataframe = pd.read_csv(filepath, sep='\s+', engine='python')
 # Rename columns
 dataframe.columns = ['column1', 'column2', 'column3', 'column4', 'column5', 'column6']

 # Extraer columnas individuales para graficar
 wavelength = dataframe['column1']
 beta1 = dataframe['column2']
 beta2 = dataframe['column3']
 beta3 = dataframe['column4']
 beta4 = dataframe['column5']
 beta5 = dataframe['column6']

 fig1 = plt.figure(fig_name)
 fig1.suptitle(fig_name)  # Optional: adds title to the figure

 ax=fig1.add_subplot(2, 1, 1)
 ax.plot(wavelength,beta1, 'r-', wavelength, beta2, 'g-', wavelength, beta3, 'b-', wavelength, beta4, 'k-', wavelength, beta5, 'm-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel("beta")
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)

 ax=fig1.add_subplot(2, 1, 2)
 ax.plot(wavelength,beta1-beta1, 'r-', wavelength, beta2-beta1, 'g-', wavelength, beta3-beta1, 'b-',wavelength, beta4-beta1, 'k-', wavelength, beta5-beta1, 'm-')
 ax.set_xlabel("wavelength [nm]")
 ax.set_ylabel("beta(beta(n3))-beta(n3=1)")
 ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)
 ax.axhline(0, color='black', linewidth=0.5)
 ax.set_xlim(0.6, 1.7)
 ax.set_ylim(0, .0000026)
 return fig1


