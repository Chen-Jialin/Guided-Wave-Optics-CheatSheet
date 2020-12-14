import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

# Page 15 Figure 1.6
# Reflection coefficient at a planer boundary between two dielectric media with n_1=1.0 and n_2=1.5
n_1 = 1.0
n_2 = 1.5
phi_1 = np.linspace(0, 90, 10000) # incident angle (unit: degree)
# TE (s) wave
Gamma_perp = (n_1 * np.cos(phi_1 * pi / 180) - np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2)) / (n_1 * np.cos(phi_1 * pi / 180) + np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2)) # TE wave reflection coefficient
plt.plot(phi_1, Gamma_perp, 'k-')
# TM (p) wave
Gamma_parallel = (n_2**2 * np.cos(phi_1 * pi / 180) - n_1 * np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2)) / (n_2**2 * np.cos(phi_1 * pi / 180) + n_1 * np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2)) # TM wave reflection coefficient
plt.plot(phi_1, Gamma_parallel, 'k--')
plt.xlim(0, 90)
plt.ylim(-1, 1)
plt.xlabel('$\phi_1~/~^{\circ}$', {'size': 16})
plt.ylabel('$\Gamma$', {'size': 16})
plt.legend(['$\Gamma_{\perp}$', '$\Gamma_{\parallel}$'])
plt.title('$n_1=1.0$, $n_2=1.5$')
plt.grid()
plt.show()

# Page 15 Figure 1.7
# Amplitude of reflection coefficient at a planar boundary between two dielectric media with n_1=1.5 and n_2=1.0
n_1 = 1.5 + 0j
n_2 = 1.0 + 0j
# TE (s) wave
Gamma_perp_abs = np.abs((n_1 * np.cos(phi_1 * pi / 180) - np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2)) / (n_1 * np.cos(phi_1 * pi / 180) + np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2))) # TE wave reflection coefficient absolute value
plt.plot(phi_1, Gamma_perp_abs, 'k-')
# TM (p) wave
Gamma_parallel_abs = np.abs((n_2**2 * np.cos(phi_1 * pi / 180) - n_1 * np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2)) / (n_2**2 * np.cos(phi_1 * pi / 180) + n_1 * np.sqrt(n_2**2 - n_1**2 * np.sin(phi_1 * pi / 180)**2))) # TM wave reflection coefficient absolute value
plt.plot(phi_1, Gamma_parallel_abs, 'k--')
plt.xlim(0, 90)
plt.ylim(0, 1.01)
plt.xlabel('$\phi_1~/~^{\circ}$', {'size': 16})
plt.ylabel('$|\Gamma|$', {'size': 16})
plt.legend(['$|\Gamma_{\perp}|$', '$|\Gamma_{\parallel}|$'])
plt.title('$n_1=1.5$, $n_2=1.0$')
plt.grid()
plt.show()

# Page 16 Figure 1.8
# Phase of reflection coefficient at a planar boundary between two dielectric media with n_1=1.5 and n_2=1.0
n_1 = 1.5 + 0j
n_2 = 1.0 + 0j
# TE (s) wave
Phi_perp = np.arctan(np.sqrt(n_1**2 * np.sin(phi_1 * pi / 180)**2 - n_2**2) / (n_1 * np.cos(phi_1 * pi / 180))) * 180 / pi # TE wave reflection phase
plt.plot(phi_1, Phi_perp, 'k-')
# TM (s) wave
Phi_parallel = np.real(np.arctan(n_1 * np.sqrt(n_1**2 * np.sin(phi_1 * pi / 180)**2 - n_2**2) / (n_2**2 * np.cos(phi_1 * pi / 180)))) * 180 / pi # TM wave reflection phase
Phi_parallel[Phi_parallel == 0.] = 90
plt.plot(phi_1, Phi_parallel, 'k--')
plt.xlim(0, 90)
plt.ylim(0, 90.5)
plt.xlabel('$\phi_1~/~^{\circ}$', {'size': 16})
plt.ylabel('$\Phi~/~^{\circ}$', {'size': 16})
plt.legend(['$\Phi_{\perp}$', '$\Phi_{\parallel}$'])
plt.title('$n_1=1.5$, $n_2=1.0$')
plt.grid()
plt.show()