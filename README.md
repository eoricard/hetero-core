# hetero-core
This repository allows reproduce the graps, and exploration of the interference in a hetero-core fiber 

==============================

 <h2>1. Project </h2>

    ├── README.md                         <- README
    ├── data
    │   ├── beta_LP01                     <- Data table of the propagation constant, for LP modes (lambda,beta(lambda))
    │   ├── beta_HE                       <- Data table of the propagation constant, for HE modes (lambda,beta(lambda))
    │   ├── beta_HE_2D                    <- Data table of the propagation constant, for HE modes and 4 refraction indexes (lambda,beta(lambda,n3=1),beta(lambda,n3=1.1),beta(lambda,,n3=1.2),beta(lambda,n3=1.3),beta(lambda,n3=1.4))
    | 
    ├── references                        <- suplemental information
    | 
    ├── SI_01_characteristic_equation     <- characteristic equation
    |   ├── plot_characteristic.py        <- Script to graph the characteristic equation as a function of the refractive index n3 and the radius of the heterocore fiber r2 #plot_characteristic(n3,r2,"Figure1")  
    │  
    ├── SI_02_propagation_constant       <- propagation constant
    │   ├── plot_betaLP.py               <- Script to graph the propagation constant, for LP modes 
    │   ├── plot_betaHE.py               <- Script to graph the propagation constant, for HE modes 
    │   ├── plot_betaHE_2D.py            <- Script to graph the propagation constant, for HE modes for 4 refracction indexes 
    │   ├── plot_diference.py            <- Script to graph the difreence propagation constant, between HE11-HE12  
    │
    ├── SI_03_modal_distribution         <- modal distribution
    │   ├── plot_modeLP.py               <- Script to graph the modal distribution, for LP modes 
    │   ├── plot_modeHE.py               <- Script to graph the modal distribution, for HE modes 
    |
    ├── SI_04_normalization              <- normalization
    │   ├── normalization_modeLP.py      <- Script to calculate the normalization constant, for LP modes 
    │   ├── normalization_betaHE.py      <- Script to calculate the normalization constant, for HE modes
    │   
    ├── SI_05_propagation                <- propagation
    │   ├── propagation.py               <- Script to calculate the propagation in plane (z,y) for a sum of modes HE 
    │   
    ├── SI_06_interference               <- interference
    │   ├── interference.py              <- Script to calculate the spectral interference.
    │   
    ├── SI_07_semi_analytical            <- semi_analytical
    │   ├── semi_analytical.py           <- Script to calculate the spectral interference, for the semi-analitycal solution 
    | 
    ├── SI_08_polarization               <- polarization
    │   ├── polarization.py              <- Script to calculate the spectral interference, for the semi-analitycal solution for 3 polarization states
   
    
