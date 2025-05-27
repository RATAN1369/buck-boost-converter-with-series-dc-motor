import numpy as np
import matplotlib.pyplot as plt

# Parameters
Vin = 24          # Input voltage in volts
Vout = -12        # Output voltage in volts (buck-boost gives negative output)
D = 0.33          # Duty cycle (0 < D < 1)
L = 100e-6        # Inductance in henries
T = 100e-6        # Switching period in seconds
fs = 1 / T        # Switching frequency in Hz
IL_avg = 5        # Average inductor current in A

# Time intervals
t_on = D * T
t_off = (1 - D) * T

# Time array for plotting (1 full cycle)
t = np.linspace(0, T, 1000)

# Inductor current waveform
iL = np.zeros_like(t)

# Peak-to-peak ripple current
delta_IL = (Vin * D * T) / L

# Current at the start of cycle (min current)
IL_min = IL_avg - delta_IL / 2
IL_max = IL_avg + delta_IL / 2

# Fill waveform values
for i in range(len(t)):
    if t[i] <= t_on:
        iL[i] = IL_min + (Vin / L) * t[i]  # increasing during ON
    else:
        iL[i] = IL_max + ((Vout) / L) * (t[i] - t_on)  # decreasing during OFF

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(t * 1e6, iL, label='Inductor Current', color='blue')
plt.axhline(IL_avg, color='gray', linestyle='--', label='Average Current')
plt.axhline(IL_min, color='red', linestyle=':', label='Min Current')
plt.axhline(IL_max, color='green', linestyle=':', label='Max Current')

plt.title('Buck-Boost Converter Inductor Current Waveform')
plt.xlabel('Time (μs)')
plt.ylabel('Inductor Current (A)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
