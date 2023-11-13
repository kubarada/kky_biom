import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import simulation

# parametry
mu = 1.0
# čas
t = np.linspace(0, 50, 500)

# počáteční podmínky
x0 = [1.0, 0.0]


sol_no_stim = odeint(simulation.van_der_pol_oscillator_no_stim, x0, t, args=(mu,))

plt.plot(t, sol_no_stim[:, 0])
plt.xlabel('t [s]')
plt.ylabel(r'$x_1(t)$')
plt.grid()
plt.title('Činnost srdce simulována Van der Polovým modelem')
plt.show()
