import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Van der Pol oscilátor --> reprezentace diff.rovnicí
def van_der_pol_oscillator_no_stim(x, t, mu):
    x1, x2 = x
    dxdt = [x2, mu*(1 - x1**2)*x2 - x1]
    return dxdt
