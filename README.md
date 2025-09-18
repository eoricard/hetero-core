# hetero-core
This repository allows reproduce the graps, and exploration of the interference in a hetero-core fiber 

This paper presents a numerical and experimental exploration of the transmission interference spectra of heterogeneous core optical fiber structures. The hetero-core device is fabricated using two multimode optical fiber segments and a coreless fiber section, using a simple and highly reproducible methodology. The refractometric response of the hetero-core device was evaluated as a function of the coreless fiber section length, ranging from 21 mm to 60 mm. The refractive index of the external medium was varied from 1.00 to a range of 1.2971-1.3912. The results show that the wavelength position of the minimum of the transmission spectrum shifts to longer wavelengths, with a sensitivity ranging from 4.32 nm/RIU  to 276.87 nm/RIU. The numerical model proposed in this work considers only two modes in the coreless fiber section, with the highest values of the overlapping integral that facilitate the determination of the position of the minimum transmittance in wavelength and its dependence on the length of the coreless section and the refractive index of the external medium. Consequently, this model can be employed as either an analytical method for designing multimode-coreless-multimode fiber-based sensors or as a complementary computational tool for determining the refractive index of a liquid sample surrounding the multimode-coreless-multimode fiber-optic structure.

\documentclass[12pt]{iopart} % IOP Class
\usepackage{iopams} % Additional package for math symbols
\usepackage{upgreek} % Upright Greek letters
\usepackage{graphicx} % For including images
\usepackage{booktabs} % For better-looking tables
\usepackage{xcolor} % For colored text and graphics
\usepackage{amsmath,amsfonts}
\usepackage{algorithmic}
\usepackage{algorithm}
\usepackage{array}
\usepackage[caption=false,font=normalsize,labelfont=sf,textfont=sf]{subfig}
\usepackage{textcomp}
\usepackage{stfloats}
\usepackage{url}
\usepackage{verbatim}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{tabularx}
\usepackage{url}
\usepackage[colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black]{hyperref}

\begin{document}


\title[Semi-analytical  model for coreless fiber-optic ....]{Supplementary Information: Semi-analytical  model for coreless fiber-optic refractive index sensors and experimental validation}
%{Full title}


%\begin{abstract}
%This paper presents a combined numerical and experimental investigation of the transmission interference spectra of heterogeneous core optical fiber structures, accompanied by a Python-based repository for data analysis and simulation. The hetero-core device is fabricated using two multimode optical fiber segments and a coreless fiber section, using a simple and highly reproducible methodology. The refractometric response of the hetero-core device was evaluated as a function of the coreless fiber section length, ranging from 21 mm to 60 mm. The refractive index of the external medium was varied from 1.0 to a range of 1.2971-1.3912. The results show that the wavelength position of the minimum of the transmission spectrum shifts to longer wavelengths, with a sensitivity ranging from 4.32 nm/RIU  to 276.87 nm/RIU. The semi-analytical model proposed in this work considers only two modes in the coreless fiber section, with the highest values of the overlapping integral that facilitate the determination of the position of the minimum transmittance in wavelength and its dependence on the length of the coreless section and the refractive index of the external medium. Consequently, this model can be employed as either an semi-analytical method for designing multimode-coreless-multimode fiber-based sensors or as a complementary computational tool for determining the refractive index of a liquid sample surrounding the multimode-coreless-multimode fiber-optic structure.
%\end{abstract}
%\noindent{\it Keywords}: Fiber-optic sensor; multimodal interference; hetero-core structure; coreless fiber model;  Python-based repository.


\section{Model}
Here, we explain the steps necessary for generating the graphs shown in the main article using the Python programs included in the repository,
 (\href{https://github.com/eoricard/hetero-core}{\textcolor{blue}{https://github.com/eoricard/hetero-core}}). In our model, we considered that the device is formed by splicing three segments of fused silica fibers Fig. 1 (a) in main document. We are interested in the spectral behavior of these devices, we considered in our model that:

\begin{enumerate}
	\item The first region (Region 1) is a multimode fiber with $d_1=62.5\ \mu$m and $d_2=125\ \mu$m, $n_1=n_{core}$, $n_2=n_{fs}$ and only  $\text{LP}_{0p}$ modes are coupled.
	\item The second region (Region 2) is a coreless fiber with a length $L$, and index refraction $n_2=n_{fs}$, the device is surrounded for a medium with index refraction $n_{3}$. The modes within the second fiber are $\text{HE}_{1h}$ modes.
	\item  The third region (Region 3) is a second multimode fiber. The spectral behavior is measured at the output port.
\end{enumerate}

The programs are structured as follow (see Fig.\ref{fig:diagraman}-SI). We start with the calculation of  modal constant propagation $\beta$, next we calculate the modal distribution $f(x,y)$ and the normalization constant $M$. This allows to calculate the overlap integral $\eta_{ph}$, with all before we can calculate the interference, and  the behavior with  parameters $L,\lambda,n_3$.
\begin{figure}[h]
	\centering
	\includegraphics[width=1\linewidth]{fig1_SI.pdf}
	\caption{Diagram of the steps for obtaining interference in our devices.}
	\label{fig:diagraman}
\end{figure}
\section{Modal constants propagation $\beta(\lambda,n_3)$ }
All programs and data for this section are available at \\
\href{https://github.com/eoricard/hetero-core/tree/main/Betas}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/Betas}}.




As we show later, the properties of interference in this type of device are generated by the phase differences between the modes propagating along Region 2 of the device. We start with the calculation of the modal propagation constants. The refractive index of fused silica can be described using the Sellmeier equation, the refractive index of fused silica can be described as \cite{Agrawal_2013}:
\begin{equation}
n_{fs}^{2}(\lambda)=1+\frac{A_{1}\lambda^{2}}{\lambda^{2}-B_{1}}+\frac{A_{2}\lambda^{2}}{\lambda^{2}-B_{2}}+\frac{A_{3}\lambda^{2}}{\lambda^{2}-B_{3}},
\end{equation}

\noindent where  	$A_{1}=0.696166300$,	$A_{2}=0.407942600$, $A_{3}=0.897479400$, $B_{1}=4.67914826\times10^{-3}$, $B_{2}=1.35120631\times 10^{-2}$ and $B_{3}=97.9340025$.

With the numerical aperture for a multimode fiber NA=0.275 we can obtain the index refraction in the core as
\begin{equation}
n_{core}(\lambda)=\sqrt{n_{fs}(\lambda)+\text{NA}}
\end{equation}

Modal propagation constant $\beta$ is calculated with the characteristic equation

\begin{equation}
	\left[\frac{J'_{m}(pa)}{pJ_{m}(pa)}+\frac{K'_{m}(qa)}{qK_{m}(qa)}\right]
	\left[\frac{J'_{m}(pa)}{pJ_{m}(pa)}+\frac{n_{2}^{2}}{n_{1}^{2}}\frac{K'_{m}(qa)}{qK_{m}(qa)}\right]=
	\left(\frac{m\beta k_{0}(n_{1}^{2}-n_{2}^{2})}{an_{1}p^{2}q^{2}}\right)^{2},
	\label{ecu:ecuacioncaracteristica}
\end{equation}

\noindent with $q=(\beta^{2}-n_{2}^{2}k_{0}^{2})^{1/2}$ and $p^{2}+q^{2}=(n_{1}^{2}-n_{2}^{2})k_{0}^{2}$, $m$ is the order of the Bessel functions, 
$n_{1}$ is the core index,  $n_{2}$ is the cladding index , and $a$ is the core radius.  Here, we have two cases: 
\begin{enumerate}
	\item{Multi mode fiber: $n_{1}=n_{core}$, $n_{2}=n_{fs}$, $a=31.25\ \mu $m.}
	\item{Coreless fiber: $n_{1}=n_{fs}$, $n_{2}=n_{3}$, $a=62.5\ \mu $m.}
\end{enumerate}

In Fig. \ref{fig:caracteristica}-SI we show a graph of the function defined as the Left Part minus the Right Part $\text{LH}-\text{RE}(\lambda,n_{fs}(\lambda),n_{3},p,q(p),a)$ of Eq. \ref{ecu:ecuacioncaracteristica}, as a function of variable $p$ with $\lambda$ and $n_{3}$ fixes, for a coreless fiber obtained with the program \href{https://github.com/eoricard/hetero-core/tree/main/Characteristic}{\textcolor{blue}{characteristic.py}} included in the repository. The zeros indicate the order of  $\text{HE}_{1h}$ mode, the first root  correspond with the mode $\text{HE}_{11}$ of the fundamental mode, the second root corresponds with the mode $\text{HE}_{12}$, etc. The number of zeros indicates, the maximum  modes inside the fiber. In the same figure, we show a close-up of the roots, with three curves corresponding to three wavelengths: $ \lambda = 1550\ \text{nm}$ red curve, $\lambda=1200\ \text{nm}$ green curve, and $\lambda=600\ \text{nm}$ blue curve. Notably, as the wavelength increases, the point where the function (LH-RE) crosses zero decreases. 

\begin{figure}[h]
	\centering
	\includegraphics[width=1\linewidth]{fig2_SI_v2.pdf}
	\caption{Roots of the characteristic equation and close up to interesting region in a coreless fiber with $n_{3}=1,\ 1.2$ and $n_{3}=1.4$ for three values of $\lambda= 600,\ 1200,\ 1550\ n$m}.
	\label{fig:caracteristica}
\end{figure}


\begin{figure}
	\centering
	\includegraphics[width=1\linewidth]{fig3_SI.pdf}
	\caption{Graph of the functions $\beta_{11}^x(\lambda,n_3)$ and $\beta_{12}^x(\lambda,n_3)$ in a coreless fiber for five values of $n_3$. For comparative analysis, we also plot the difference concerning to $n_3 = 1$.}
	\label{fig:dispersion_2d}
\end{figure}



To minimize computation time, in the repository  we included tables with the values of  $\beta_{0p}^x(\lambda)$ and $\beta_{1h}^x(\lambda,n_3)$ in the range of $\lambda \in [600-1700\ \text{nm}]$ and $n_3 \in [1,1.4]$ with names \href{https://github.com/eoricard/hetero-core/tree/main/Betas}{\textcolor{blue}{\text{HE11\_2d.csv, HE12\_2d.csv, HE13\_2d.csv, HE14\_2d.csv}}}, the first column is the wavelength $\lambda$, second correspond with the $\beta$ values for $n_3=1$, third correspond with $n_3=1.1$, and the last correspond with the $\beta$ values for $n_3=1.4$. In Fig. \ref{fig:dispersion}-SI  we can see curves for $\beta_{11}^x(\lambda,n_3)-\beta_{12}^x(\lambda,n_3)$ and a close up around $\lambda=1550\ \text{nm}$, together, with a graph of  $[\beta_{11}^x(\lambda,n_3)-\beta_{12}^x(\lambda,n_3)]L$ with $L=28\ \text{mm}$, we note that the condition, 


\begin{equation}
	L_{beat}=\frac{2\pi N}{(\beta_{11}^x(\lambda,n_3)-\beta_{12}^x(\lambda,n_3))}
\end{equation}
is satisfied $N=1$ for $\lambda\approx 800\ \text{nm}$ and $N=2$ is satisfied with $\lambda\approx 1550\  \text{nm}$ note that experimentally the interference shows two minima near of this wavelength. Here we can conclude that i) the dependence with $n_3$ is more evident at $1550\ \text{nm} $ instead of $800\ \text{nm}$, ii) the beat length that can explain the experimental data is the interaction between modes $\text{HE}_{11}^x-\text{HE}_{12}^x$.

\begin{figure}
	\centering
	\includegraphics[width=1\linewidth]{fig4_SI.pdf}
	\caption{Graph of the difference between, modal propagation constant $\beta_{11}^x(\lambda,n_3)$ and $\beta_{12}^x(\lambda,n_3)$ in a coreless fiber, showing a linear dependence.}
	\label{fig:dispersion}
\end{figure}


\section{Modal distribution, modes LP}

All programs and data for this section are available at\\
\href{https://github.com/eoricard/hetero-core/tree/main/ModesLP}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/ModesLP}}

The transverse distribution for  modes $\text{LP}_{0p}$ is given by 
\begin{equation}
	\begin{split}
		f_{0p}(x,y)=& J_{p-1}(\gamma r)/J_{p-1}(\gamma a)  \ ; \ \ r<a,\ \ \ p=1,2...\ \\
		f_{0p}(x,y)=& K_{p-1}(\kappa r)/K_{p-1}(\kappa a)  \ ;\ \ r>a,\ \ \ p=1,2...\ \ \ \ 
	\end{split}
\end{equation}
with $r = (x^2 + y^2)^{1/2}$,  $\kappa=(\beta_{0 p}^{2}-n_{cd}^{2}k_{0}^{2})^{1/2}$,
$ \gamma^{2}+\kappa^{2}=(n_{co}^{2}-n_{cd}^{2})k_{0}^{2}
$,  where $n_{co}$ is the core refractive index  $n_{co}=\sqrt{n_{fs}^2+0.275}$ and 
$n_{cd}$ is the cladding refractive index $n_{cd}=n_{fs}$. The core radius of the  MMF is  $a=32.5\ \mu $m;  $J_{p}$ and $K_{p}$ are, respectively, the Bessel functions of the first kind, and the Bessel functions of the second kind, both with order $p$ \cite{Agrawal_2013}. 

\begin{figure}[h]
	\centering
	\includegraphics[width=\linewidth]{fig5_SI.pdf}
	\caption{Density plots of the functions $f_{01}(x,y)$ and $f_{02}(x,y)$ in a Multimode fiber.}
	\label{fig:modesLP}
\end{figure}
\section{Modal distribution, modes HE}
All programs and data for this section are available at\\
\href{https://github.com/eoricard/hetero-core/tree/main/ModesHE}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/ModesHE}}  


The transverse distribution for  modes $\text{HE}_{1h}$ is given by 
\begin{equation}
	\begin{split}
		f_{1 h}(x,y)=& J_{h-1}(\gamma r)/J_{h-1}(\gamma a)  \ ;\ \ r<a\ \ \ \ h=1,2...\ , \ \\
		f_{1 h}(x,y)=& K_{h-1}(\kappa r)/K_{h-1}(\kappa a)  \ ;\ \ r>a\ \ \ h=1,2...\  ,
	\end{split}
\end{equation}
with $r = (x^2 + y^2)^{1/2}$,  $\kappa=(\beta_{1 h}^{2}-n_{cd}^{2}k_{0}^{2})^{1/2}$,
$ \gamma^{2}+\kappa^{2}=(n_{co}^{2}-n_{cd}^{2})k_{0}^{2}
$,  where $n_{co}$ is the core refractive index $n_{co}=n_{fs}$ and, 
$n_{cd}$ is the cladding refractive index $n_{cd}=n_3$. The core radius of the coreless fiber in Region 2 is  $a=62.5\ \mu $m ;  $J_{h}$ and $K_{h}$ are, respectively, the Bessel functions of the first order, and the modified Bessel functions of the second kind, both with order $h$ \cite{Agrawal_2013}. 
\begin{figure}[h]
	\centering
\includegraphics[width=\linewidth]{fig6_SI.pdf}

\caption{Density plots of the functions $f_{11}^x(x,y)$ and $f_{12}^x(x,y)$ in a Coreless fiber.}
\label{fig:modesHE}
\end{figure}

\section{Normalization}
The transverse distribution functions are normalized such that
\begin{equation}
	\left[M_{\nu}^{2}\int_{-\infty}^{\infty} dx\int_{\infty}^{\infty} dy f_{\nu}(x,y)f^{*}_{\nu}(x,y)\right]^{1/2}=1.
\end{equation}
The values of $M_\nu$ are determined by
\begin{equation}
	M_{\nu}=\left[\int_{-\infty}^{\infty} dx\int_{-\infty}^{\infty} dy f_{\nu}(x,y)f^{*}_{\nu}(x,y)\right]^{-1/2}.
\end{equation}
\begin{figure}[h]
	\centering
	\includegraphics[width=\linewidth]{fig7_SI.pdf}
	\caption{Normalized density plots of the functions $f_{01}^{x}(x,y)$, $f_{02}^{x}(x,y)$, $f_{11}^{x}(x,y)$ and $f_{12}^{x}(x,y)$.}
	\label{fig:normalized modes}
\end{figure}
In fig. \ref{fig:normalized modes}-SI we can see the transverse distribution functions normalized. 

\section{Overlap}
All programs and data for this section are available at\\
\href{https://github.com/eoricard/hetero-core/tree/main/Overlap}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/Overlap}}  


The overlap integral quantifies the amount of light coupled between the modes in Region 1 and the modes in Region 2. It is defined as
\begin{equation}
	\eta_{p h}=\frac{\left|\displaystyle  \iint_{-\infty}^{\infty} dx dy f_{0p}(x,y) f_{1h}^{*}(x,y)\right|^2}{\displaystyle  \iint_{-\infty}^{\infty} dx dy f_{0p}(x,y) f_{0p}^{*}(x,y) \times \displaystyle  \iint_{-\infty}^{\infty} dx dy f_{1h}(x,y) f_{1h}^{*}(x,y) }
	\label{eq:overlap}
\end{equation}
for non-normalized functions distributions. 

\begin{table}[h]

	\caption{Overlap integral values numerically obtained for the interaction between the first four LP modes and four HE modes are shown, with high-value interactions highlighted in red.}
	\begin{center}
		\begin{tabular}{|c|c|c|c|}		
			\hline
			$\textcolor{red}{\eta^{x}_{11}=0.521}$ & $\textcolor{red}{\eta^{x}_{12}=0.438}$ &$\eta^{x}_{13}=0.067$ &$\eta^{x}_{14}=0.001$ \\
			\hline
			$\eta^{x}_{21}=0.053$ & $\eta^{x}_{22}=0.016$ &$\textcolor{red}{\eta^{x}_{23}=0.445}$ &$\textcolor{red}{\eta^{x}_{24}=0.390}$ \\
			\hline
			$\eta^{x}_{31}=0.022$ & $\eta^{x}_{32}=0.002$ &$\eta^{x}_{34}=0.039$ &$\eta^{x}_{35}=0.025$ \\
			\hline
			$\eta^{x}_{41}=0.012$ & $\eta^{x}_{42}=0.000$ &$\eta^{x}_{43}=0.016$ &$\eta^{x}_{44}=0.004$ \\
			\hline
		\end{tabular}
	\end{center}
\label{Table:overlap}
\end{table}

\begin{figure}[h]
	\centering
	\includegraphics[width=18cm]{fig8_SI.pdf}
	\caption{Spectral representation of the overlap integral, indicating weak sensitivity to wavelength. } 
	\label{fig:overlap}
\end{figure}

\newpage
\section{Interference}

Spectral interference in these devices is obtained as follows. We supposed that the pump has a fixed wavelength $\lambda$. In Region 1, the pump can be write as a superposition of modes $LP=LP^x$ polarized along $x$ axis.

\begin{equation}
	\begin{split}
			E_{in}(x,y,z)&=A_{1}M_{01}f_{01}(x,y)e^{i(\beta_{01}(\lambda)z)}+A_{2}M_{2}f_{02}(x,y)e^{i(\beta_{02}(\lambda)  z)}+...\\
			&=\sum_{p=1}^{P} A_{p}M_{0p}f_{0p}(x,y)e^{i(\beta_{0p}(\lambda))},
	\end{split}
\end{equation}

\noindent where $f_{0p}(x,y)$ is the transversal distribution and $A_p$ the initial amplitude. In Region 2 the field cavity  $E_{cav}(r;\lambda)$ can be write as
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z)=&B_{1}M_{11}f_{11}(x,y)e^{i(\beta_{11}(\lambda)z)}+B_{2}M_{12}f_{12}(x,y)e^{i(\beta_{12}(\lambda)  z)}+...\\
		&=\sum_{h=1}^{H} B_{h}M_{1h}f_{1h}(x,y)e^{i(\beta_{1h}(\lambda) z)}=\sum_{h=1}^{H}\sum_{p=1}^{P}A_{p}\eta_{ph}M_{1h} f_{1h}(x,y)e^{i[\beta_{1h}(\lambda)z]},
	\end{split}
\end{equation}
with
\begin{equation}
\begin{split}
B_1=&(A_1\eta_{11}+A_2\eta_{21}+A_3\eta_{31}+ .....)\\
B_2=&(A_1\eta_{12}+A_2\eta_{22}+A_3\eta_{32}+ .....),\\
\end{split}
\end{equation}
where $\eta_{ph}$ is the overlap integral Eq. \ref{eq:overlap}



Before arriving at the second splice section, the cavity field travels a distance $L$, acquiring a phase $\beta_{1h}(\lambda) L$, and can be expressed as

\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L;\lambda)=
		\sum_{h=1}^{H}\sum_{p=1}^{P}A_{p}\eta_{ph}M_{1h} f_{1h}(x,y)e^{i[\beta_{1h}(\lambda)L]},
	\end{split}
\end{equation}


Case 1: $P=H=1$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=A_{1}\eta_{11}M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]},
	\end{split}
\end{equation}

Case 2:  $P=H=2$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=&(A_{1}\eta_{11}+A_{2}\eta_{21})M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]}\\
		+&(A_{1}\eta_{12}+A_{2}\eta_{22})M_{12} f_{12}(x,y)e^{i[\beta_{12}(\lambda)L]},
	\end{split}
\end{equation}

Case 3:  $P=H=3$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=&(A_{1}\eta_{11}+A_{2}\eta_{21}+A_{3}\eta_{31})M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]}\\
		+&(A_{1}\eta_{12}+A_{2}\eta_{22}+A_{3}\eta_{32})M_{12} f_{12}(x,y)e^{i[\beta_{12}(\lambda)L]}\\
	     +&(A_{1}\eta_{13}+A_{2}\eta_{23}+A_{3}\eta_{33})M_{13} f_{13}(x,y)e^{i[\beta_{13}(\lambda)L]},
	\end{split}
\end{equation}

Case 4: $P=H=4$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=&(A_{1}\eta_{11}+A_{2}\eta_{21}+A_{3}\eta_{31}+A_{4}\eta_{41})M_{1} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]}\\
		+&(A_{1}\eta_{12}+A_{2}\eta_{22}+A_{3}\eta_{32}+A_{4}\eta_{42})M_{12} f_{12}(x,y)e^{i[\beta_{12}(\lambda)L]}\\
		+&(A_{1}\eta_{13}+A_{2}\eta_{23}+A_{3}\eta_{33}+A_{4}\eta_{43})M_{13} f_{13}(x,y)e^{i[\beta_{13}(\lambda)L]}\\
	    +&(A_{1}\eta_{14}+A_{2}\eta_{24}+A_{3}\eta_{34}+A_{4}\eta_{44})M_{14} f_{14}(x,y)e^{i[\beta_{14}(\lambda)L]}.\\
	\end{split}
\end{equation}

Considering only the higher values in Table \ref{Table:overlap}, namely  $\eta_{11},\eta_{12},\eta_{23}$ and $\eta_{24}$ the preceding equations can be simplified as


 
Case 1: $P=H=1$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=A_{1}\eta_{11}M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]},
	\end{split}
\end{equation}


Case 2: $P=H=2$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=(A_{1}\eta_{11})M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]}+(A_{1}\eta_{12})M_{12} f_{12}(x,y)e^{i[\beta_{12}(\lambda)L]},
	\end{split}
	\label{eq:field2modes}
\end{equation}

Case 3: $P=H=3$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=&(A_{1}\eta_{11})M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]}+
		(A_{1}\eta_{12})M_{12} f_{12}(x,y)e^{i[\beta_{12}(\lambda)L]}\\
		+&(A_{2}\eta_{23})M_{13} f_{13}(x,y)e^{i[\beta_{13}(\lambda)L]},
	\end{split}
\end{equation}

Case 4: $P=H=4$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=(A_{1}\eta_{11})M_{11} f_{11}(x,y)e^{i[\beta_{11}(\lambda)L]}+
		(A_{1}\eta_{12})M_{12} f_{12}(x,y)e^{i[\beta_{12}(\lambda)L]}\\
		+(A_{2}\eta_{23})M_{13} f_{13}(x,y)e^{i[\beta_{13}(\lambda)L]}+
		(A_{2}\eta_{24})M_{14} f_{14}(x,y)e^{i[\beta_{14}(\lambda)L]}\\
	\end{split}
\end{equation}
 \newpage
 \newpage
 \section{Propagation}
All programs and data for this section are available at\\ \href{https://github.com/eoricard/hetero-core/tree/main/Propagation}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/Propagation}}. 


Using Eq. \ref{eq:field2modes} for the interaction between  two modes in Region 2, we plot a density map of $|E(x,y,z,\lambda,n_3=1)|$. \\
\subsection{$A_1=1 , \ \lambda=750\ \text{nm}, \ n_3=1$}
 \begin{figure}[h!]
 	\centering
 	\includegraphics[width=\linewidth]{fig9_SI.pdf}
 	\caption{Density plots for the interaction between $HE_{11}$ and $HE_{12}$ modes in a coreless fiber with $\lambda=750\ \text{nm}$ and $n_3=1$ in the (z,y) and (x,y) planes.} 
 	\label{fig:propagation750}
 \end{figure}
 
 
 
 In the bottom of Fig. \ref{fig:propagation750}-SI we show 3 graphs of the transverse distribution in the  $(x,y)$ plane of the function  $|E(x,y,z=L,\lambda=750\ \text{nm},n_3=1)|$ for $L=0\ \text{mm}$, $L=7\ \text{mm}$, $L=14\ \text{mm}$. We observe the emergence of a disk at $L=0$ and a Gaussian profile centered at the origin for $L=14\ \text{mm}$.\\
 
\subsection{$A_1=1, \ \lambda=1550\ \text{nm}, \ n_3=1$}
 \begin{figure}[h!]
 	\centering
 	\includegraphics[width=\linewidth]{fig10_SI.pdf}
 	\caption{Density plots for the interaction between $HE_{11}^x$ and $HE_{12}^x$ modes in a coreless fiber with $\lambda=1550\ \text{nm}$ and $n_3=1$ in (z,y) and (x,y) planes.}
 	\label{fig:propagation1550}
 \end{figure}
 
 
  In the bottom of Fig. \ref{fig:propagation1550}-SI,  we show three graphs of the transverse distribution in the $(x,y)$ plane of the function  $|E(x,y,z=L,\lambda=1550\ \text{nm},n_3=1)|$ for $L=0\ \text{mm}$, $L=7\ \text{mm}$, $L=14\ \text{mm}$. We observe the emergence of a disk at $L = 0 $ mm and a Gaussian profile centered at the origin for $L = 7\ \text{mm}$.
  
  In conclusion, parameters such as the wavelength $\lambda$ and device length $L$ have a noticeable effect on the interference.
  
 \section{Integrated intensity}
 


Experimentally only the field coupled in the core of the second multimode fiber can be measured, so we calculate the intensity over the region  $\Omega=\{(x,y)\ |\ r\in (0,32.5\ \mu \text{m})\}$. 
  
Case 1: $P=H=1$
 \begin{equation}
 	\begin{split}
 		I(L,\lambda)=\left[A_{1}^2\eta_{11}^2 M_{11}^2 \iint_{\Omega} dxdy f_{11}(x,y)f_{11}^{*}(x,y)\right]^{1/2},		
 	\end{split}
 \end{equation}
 Note that in this case, there is not interference. 
 
Case 2: $P=H=2$
 \begin{equation}
 	\begin{split}
 		I(L,\lambda)=&
 		[A_1^2 \eta _{11} \eta _{1,2} M_{11} M_{12} e^{i L \beta _{12}-i L \beta _{11}}\iint_{\Omega}dxdy f_{12} f_{11}^*\\
 		+&A_1^2 \eta _{11} \eta _{1,2} M_{11} M_{12} e^{i L \beta _{11}-i L \beta _{12}} \iint_{\Omega} dxdy f_{11} f_{12}^*(x,y)\\ +& A_1^2 \eta _{11}^2 M_{11}^2\iint_{\Omega} dxdy f_{11} f_{11}^*+A_1^2 \eta _{12}^2 M_{12}^2\iint_{\Omega} dxdy f_{12} f_{12}^*]^{1/2}
 		\label{eq:intensity2modes}
 	\end{split}
 \end{equation}
In this case, the integrals are not orthonormal, i.e.,

 \begin{equation}
\iint_{\Omega}dx dy f_{1i}(x,y)f_{1j}^{*}(x,y) \neq \delta_{ij}.
 \end{equation}
 This is a consequence of integrating the functions over a restricted region, rather than over all space. Moreover, the intensity depends on the phase difference $ [\beta _{11}(\lambda)- \beta _{12}(\lambda)]L$
 
 
Case 3: $P=H=4$
 \begin{equation}
 	\begin{split}
	&I(\lambda,L,n_3)=[\iint_{\Omega}dx dy
	\{A_1^2 f_{12} f_{11}
^* \eta _{11} \eta _{12} M_{11} M_{12} e^{i L \beta _{12}-i L \beta _{11}}+A_1^2 f_{11} f_{12}^* \eta _{11} \eta _{12} M_{11} M_{12} e^{i L \beta _{11}-i L \beta _{12}}\\ 
	&+ A_2 A_1 f_{13}\ f_{11}^* \eta _{11} \eta _{23} M_{11} M_{13} e^{i L \beta _{13}-i L \beta _{11}}+A_2 A_1 f_{14} f_{11}^* \eta _{11} \eta _{24} M_{11} M_{14} e^{i L \beta _{14}-i L \beta _{11}}\\
	&+ A_2 A_1 f_{13} f_{12}^* \eta _{12} \eta _{23} M_{12} M_{13} e^{i L \beta _{13}-i L \beta _{12}}+A_2 A_1 f_{14} f_{12}^* \eta _{12} \eta _{24} M_{12} M_{14} e^{i L \beta _{14}-i L \beta _{12}}\\ 
	&+ A_2 A_1 f_{11} f_{13}^* \eta _{11} \eta _{23} M_{11} M_{13} e^{i L \beta _{11}-i L \beta _{13}}+A_2 A_1 f_{12} f_{13}^* \eta _{12} \eta _{23} M_{12} M_{13} e^{i L \beta _{12}-i L \beta _{13}}\\ 
	&+ A_2 A_1 f_{11} f_{14}^* \eta _{11} \eta _{24} M_{11} M_{14} e^{i L \beta _{11}-i L \beta _{14}}+A_2 A_1 f_{12} f_{14}^* \eta _{12} \eta _{24} M_{12} M_{14} e^{i L \beta _{12}-i L \beta _{14}}\\
	&+  A_2^2 f_{14} f_{13}^* \eta _{23} \eta _{24} M_{13} M_{14} e^{i L \beta _{14}-i L \beta _{13}}+ A_2^2 f_{13} f_{14}^* \eta _{23} \eta _{24} M_{13} M_{1,4} e^{i L \beta _{13}-i L \beta _{14}}\\ 
	&+ A_1^2 f_{11} f_{11}^* \eta _{11}^2 M_{11}^2+A_1^2 f_{12} f_{12}^* \eta _{12}^2 M_{12}^2+ A_2^2 f_{13} f_{13}^* \eta _{23}^2 M_{13}^2+A_2^2 f_{14} f_{14}^* \eta _{24}^2 M_{14}^2\}]^{1/2}
 	\end{split}
 	\label{eq:intensity4modes}
 \end{equation}
 
\newpage
\section{Spectral Interference}
All programs and data for this section are available at \\ \href{https://github.com/eoricard/hetero-core/tree/main/Interference}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/Interference}} 


\subsection{Dependence with the length of device $L$}

By using the Eq. \ref{eq:intensity2modes} with $A_1=1$ and $n_3=1$, we explore  the interference at the output of the device as function of the parameter $L$.
\begin{figure}[h]
	\centering
	\includegraphics[width=\linewidth]{fig11_SI.pdf}
	\caption{Spectral Interference I($\lambda,L,A_1$) for $L=7$ mm, $14$ mm and $ 28$ mm, with $A_1=1$, considering  the interaction between two modes.}
	\label{fig:longitud28}
\end{figure}

In this case, we observe the emergence of a minimum in transmission at $L=14\ \text{mm}$ near $1550\ \text{nm}$, which is consistent with Fig. \ref{fig:longitud28}-SI. When $L=28\ \text{mm}$, we observe the emergence of a second minimum near $800\  \text{nm}$.

\subsection{Dependence with the parameters $A_1$ and $A_2$}
By using the Eq. \ref{eq:intensity4modes} with $L=28\ \text{mm}$ and $n_3=1$, we explore  the interference at the output of device as function of the parameter $A_1$, with $A_2=\sqrt{1-A_1^2}$


\begin{figure}[h]
	\centering
	\includegraphics[width=\linewidth]{fig12_SI.pdf}
	\caption{Spectral Interference I($\lambda,L,A_1,A_2$), for $A_1=0,\ 0.25 ,\ 0.5 ,\ 0.75 ,\ 0.9$ and $\ 0.99$, with $A_2=\sqrt{1-A_1^2}$ considering the interaction between four modes.}
	\label{fig:amplitudes}
\end{figure}
With this exploration, we can conclude that our experiment can be explained by analyzing only the contribution of a single mode in the input, specifically $A_1=1$, $A_2=0$, that is, considering only the $\text{LP}_{01}$ mode at the device input.


\section{Semi-analytical solution}


All programs and data for this section are available at \\
\href{https://github.com/eoricard/hetero-core/tree/main/Semi-analytical}{\textcolor{blue}{https://github.com/eoricard/hetero-core/tree/main/Semi-analytical}}

A semi-analytical solution can be found for the interaction between the $\text{HE}_{11}$ and $\text{HE}_{12}$ modes in Region 2, as follows

Case $P=H=2$
\begin{equation}
	\begin{split}
		I(L,\lambda)=&
		[A_1^2 \eta _{11} \eta _{12} M_{11} M_{12} e^{i L \beta _{12}-i L \beta _{11}}\iint_{\Omega}dx dy f_{12} f_{11}^*\\
		+ & A_1^2 \eta _{11} \eta _{12} M_{11} M_{12} e^{i L \beta _{11}-i L \beta _{12}} \iint_{\Omega}dx dy f_{11} f_{12}^*\\ + & A_1^2 \eta _{11}^2 M_{11}^2\iint_{\Omega}dx dy f_{11} f_{11}^*+A_1^2 \eta _{12}^2 M_{12}^2\iint_{\Omega}dx dy f_{12} f_{12}^*]^{1/2}
	\end{split}
\end{equation}

\begin{equation}
	\label{eq:semi}
	\boxed{
	\begin{split}
		I(\lambda,L,n_3)=
		\{C_1+C_2+ 2C_3 \text{Cos}[L \Delta \beta(\lambda,n_3)]\}^{1/2}
	\end{split}}
\end{equation}

\begin{figure}[h]
	\centering
	\includegraphics[width=.6\linewidth]{fig13_SI.pdf}
	\caption{Density plot of I($\lambda,L$) with $A=1$ and $n_3=1$,  considering the semi-analytical solution Eq. \ref{eq:semi}.}
	\label{fig:L2d}
\end{figure}

In this analysis, we consider a linear approximation for the phase difference between the $HE_{11}$ and $HE_{12}$ modes, defined as:

\begin{equation}
	\Delta \beta(\lambda, n_3) = \beta_{11}(\lambda, n_3) - \beta_{12}(\lambda, n_3).
\end{equation}

This difference is approximated by a linear expression as a function of the wavelength $\lambda$:

\begin{equation}
	\Delta \beta(\lambda, n_3) \approx m(n_3)\lambda + b(n_3),
\end{equation}

\noindent where both the slope $m(n_3)$ and the intercept $b(n_3)$ depend on the external refractive index $n_3$.

For this model, the coefficient $A_1 = 1$ is considered, while the constants $C_1$, $C_2$, and $C_3$ take the following values:




\begin{equation}
\begin{split}
C_1=A_1^2\eta _{11}^2 M_{11}^2\iint_{\Omega}dx dy f_{11}(x,y) f_{11}^*(x,y)=0.175061.\\
C_2=A_1^2\eta _{12}^2 M_{12}^2\iint_{\Omega}dx dy f_{12}(x,y) f_{12}^*(x,y)=0.0856348.\\
C_3=A_1^2\eta _{11} \eta _{12} M_{11} M_{12}\iint_{\Omega}dx dy f_{12}(x,y) f_{11}^*(x,y) =-0.10259.\\
\end{split}
\end{equation}


\begin{figure}[h!]
	\centering
	\includegraphics[width=1\linewidth]{fig14_SI.pdf}
	\caption{Spectral interference I($\lambda,n_3$) with $A=1$, $L=28000\ \mu \text{m}$ and $n_3=1,\ 1.1,\ 1.2,\ 1.3$, and $1.4$, considering the semi-analytical solution Eq. \ref{eq:semi}.}
	\label{fig:index}
\end{figure}

The minimum of Eq. \ref{eq:semi} can be found by applying the conditions that the first derivative vanishes,
$\frac{d I(\lambda)}{d\lambda} = 0$,
and the second derivative is positive,
$\frac{d^2 I(\lambda)}{d\lambda^2} > 0$.
These lead to the relation:

\begin{equation}
	L(m\lambda_{\text{min}} + b) = 2\pi N, \quad N = 1, 2, \dots
\end{equation}

Neglecting the contribution of the term $\frac{b}{L}$, the first minimum corresponds to
$\lambda_{\text{min},1} = \frac{2\pi}{mL}$,
and the second to
$\lambda_{\text{min},2} = \frac{4\pi}{mL}$.
The positions of the minima are shown in Table \ref{Table:minimum}.



\begin{table}[h!]
	\caption{Values of the linear fit to the difference phases $\beta_{11}(\lambda)-\beta_{12}(\lambda)\approx m\lambda+b$, for five values of index refraction $n_3$, together with the minimum for $L=28000\ \mu \text{m}$.}
	\begin{center}
		\begin{tabular}{|c|c|c|c|c|}
			\hline
			$n_3$ & $m$ [$\mu \text{m}^{-2}$] &$b$ [$\mu \text{m}^{-1}$] & $\lambda_{\text{min},1}\approx \frac{2\pi}{mL}$ [$ \mu \text{m}$] & $\lambda_{\text{min},2}\approx \frac{4\pi}{mL}$ [$ \mu \text{m}$]\\
			\hline
			\hline
			1 & 0.0002766 & -1.75845019$\times 10^{-6}$ & 0.783 &  1.566 \\
			\hline
			1.1 &  0.0002762 & -1.5237094$\times 10^{-6}$  &0.784 & 1.568 \\
			\hline
			1.2 &  0.0002755 &-1.1568377$\times 10^{-6}$  &0.786 & 1.572 \\
			\hline
			1.3 &0.0002743 & -4.5654432$\times 10^{-7}$ &0.789 & 1.579 \\
			\hline
			1.4 & 0.0002700 & 2.10136618$\times 10^{-6}$ & 0.802 & 1.604\\
			\hline			
		\end{tabular}
		\label{Table:minimum}
	\end{center}
\end{table}

\section{Polarization.}
 \textcolor{red}{In Region 2 the linear polarized field cavity  $\textbf{E}_{cav}(r;\lambda)$ can be write as
\begin{equation}
	\begin{split}
	\textbf{E}_{cav}(x,y,z=L;\lambda)=\hat{\textbf{e}}_{x}\gamma_x
	\sum_{h=1}^{H}\sum_{p=1}^{P}A_{p}^x\eta_{ph}^x M_{1h}^x f_{1h}^x (x,y)e^{i[\beta_{1h}^x(\lambda)L]} \\ +\hat{\textbf{e}}_{y}\gamma_y
	\sum_{h=1}^{H}\sum_{p=1}^{P}A_{p}^y\eta_{ph}^y M_{1h}^y f_{1h}^y (x,y)e^{i[\beta_{1h}^y(\lambda)L]}
	\end{split}
\end{equation}
where $(\gamma_x)^2+(\gamma_y)^2=1$.\\
Case  $P=H=2$
\begin{equation}
	\begin{split}
		E_{cav}(x,y,z=L:\lambda)=\hat{\textbf{e}}_{x}\gamma_x\left(A_{1}^x\eta_{11}^x M_{11}^x f_{11}^x(x,y)e^{i[\beta_{11}^x(\lambda)L]}+A_{1}^x\eta_{12}^xM_{12}^x f_{12}^x(x,y)e^{i[\beta_{12}^x(\lambda)L]}\right),\\
		+\hat{\textbf{e}}_{y}\gamma_y\left(A_{1}^y\eta_{11}^y M_{11}^y f_{11}^y(x,y)e^{i[\beta_{11}^y(\lambda)L]}+A_{1}^y\eta_{12}^y M_{12}^y f_{12}^y(x,y)e^{i[\beta_{12}^y(\lambda)L]}\right),
	\end{split}
\end{equation}
}



\begin{figure}[h]
	\centering
	\includegraphics[width=\linewidth]{fig15_SI.pdf}

	\caption{Polarized modes in the first row  $\text{HE}_{11}^x$,$\text{HE}_{11}^y$,$\frac{1}{\sqrt{2}}\text{HE}_{11}^x+\frac{1}{\sqrt{2}}\text{HE}_{11}^x$ and in the second row	$\text{HE}_{12}^y$, $\text{HE}_{12}^y$, $\frac{1}{\sqrt{2}}\text{HE}_{11}^y+\frac{1}{\sqrt{2}}\text{HE}_{11}^y$. }
	\label{fig:polarizacionmodos}
\end{figure}

\textcolor{red}{
the intensity is
\begin{equation}
	I(\lambda,L,n_3=1)=
\{\gamma_x(C_1+C_2+ 2C_3 \text{Cos}[L \Delta \beta^x(\lambda)])+\gamma_y(C_1+C_2+ 2C_3 \text{Cos}[L \Delta \beta^y(\lambda)])\}^{1/2}
\end{equation}
where $ \Delta\beta^x=\beta_{11}^x-\beta_{12}^x\approx 0.000281 [\mu m]^{-1}$ and $ \Delta\beta^y=\beta_{11}^y-\beta_{12}^y\approx 0.000337 [\mu m]^{-1}$\\
Fig.\ref{fig:polarizacionmodos} shows vectorial distribution of modes HE$_11$ ,HE$_12$ and three configuration of polarization states.\\ 
The effects of polarization for three different states over spectral interference, along with their comparison to the experimental spectra, are shown in the Fig.\ref{fig:polarization} .}
\begin{figure}[h]
	\centering
	\includegraphics[width=15cm]{fig16_SI.pdf}
	\caption{Interference patterns for three representative linear polarization states  vertical (red), horizontal (blue), and  diagonal (black) )) and experimental data (green). With $P=H=2,n_3=1$, $A_1=A_2=1$} 
	\label{fig:polarization}
\end{figure}

\section{Conclusion}
In conclusion, we explore the effect of all the variables involved in the interference, which are:
i) wavelength $\lambda$,	
ii) length of device $L$,
iii) index refraction external $n_3$,
iv) number and amplitude of modes in Region 1, $P, A_1,A_2,...$,  and
v) number and amplitude of modes in Region 2, $H, B_1,B_2,...$.
We also present a semi-analytical solution for the case of $P=H=2$ modes.


\section*{References}
\begin{thebibliography}{1}
	\bibliographystyle{IEEEtran}
	
	\bibitem{Agrawal_2013}
	G. P. Agrawal, “Nonlinear fiber optics,” \textit{Academic Press}, 2012.
	
	\bibitem{Saleh_1991}
	B. E. A. Saleh and M. C. Teich, “Guided‐Wave Optics,” in \textit{Fundamentals of Photonics}, 1991, pp. 238–271. doi: 10.1002/0471213748.ch7.

\end{thebibliography}
\end{document}


