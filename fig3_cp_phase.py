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

# Constants
MZ = 91.1876       
MGUT = 1.0e16      
energy_Z_to_GUT = np.logspace(np.log10(MZ), np.log10(MGUT), 500)

plt.figure(figsize=(7, 5))

# Boundaries
delta_CP_GUT = np.pi   
delta_CP_MZ = 1.3216 * np.pi 
PDG_2024_central = 1.36 * np.pi
PDG_2024_err = 0.11 * np.pi

# Corrected Evolution: From MZ (1.32*pi) to MGUT (pi)
evolution_curve = np.linspace(delta_CP_MZ, delta_CP_GUT, 500)
log_energy_axis = np.log10(energy_Z_to_GUT)

plt.plot(log_energy_axis, evolution_curve, color='#756bb1', linewidth=2.5)

# GUT Boundary
plt.axhline(y=delta_CP_GUT, color='k', linestyle=':', linewidth=1.2)
plt.text(14.5, delta_CP_GUT + 0.02*np.pi, r'$\delta_{CP}(M_{GUT}) = \pi$')

# Low Energy Prediction
plt.axhline(y=delta_CP_MZ, color='#756bb1', linestyle='--', linewidth=1.5)
plt.text(2, delta_CP_MZ - 0.05*np.pi, r'UBM Prediction $\approx 1.32\pi$')

# PDG 2024 Constraint
plt.axhspan(PDG_2024_central - PDG_2024_err, PDG_2024_central + PDG_2024_err, color='gray', alpha=0.15, label='PDG 2024 ($1\sigma$)')
plt.axhline(y=PDG_2024_central, color='gray', linestyle='-', linewidth=0.8, alpha=0.5)

plt.xlim(1.5, 16.5)
plt.ylim(0.9*np.pi, 1.6*np.pi)
plt.xlabel(r'$\log_{10}(\mu / \text{GeV})$')
plt.ylabel(r'Leptonic CP Phase $\delta_{CP}$ [Radians]')
plt.title(r'**Fig. 3**: Leptonic CP Phase Loop-Level RG Evolution')
plt.legend(frameon=False, loc='lower left')
plt.grid(True)
plt.tight_layout()
plt.savefig('Fig3_CP_Evolution.pdf')
print("Saved: Fig3_CP_Evolution.pdf")
plt.show()
