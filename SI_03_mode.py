import numpy as np
from scipy.special import jv, kv
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define constants

def plot_modeLP(csvfile, wavelength,lim, fig_name):
    filepath = f"data/{csvfile}.csv"
    dataframe = pd.read_csv(filepath, sep=',', engine='python')
    # Rename columns
    dataframe.columns = ['column1', 'column2']
    
    # Extract individual columns for plotting
    lamb = dataframe['column1']
    beta1 = dataframe['column2']
    beta2 = interp1d(lamb, beta1, kind='linear')
    Beta = beta2(wavelength)
    c = [0.0684043, 0.1162414, 9.896161]
    d = [0.6961663, 0.4079426, 0.8974794]
    order = 1 
    # Define functions
    def n2(wavelength):
        return np.sqrt(1 + sum((d[i] * wavelength**2) / (wavelength**2 - c[i]**2) for i in range(3)))
    def n1(wavelength):
        return np.sqrt(n2(wavelength)**2 + 0.275)
    
    def k(wavelength):
        return 2 * np.pi / wavelength

    def P_01(wavelength):
        return np.sqrt((n1(wavelength) * k(wavelength))**2 - Beta**2)

    def Q_01(wavelength):
        return np.sqrt(Beta**2 - (n2(wavelength) * k(wavelength))**2)

    def r(x, y):
        return np.sqrt(x**2 + y**2)

    def Psi_11(x, y, z, wavelength):
        radius = r(x, y)
        P = P_01(wavelength)
        Q = Q_01(wavelength)
        core_radius = 31.25  # μm

        if radius < core_radius:
            return (jv(0, P * radius) / jv(0, P * core_radius)) * np.exp(1j * Beta * z)
        else:
            return (kv(0, Q * radius) / kv(0, Q * core_radius)) * np.exp(1j * Beta * z)

    # Vectorize the Psi_11 function to apply it on a meshgrid
    Psi_11_vectorized = np.vectorize(Psi_11, otypes=[np.complex128])

    # Define the mesh grid
    x_vals = np.linspace(-lim, lim, 200)
    y_vals = np.linspace(-lim, lim, 200)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Calculate the field
    field = Psi_11_vectorized(X, Y, 1, wavelength)

    # Calculate the density
    density = np.abs(field)
    dx = x_vals[1] - x_vals[0]
    dy = y_vals[1] - y_vals[0]
    integral = np.sum(density) * dx * dy

    # Plotting
    fig1 = plt.figure(fig_name)
    fig1.suptitle(fig_name)  # Optional: adds title to the figure

    ax = fig1.add_subplot(1, 1, 1)
    c = ax.pcolormesh(X, Y, density / np.sqrt(integral), cmap="viridis", shading='auto')
    fig1.colorbar(c, ax=ax, label="Density")
    ax.set_xlabel("x [μm]", fontsize=14)
    ax.set_ylabel("y [μm]", fontsize=14)
    ax.set_title("$Mf(x,y)$ $\\lambda=$" fr"{wavelength}", fontsize=16)
    ax.axis('equal')
    plt.tight_layout()

    return fig1

def plot_modeHE(csvfile, wavelength,n3,lim, fig_name):
    filepath = f"data/{csvfile}.csv"
    dataframe = pd.read_csv(filepath, sep=',', engine='python')
    # Rename columns
    dataframe.columns = ['column1', 'column2']
    
    # Extract individual columns for plotting
    lamb = dataframe['column1']
    beta1 = dataframe['column2']
    beta2 = interp1d(lamb, beta1, kind='linear')
    Beta = beta2(wavelength)
    c = [0.0684043, 0.1162414, 9.896161]
    d = [0.6961663, 0.4079426, 0.8974794]
    order = 1 
    # Define functions
    def n2(wavelength):
        return np.sqrt(1 + sum((d[i] * wavelength**2) / (wavelength**2 - c[i]**2) for i in range(3)))
    
    def k(wavelength):
        return 2 * np.pi / wavelength

    def P_01(wavelength):
        return np.sqrt((n2(wavelength) * k(wavelength))**2 - Beta**2)

    def Q_01(wavelength):
        return np.sqrt(Beta**2 - (n3 * k(wavelength))**2)

    def r(x, y):
        return np.sqrt(x**2 + y**2)

    def Psi_11(x, y, z, wavelength):
        radius = r(x, y)
        P = P_01(wavelength)
        Q = Q_01(wavelength)
        core_radius = 62.5  # μm

        if radius < core_radius:
            return (jv(0, P * radius) / jv(0, P * core_radius)) * np.exp(1j * Beta * z)
        else:
            return (kv(0, Q * radius) / kv(0, Q * core_radius)) * np.exp(1j * Beta * z)

    # Vectorize the Psi_11 function to apply it on a meshgrid
    Psi_11_vectorized = np.vectorize(Psi_11, otypes=[np.complex128])

    # Define the mesh grid
    x_vals = np.linspace(-lim, lim, 200)
    y_vals = np.linspace(-lim, lim, 200)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Calculate the field
    field = Psi_11_vectorized(X, Y, 1, wavelength)

    # Calculate the density
    density = np.abs(field)
    dx = x_vals[1] - x_vals[0]
    dy = y_vals[1] - y_vals[0]
    integral = np.sum(density) * dx * dy

    # Plotting
    fig1 = plt.figure(fig_name)
    fig1.suptitle(fig_name)  # Optional: adds title to the figure

    ax = fig1.add_subplot(1, 1, 1)
    c = ax.pcolormesh(X, Y, density / np.sqrt(integral), cmap="viridis", shading='auto')
    fig1.colorbar(c, ax=ax, label="Density")
    ax.set_xlabel("x [μm]", fontsize=14)
    ax.set_ylabel("y [μm]", fontsize=14)
    ax.set_title("$Mf(x,y)$ $\\lambda=$" fr"{wavelength}", fontsize=16)
    ax.axis('equal')
    plt.tight_layout()

    return fig1
# Example usage of the function
#plot_modeLP("beta_LP01", 0.7, 80, "Figure1")
#plot_modeHE("beta_HE11", 0.7,1, 80, "Figure2")
#plt.show()
