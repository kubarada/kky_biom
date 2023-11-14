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

# graf bez stimulace
plt.plot(t, sol_no_stim[:, 0])
plt.xlabel('t [s]')
plt.ylabel(r'$x_1(t)$')
plt.grid()
plt.title('Činnost srdce simulována Van der Polovým modelem')
plt.show()

sol_arrhythmia = odeint(simulation.van_der_pol_arrhythmia, x0, t, args=(mu, arrhythmia_factor))

# Plot results with arrhythmia simulation
plt.plot(t, sol_arrhythmia[:, 0])
plt.xlabel('t [s]')
plt.ylabel(r'$x_1(t)$')
plt.grid()
plt.title('Činnost srdce s arytmií simulována Van der Polovým modelem')
plt.show()

sol_arrhythmia_stimulator = odeint(simulation.van_der_pol_arrhythmia_stimulator, x0, t, args=(mu, arrhythmia_factor, simulation.cardiac_stimulator))

# Plot results with arrhythmia and stimulator
plt.plot(t, sol_arrhythmia_stimulator[:, 0])
plt.xlabel('t [s]')
plt.grid()
plt.ylabel(r'$x_1(t)$')  # Using LaTeX for the y-axis label
plt.title('Činnost srdce s arytmií regulována kardiostimulátorem')
plt.show()

sol_cardiac_arrest = odeint(simulation.van_der_pol_cardiac_arrest, x0, t, args=(mu, arrest_time))

# Plot results with cardiac arrest simulation
plt.plot(t, sol_cardiac_arrest[:, 0])
plt.xlabel('t [s]')
plt.ylabel(r'$x_1(t)$')
plt.grid()
plt.title('Srdeční zástava')
plt.show()

# Solve ODE with cardiac arrest and defibrillator
sol_defibrillator = odeint(simulation.van_der_pol_defibrillator, x0, t, args=(mu, arrest_time, defib_time, defib_strength))

# Plot results with cardiac arrest and defibrillator
plt.plot(t, sol_defibrillator[:, 0])
plt.xlabel('t [s]')
plt.ylabel(r'$x_1(t)$')
plt.grid()
plt.xlim([0, 35])
plt.ylim([-2, 10])
plt.title('Defibrilace po srdeční zástavě')
plt.show()