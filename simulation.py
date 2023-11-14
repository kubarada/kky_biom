import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Van der Pol oscilátor --> reprezentace diff.rovnicí
def van_der_pol_oscillator_no_stim(x, t, mu):
    x1, x2 = x
    dxdt = [x2, mu*(1 - x1**2)*x2 - x1]
    return dxdt

# Van der Pol oscilátor --> přidání arytmie
def van_der_pol_arrhythmia(x, t, mu, arrhythmia_factor):
    x1, x2 = x
    mu += arrhythmia_factor * np.sin(0.5 * t)
    dxdt = [x2, mu*(1 - x1**2)*x2 - x1]
    return dxdt

def van_der_pol_arrhythmia_stimulator(x, t, mu, arrhythmia_factor, I):
    x1, x2 = x
    # Introduce arrhythmia by adding a time-varying factor to the mu parameter
    mu += arrhythmia_factor * np.sin(0.5 * t)
    dxdt = [x2, mu*(1 - x1**2)*x2 - x1 + I(t)]
    return dxdt

# Cardiac stimulator function
def cardiac_stimulator(t):
    # Simple stimulator: periodic pulses
    if t % 5 == 0:  # Stimulate at a regular interval (e.g., every 10 seconds)
        return 10  # Strength of the stimulation
    else:
        return 0

def van_der_pol_cardiac_arrest(x, t, mu, arrest_time):
    x1, x2 = x
    if t >= arrest_time:
        # Simulate cardiac arrest by setting the system to a stable state
        dxdt = [0, 0]
    else:
        dxdt = [x2, mu*(1 - x1**2)*x2 - x1]
    return dxdt

def van_der_pol_defibrillator(x, t, mu, arrest_time, defib_time, defib_strength):
    x1, x2 = x
    if t > arrest_time:
        # Simulate cardiac arrest
        dxdt = [0, 0]
        if t > defib_time:
            # Simulate defibrillation
            dxdt = [defib_strength, 0]
    else:
        dxdt = [x2, mu*(1 - x1**2)*x2 - x1]
    return dxdt
