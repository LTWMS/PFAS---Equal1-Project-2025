## Code written by Bryan CHan
import numpy as np
import matplotlib.pyplot as plt
from qutip import (basis, mesolve, sigmax, sigmaz, qeye)

def simulate_bond(omega, Omega_Rabi, omega_drive, tlist):
    """
    Returns the time evolution of ground- and excited-state populations
    for a simplified, two-level 'bond' under a time-dependent driving field.
    
    Parameters:
    -----------
    omega       : float
        The 'bond frequency' (energy gap) in radians/sec.
    Omega_Rabi  : float
        strength of the driving amplitude (Rabi frequency).
    omega_drive : float
        The driving frequency for the external probe (driving field).
    tlist       : array-like
        Array of time points for simulation.
    
    Returns:
    --------
    (pop_g, pop_e): tuple of arrays
        Ground and excited-state populations as functions of time.
    """
    # Pauli operators
    sx = sigmax()
    sz = sigmaz()
    # Identity on 2D space
    eye2 = qeye(2)

    # Define the two-level basis states
    g = basis(2, 0)  # ground
    e = basis(2, 1)  # excited

    # Define the Hamiltonian:
    # H0 = 0.5 * omega * sz (the base energy splitting)
    # H_drive = 0.5 * Omega_Rabi * sx * cos(omega_drive * t)
    H0 = 0.5 * omega * sz
    H_drive = [0.5 * Omega_Rabi * sx, 'cos(omega_drive * t)']
    H = [H0, H_drive]
    
    # No collapse operators: we treat this as a closed quantum system
    c_ops = []
    
    # Expectation operators for ground and excited states
    e_ops = [g*g.dag(), e*e.dag()]
    
    # Initial state: all population in ground state
    psi0 = g

    # Solve the time-dependent Schrödinger equation
    args = {'omega_drive': omega_drive}
    result = mesolve(H, psi0, tlist, c_ops, e_ops, args=args)

    # result.expect[0] -> population in ground state
    # result.expect[1] -> population in excited state
    return result.expect[0], result.expect[1]

def main():
    # ------------------------------
    # Simulation parameters
    # ------------------------------
    omega_CH = 1.0 * 2*np.pi   # "bond frequency" for C-H (arbitrary)
    omega_CF = 1.5 * 2*np.pi   # "bond frequency" for C-F (stronger bond)
    
    # Driving (probe) frequency and amplitude
    omega_drive = 1.0 * 2*np.pi
    Omega_Rabi = 0.1 * 2*np.pi
    
    # Time array for simulations
    tlist = np.linspace(0, 50, 100)
    
    # ------------------------------
    # Run simulations
    # ------------------------------
    pop_g_CH, pop_e_CH = simulate_bond(omega_CH, Omega_Rabi, omega_drive, tlist)
    pop_g_CF, pop_e_CF = simulate_bond(omega_CF, Omega_Rabi, omega_drive, tlist)
    
    # ------------------------------
    # Plot results
    # ------------------------------
    plt.figure(figsize=(8,5))
    plt.plot(tlist, pop_e_CH, label='Excited-State (C–H)')
    plt.plot(tlist, pop_e_CF, label='Excited-State (C–F)')
    
    plt.xlabel('Time (arb. units)')
    plt.ylabel('Excited-State Population')
    plt.title('Comparison of Toy Two-Level Bond Dynamics\n(C–H vs. C–F)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
