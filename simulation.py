import numpy as np

def compute_acceleration(positions, masses):
    G = 1  # Gravitational constant (arbitrary units)
    num_bodies = len(masses)
    accelerations = np.zeros_like(positions)
    
    for i in range(num_bodies):
        for j in range(num_bodies):
            if i != j:
                r = positions[j] - positions[i]
                distance = np.linalg.norm(r)
                accelerations[i] += G * masses[j] * r / distance**3
    
    return accelerations

def simulate(masses, initial_positions, initial_velocities, time_step, num_steps):
    positions = np.zeros((num_steps, len(masses), 2))
    velocities = initial_velocities.copy()
    positions[0] = initial_positions

    for t in range(1, num_steps):
        accelerations = compute_acceleration(positions[t-1], masses)
        velocities += accelerations * time_step
        positions[t] = positions[t-1] + velocities * time_step

    return positions
