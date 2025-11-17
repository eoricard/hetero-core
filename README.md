# hetero-core
This repository allows reproduce the graps, and exploration of the interference in a hetero-core fiber 

Citation: Karla I Serrano-Arévalo et al 2025 J. Phys. Photonics 7 045036

DOI: 10.1088/2515-7647/ae0c4c

==============================

 <h2>1. Project </h2>

    ├── README.md                          <- README
    ├── data                              <- data of propagation constant
    │   ├── beta_LP01                      <- Data table of the propagation constant, for LP modes (lambda,beta(lambda))
    │   ├── beta_HE                        <- Data table of the propagation constant, for HE modes (lambda,beta(lambda))
    │   ├── beta_HE_2D                     <- Data table of the propagation constant, for HE modes and 5 refraction indexes  (lambda,beta(lambda,n3=1),beta(lambda,n3=1.1),beta(lambda,n3=1.2),beta(lambda,n3=1.3),beta(lambda,n3=1.4))
    | 
    ├── references                         <- suplemental information
    ├──main.py                             <-Main execution file for study control (select a study). 
    |  ├── (study==1) characteristic       <- characteristic equation
    |       ├── plot_characteristic.py        <- Script to graph the characteristic equation as a function of the refractive index n3 and the radius of the heterocore fiber r2   
    │  
    |  ├── (study==2) beta                 <- propagation constant
    │       ├── plot_betaLP.py               <- Script to graph the propagation constant, for LP modes 
    │       ├── plot_betaHE.py               <- Script to graph the propagation constant, for HE modes 
    │       ├── plot_betaHE_2D.py            <- Script to graph the propagation constant, for HE modes and 5 refracction indexes 
    │       ├── plot_diference.py            <- Script to graph the diference propagation constant, between HE11-HE12  
    │
    │   ├── (study==3) mode                <- modal distribution
    │       ├── plot_modeLP.py               <- Script to graph the modal distribution, for LP modes 
    │       ├── plot_modeHE.py               <- Script to graph the modal distribution, for HE modes 
    |
    │   ├── (study==4) overlap             <- normalization
    │       ├── overlap.py                 <- Script to calculate the overlap integral 
    │   
    │   ├── (study==5) propagation          <- propagation along z
    │       ├── propagation.py               <- Script to calculate the propagation in plane (z,y) for a sum of N modes HE 
    │   
    │   ├── (study==6) interference         <- interference
    │       ├── interference.py              <- Script to calculate the spectral interference for 4 modes interaction
    │   
    │   ├── (study==7) semi_analytical      <- semi-analytical model
    │       ├── semi_analytical.py              <- Script to calculate the spectral interference based in semi-analitycal model
    | 

   
    
