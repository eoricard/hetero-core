# hetero-core
This repository allows reproduce the graps, and exploration of the interference in a hetero-core fiber 

This paper presents a numerical and experimental exploration of the transmission interference spectra of heterogeneous core optical fiber structures. The hetero-core device is fabricated using two multimode optical fiber segments and a coreless fiber section, using a simple and highly reproducible methodology. The refractometric response of the hetero-core device was evaluated as a function of the coreless fiber section length, ranging from 21 mm to 60 mm. The refractive index of the external medium was varied from 1.00 to a range of 1.2971-1.3912. The results show that the wavelength position of the minimum of the transmission spectrum shifts to longer wavelengths, with a sensitivity ranging from 4.32 nm/RIU  to 276.87 nm/RIU. The numerical model proposed in this work considers only two modes in the coreless fiber section, with the highest values of the overlapping integral that facilitate the determination of the position of the minimum transmittance in wavelength and its dependence on the length of the coreless section and the refractive index of the external medium. Consequently, this model can be employed as either an analytical method for designing multimode-coreless-multimode fiber-based sensors or as a complementary computational tool for determining the refractive index of a liquid sample surrounding the multimode-coreless-multimode fiber-optic structure.

==============================

 <h2>1. project </h2>

    ├── README.md          <- README
    ├── data
    │   ├── beta_LP         <- Data table of the propagation constant, for LP modes ($\lambda$, $\beta(\lambda)$)
    │   ├── beta_HE         <- Data table of the propagation constant, for HE modes ($\lambda$, $\beta(\lambda)$)
    │   ├── beta_HE_2D      <- Data table of the propagation constant, for LP modes ($\lambda$, $\beta(\lambda)$)
    |
    ├── references         <- Diccionarios de datos, manuales y todos material que explique los datos.
    │
    ├── reports            <- Análisis generado puede ser como HTML, PDF, LaTex, etc.
    │   └── figures        <- Gráficos y figuras generados usados en los reports.
    │
    ├── src                <- Código principal para el uso del proyecto.
    │   ├── __init__.py    <- Convierte al folder en un modulo de Python.
    │   │
    │   ├── _01_Business_Understanding      <- Exploración inicial para entender el negocio.
    │   │
    │   ├── _02_Data_Understanding          <- Exploración para entender los datos y sus disponibilidad.
    │   │
    │   ├── _03_Data_Preparation            <- Seleccionar, ordenar, agrupar, remover, etc. los datos para alcanzar los objetivos.
    │   │
    │   ├── _04_Modeling                    <- Scripts para generación del modelo y afinamiento de parámetros.
    │   │
    │   ├── _05_Evaluation                  <- Scripts para evaluación de resultados establecidos al inicio del proyecto.
    │   │
    │   └── _06_Deployment                  <- Scripts para el despliegue y pase a producción.
    │   
    ├── enviroment.yml              <- Archivo con listado de los paquetes necesarios para reproducir el entorno de análisis.
    │
    ├── 00.create_env.bat           <- Ejecutable para crear el entorno virtual con los parámetros del archivo "enviroment.yml".
    │
    └── 01.update_enviroment.bat    <- Ejecutable para actualizar el archivo "enviroment.yml" antes de ser compartido.


