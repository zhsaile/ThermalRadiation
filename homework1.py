from basic import *

c = 3e8

def q1():
    visible_spectrum = np.array([0.4e-6, 0.7e-6])
    wave_numbers = np.flip(1 / visible_spectrum)
    visible_frequency = np.flip(c / visible_spectrum)
    print('wave numbers:\t', wave_numbers)
    print('visible_frequency:\t', visible_frequency)

def q2():
    wavelength = 1.633e-6
    velocity = 2.6e8
    refractive_index = c / velocity
    f = velocity / wavelength
    wavelength_vacuum = c / f

    print(f'The refractive index of the medium is: {refractive_index:.3f}')
    print(f'The wavelength of this radiation if it propagates into a vacuum is: {wavelength_vacuum*1e6:.3f}um')

def q5():
    T = 1350
    wavelength = 4
    I, _ = PlanckLaw(wavelength, T)
    print('The spectral intensity emitted in a direction normal to the surface is: ')
    print(f'{I:.2f} W/(m2*um*Sr)')

    print('The spectral intensity emitted at theta=50 degree is: ')
    print(f'{I:.2f} W/(m2*um*Sr)')

    E_50 = I * np.cos(np.deg2rad(50))
    print('The directional spectral emissive power at theta=50 degree is:')
    print(f'{E_50:.2f} W/(m2*um*Sr)')

    wavelength_max = WeinDisplacementLaw(T=1350)
    print(f'At λ = {wavelength_max:.2f}um the blockbody emitted the maximum spectral intensity.')
    I, _ = PlanckLaw(wavelength_max, 1350)
    print(f'The intensity is: {I:.2f} W/(m2*um*Sr)')

    E_total = StefanBoltzmannLaw(T)
    print(f'The hemispherical total emissive power of the blackbody is: {E_total/1e3:.2f} kW/m2')

def q6():
    T = 2450
    wavelength_max = WeinDisplacementLaw(T)
    I, _ = PlanckLaw(lamda=wavelength_max, T=T)
    print(f'The maximum emitted spectral intensity is: {I/1e3:.2f} kW/(m2*um*Sr)')
    E_total = StefanBoltzmannLaw(T)
    print(f'The hemispherical total emissive power is : {E_total/1e3:.2f} kW/m2')

def q8():
    T = 5780

    wavelength_max = WeinDisplacementLaw(T)
    print('At what wavelength and frequency is the maximum energy per unit wavelength emitted?')
    print(f'{wavelength_max:.2f}um, {3e8/wavelength_max/1e-6:.2e}Hz')
    
    _, E = PlanckLaw(wavelength_max, T)
    print('What is the maximum value of the solar hemispherical spectral emissive power?')
    print(f'{E:.2e} W/(m2*um)')

def q9():
    


