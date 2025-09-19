# hetero-core
This repository allows reproduce the graps, and exploration of the interference in a hetero-core fiber 

This paper presents a numerical and experimental exploration of the transmission interference spectra of heterogeneous core optical fiber structures. The hetero-core device is fabricated using two multimode optical fiber segments and a coreless fiber section, using a simple and highly reproducible methodology. The refractometric response of the hetero-core device was evaluated as a function of the coreless fiber section length, ranging from 21 mm to 60 mm. The refractive index of the external medium was varied from 1.00 to a range of 1.2971-1.3912. The results show that the wavelength position of the minimum of the transmission spectrum shifts to longer wavelengths, with a sensitivity ranging from 4.32 nm/RIU  to 276.87 nm/RIU. The numerical model proposed in this work considers only two modes in the coreless fiber section, with the highest values of the overlapping integral that facilitate the determination of the position of the minimum transmittance in wavelength and its dependence on the length of the coreless section and the refractive index of the external medium. Consequently, this model can be employed as either an analytical method for designing multimode-coreless-multimode fiber-based sensors or as a complementary computational tool for determining the refractive index of a liquid sample surrounding the multimode-coreless-multimode fiber-optic structure.

==============================

 <h2>1. project </h2>

    ├── README.md          <- README
    ├── data
    │   ├── beta_LP01       <- Data table of the propagation constant, for LP modes 
    │   ├── beta_HE         <- Data table of the propagation constant, for HE modes 
    │   ├── beta_HE_2D      <- Data table of the propagation constant, for LP modes 
    |
    ├── references         <- suplemental information
    │
    ├── figures           <- figures for suplemental information.
    │  
    ├── SI_01_propagation_constant      <-propagation constant
    │   ├── Plot_betaLP.py               <- Data table of the propagation constant, for LP modes 
    │   ├── Plot_betaHE.py               <- Data table of the propagation constant, for HE modes 
    │   ├── Plot_betaHE_2D.py            <- Data table of the propagation constant, for LP modes 
    │   ├── Plot_diference.py            <- Data table of the propagation constant, for HE modes 
    │   ├── Plot_betaHE_2D.py            <- Data table of the propagation constant, for LP modes 
    │
    ├── _02_Data_Understanding          <- Exploración para entender los datos y sus disponibilidad.
    |
    ├── _03_Data_Preparation            <- Seleccionar, ordenar, agrupar, remover, etc. los datos para alcanzar los objetivos.
    │   
    ├── _04_Modeling                    <- Scripts para generación del modelo y afinamiento de parámetros.
    │   
    ├── _05_Evaluation                  <- Scripts para evaluación de resultados establecidos al inicio del proyecto.
    │   
    ├── _06_Deployment                  <- Scripts para el despliegue y pase a producción.
    
