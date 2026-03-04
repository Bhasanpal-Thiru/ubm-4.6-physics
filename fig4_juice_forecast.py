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

def simulate_juice_doppler(peak_shift=1.84e-8, noise_floor=2e-10):
    """
    Simulates Doppler residual for JUICE EGA-2 (Sept 2026).
    """
    # Time window: -30 to +30 mins from perigee (in seconds)
    t = np.linspace(-1800, 1800, 1000) 
    
    # Predicted UBM asymmetric blue-shift profile
    signal = peak_shift * np.exp(-(t - 420)**2 / (2 * 300**2)) 
    
    # Add Ka-band tracking noise
    noise = np.random.normal(0, noise_floor, len(t))
    total_obs = signal + noise
    
    return t, total_obs, signal

plt.figure(figsize=(7, 5))

t, obs, clean_signal = simulate_juice_doppler()

plt.plot(t/60, obs * 1e9, label='Simulated Ka-band Residual + Noise', color='blue', alpha=0.4)
plt.plot(t/60, clean_signal * 1e9, label='UBM 4.6 Theoretical Signal', color='darkblue', linewidth=2)

plt.axhline(0, color='black', linestyle='--', alpha=0.8)
plt.axvline(0, color='red', linestyle=':', alpha=0.8, label='Perigee ($h_p \\approx 50,000$ km)')

plt.xlim(-30, 30)
plt.ylim(-5, 25)
plt.xlabel(r'Time from Perigee [Minutes]')
plt.ylabel(r'Frequency Shift $\Delta f$ [nHz]')
plt.title(r'**Fig. 4**: JUICE EGA-2 Doppler Forecast (Sept 29, 2026)')
plt.legend(frameon=False, loc='upper left')
plt.grid(True, which='both', linestyle=':', alpha=0.5)
plt.tight_layout()
plt.savefig('Fig4_JUICE_Forecast.pdf')
print("Saved: Fig4_JUICE_Forecast.pdf")
plt.show()
