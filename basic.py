import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def E(I, theta):
    """
    Blackbody Emissive Power: Cosine Law Dependence

    Blackbody intensity is isotropic, this means that the blackbody emissive
    power is a maximum if the surface is normal to a receiving surface.

    E: Emissive Power
    I: Intensity
    """

    return I*np.cos(np.deg2rad(theta))

def PlanckLaw(lamda, T, theta=None):
    """
    Planck's law is to express the spectral distribution of hemispherical
    emissive power and radiant intensity in vacuum.

    lamda: lambda, um
    T: Temperature, K
    theta: degree
    """

    C1 = 0.59552e8
    C2 = 14388
    n = 1.0
    
    I = 2*C1/n**2/lamda**5/(np.exp(C2/(n*lamda*T))-1)
    E = np.pi * I

    if theta is None:
        return I, E
    else:
        return I, E, I*np.cos(np.deg2rad(theta))

def WeinDisplacementLaw(wavelength=None, T=None):
    const = 2897.8
    if wavelength is not None and T is None:
        return const / wavelength
    elif wavelength is None and T is not None:
        return const / T

def PlanckLawFigure():
    Ts = (300, 1000, 2000, 3000, 5000, 5762)
    lamdas = np.linspace(0.1, 5, 1000)
    Es = []
    for T in Ts:
        Es.append(PlanckLaw(lamda=lamdas, T=T)[1])

    for E in Es:
        plt.plot(lamdas, E)
    plt.yscale('log')
    plt.show()

def StefanBoltzmannLaw(T):
    sigma = 5.67e-8
    return sigma * T**4

def BouguerLaw(beta, S, I_0):
    """
    beta: a function of $beta(\lambda)$
    """
    I_S = I_0 * np.exp(-quad(beta, 0, S))
    return I_S




