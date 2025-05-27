# Buck-Boost Converter Inductor Voltage Waveform over 3 periods
import numpy as np
import matplotlib.pyplot as plt

# Parameters
Vin = 12             # Input voltage in volts
D = 0.4              # Duty cycle (0 < D < 1)
T = 1e-5             # Switching period in seconds
L = 100e-6           # Inductance in Henry
fs = 1/T             # Switching frequency in Hz
time_resolution = 1e-8  # Time resolution for plotting
periods = 3          # Number of switching periods to simulate

# Time vector for 3 periods
t = np.arange(0, periods * T, time_resolution)

# Initialize inductor voltage waveform
vL = np.zeros_like(t)

# Calculate waveform for each period
for i in range(periods):
    t_start = i * T
    on_time = t_start + D * T
    off_time = t_start + T

    # Find indices for on and off time in each period
    on_indices = (t >= t_start) & (t < on_time)
    off_indices = (t >= on_time) & (t < off_time)

    vL[on_indices] = Vin
    vL[off_indices] = - (Vin * D / (1 - D))  # Steady-state condition: average voltage across inductor = 0

# Plotting
plt.figure(figsize=(12, 5))
plt.plot(t * 1e6, vL, label='Inductor Voltage $V_L(t)$', color='blue')
plt.axhline(0, color='black', linestyle='--')
plt.title('Buck-Boost Inductor Voltage over 3 Switching Cycles')
plt.xlabel('Time (µs)')
plt.ylabel('Inductor Voltage $V_L$ (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
