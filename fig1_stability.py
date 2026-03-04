import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Journal Style Configuration
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 11
rcParams['axes.linewidth'] = 1.0
rcParams['lines.linewidth'] = 1.8
rcParams['grid.alpha'] = 0.5
rcParams['xtick.direction'] = 'in'
rcParams['ytick.direction'] = 'in'

# Core Constants
XI = -1.21e-12 
f = 0.5  # Normalized M_P^2/2
X_energy_range = np.logspace(-15, 0, 500) 

plt.figure(figsize=(7, 5))

# Derived Stability Parameter Q(X)
A3 = XI
A4 = -(A3**2) / (4*f)
Q_eigenvalue = (A3**2 * X_energy_range) / (4*f) + A4 + (3 * (A3/2)**2) / (2*f + 3 * X_energy_range * A3)

plt.semilogx(X_energy_range, Q_eigenvalue, color='#31a354', linewidth=2.2)

# Stability boundary
plt.axhline(y=0, color='r', linestyle='--', linewidth=1.5)
plt.fill_between(X_energy_range, 0, Q_eigenvalue, color='#31a354', alpha=0.15)

# Limits and labels
stability_min_display = np.min(Q_eigenvalue)
plt.xlim(1e-15, 1.0)
plt.ylim(-1e-25, 1.5e-24) 
plt.xlabel(r'Kinetic Density $X$ [$\nabla \mathcal{B} \nabla \mathcal{B} / M_P^4$]')
plt.ylabel(r'Stability Parameter $Q(X)$ [$M_P^2$]')
plt.title(r'**Fig. 1**: DHOST Class Ia Kinetic Stability Domain')
plt.text(1e-14, stability_min_display + 1e-25, r'$Q_{min} \approx 3.66 \times 10^{-25}$ $M_P^2$', color='#31a354')
plt.grid(True, which="both", ls="-", alpha=0.3)
plt.tight_layout()
plt.savefig('Fig1_DHOST_Stability.pdf')
print("Saved: Fig1_DHOST_Stability.pdf")
plt.show()
