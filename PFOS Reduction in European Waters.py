### File 1
import numpy as np
import matplotlib.pyplot as plt

def pfos_decay(C0, k, t):
    """Model for PFOS decay over time.
    C0: Initial concentration
    k: Decay constant (rate of reduction)
    t: Time (years)"""
    return C0 * np.exp(-k * t)

initial_concentration = 10
safe_limit_freshwater = 6.5e-4  
safe_limit_coastal = 1.35e-4  

years = np.arange(0, 110, 1)
decay_rate_10 = -np.log(0.9)
decay_rate_20 = -np.log(0.8)  

pfos_10 = pfos_decay(initial_concentration, decay_rate_10, years)
pfos_20 = pfos_decay(initial_concentration, decay_rate_20, years)

plt.figure(figsize=(10, 6))
plt.plot(years, pfos_10, label='10% Annual Reduction')
plt.plot(years, pfos_20, label='20% Annual Reduction')
plt.axhline(safe_limit_freshwater, color='green', linestyle='--', label='Safe Limit (Freshwater)')
plt.axhline(safe_limit_coastal, color='blue', linestyle='--', label='Safe Limit (Coastal)')

plt.yscale('log')
plt.xlabel('Years')
plt.ylabel('PFOS Concentration (µg/L)')
plt.title('Projected PFOS Reduction in European Waters')
plt.legend()
plt.grid(True)
plt.show()

### File 2
import numpy as np
import matplotlib.pyplot as plt

permafrost_area_km2 = 22.79e6
thawed_fraction = 0.25
initial_pfas_concentration = 0.01  
annual_reduction_rate = 0.20

def pfas_permafrost_release(C0, k, years):
    """Calculate PFAS release over time from thawing permafrost."""
    return C0 * (1 - np.exp(-k * years))

# Simulate 30 years of reduction
years = np.arange(0, 30, 1)
pfas_concentration = initial_pfas_concentration * np.exp(-annual_reduction_rate * years)
pfas_release = thawed_fraction * permafrost_area_km2 * pfas_concentration

# Carbon Sequestration Model
baseline_carbon_sequestration = 50
pfas_impact_factor = 0.1  
carbon_sequestration = baseline_carbon_sequestration * (1 - pfas_impact_factor * np.exp(-annual_reduction_rate * years))

# Bioaccumulation Model
initial_pfas_prey = 0.5  
bioaccumulation_factor = 10
pfas_predator = initial_pfas_prey * bioaccumulation_factor * np.exp(-annual_reduction_rate * years)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(years, pfas_release, label='PFAS Released from Thawing Permafrost')
plt.title('PFAS Release from Thawing Permafrost')
plt.xlabel('Years')
plt.ylabel('Released PFAS (µg)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(years, carbon_sequestration, label='Marine Carbon Sequestration Efficiency')
plt.title('Impact of PFAS Reduction on Carbon Sequestration')
plt.xlabel('Years')
plt.ylabel('Carbon Sequestration Efficiency (%)')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(years, pfas_predator, label='PFAS in Marine Predators')
plt.title('PFAS Bioaccumulation in Predators')
plt.xlabel('Years')
plt.ylabel('PFAS Concentration (µg/kg)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
