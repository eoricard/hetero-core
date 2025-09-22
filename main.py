import numpy as np
import SI_01_characteristic
import SI_02_beta
import SI_03_mode
import SI_04_overlap
import SI_05_propagation
import matplotlib.pyplot as plt
from scipy.special import jv, kv

loop_exec = 1 # Processing loop execution flag

study = 5  #characteristic 1 : beta, 2 : modes, 3 : overlap,4 : propagation, 5:

if study not in [1,2,3,4,5]:
    loop_exec = 0
    print("Please choose a correct boundary condition")

if study == 1: #Script to graph the characteristic equation as a function 
 #refractive index n3 
 #radius of the heterocore fiber r2 
 #plot_characteristic(n3,r2,"Figure1") 
 SI_01_characteristic.plot_characteristic(1.0, 62.5,"Figure1") 
 SI_01_characteristic.plot_characteristic(1.2, 62.5,"Figure2") 
 SI_01_characteristic.plot_characteristic(1.4, 62.5,"Figure3") 

if study == 2: #Script to graph the propagation constant as wavelength function
 SI_02_beta.plot_betaLP("beta_LP01","Figure1") #for LP modes
 SI_02_beta.plot_betaHE("beta_HE11","Figure2") #for HE modes
 SI_02_beta.plot_betaHE_2d("beta_HE11_2d","Figure3") #for HE modes and 4 refracction indexes
 SI_02_beta.plot_diference_beta("beta_HE11","beta_HE12","Figure4") #diference between HE modes

if study == 3: #Script to graph the transversal distribution function as wavelength function
 SI_03_mode.plot_modeLP("beta_LP01", 0.7, 80, "Figure1") #for LP modes
 SI_03_mode.plot_modeHE("beta_HE11", 0.7,1, 80, "Figure2") #for HE modes)

if study == 4: #Script to graph the overlap between modes LP and HE modes
 #calculate_overlap(P,H,wavelength,lim,"Figure1")
 SI_04_overlap.calculate_overlap(1,4,0.7,100, "Figure1")

if study == 5: #Script to graph the propagation between h1,h2 in [1,2,3,4], z=L
 #plot_propagation(h1,h2,wavelength,lim,L,"Figure1")
 SI_05_propagation.plot_propagation(1,2,0.7,100,28000,"Figure1")
plt.show()