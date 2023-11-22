import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import simulation

# parametry
mu = 1.0
t = np.linspace(0, 50, 500)
x0 = [1.0, 0.0]
arrhythmia_factor = 0.5
arrest_time = 25
defib_time = 30
defib_strength = 2

sol_no_stim = odeint(simulation.van_der_pol_oscillator_no_stim, x0, t, args=(mu,))

plt.plot(t, sol_no_stim[:, 0])
plt.xlabel('t [s]')
plt.ylabel('U[mV]')
plt.grid()
plt.title('Činnost srdce simulována Van der Polovým modelem')
plt.show()

sol_arrhythmia = odeint(simulation.van_der_pol_arrhythmia, x0, t, args=(mu, arrhythmia_factor))

plt.plot(t, sol_arrhythmia[:, 0])
plt.xlabel('t [s]')
plt.ylabel('U[mV]')
plt.grid()
plt.title('Činnost srdce s arytmií simulována Van der Polovým modelem')
plt.show()

sol_arrhythmia_stimulator = odeint(simulation.van_der_pol_arrhythmia_stimulator, x0, t, args=(mu, arrhythmia_factor, simulation.cardiac_stimulator))

plt.plot(t, sol_arrhythmia_stimulator[:, 0])
plt.xlabel('t [s]')
plt.grid()
plt.ylabel('U[mV]')
plt.title('Činnost srdce s arytmií regulována kardiostimulátorem')
plt.show()

plt.plot(t, sol_no_stim[:, 0], label = 'Zdravá srdeční činnost')
plt.plot(t, sol_arrhythmia_stimulator[:, 0], label = 'Regulovaná srdeční činnost')
plt.xlabel('t [s]')
plt.grid()
plt.legend(loc = 'upper right')
plt.ylabel('U [mV]')
plt.title('Srovnání zdravé srdeční činnosti s regulovanou')
plt.show()


sol_cardiac_arrest = odeint(simulation.van_der_pol_cardiac_arrest, x0, t, args=(mu, arrest_time))

plt.plot(t, sol_cardiac_arrest[:, 0])
plt.xlabel('t [s]')
plt.ylabel('U[mV]')
plt.grid()
plt.title('Srdeční zástava')
plt.show()

sol_defibrillator = odeint(simulation.van_der_pol_defibrillator, x0, t, args=(mu, arrest_time, defib_time, defib_strength))

plt.plot(t, sol_defibrillator[:, 0])
plt.xlabel('t [s]')
plt.ylabel('U[mV]')
plt.grid()
plt.xlim([0, 35])
plt.ylim([-2, 10])
plt.title('Defibrilace po srdeční zástavě')
plt.show()