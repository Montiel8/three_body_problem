import numpy as np

def find_stable_orbits(masses, num_trials, time_step, num_steps):
    stable_configs = []
    for _ in range(num_trials):
        positions = np.random.uniform(-5, 5, (len(masses), 2))
        velocities = np.random.uniform(-1, 1, (len(masses), 2))
        trajectories = simulate(masses, positions, velocities, time_step, num_steps)

        # Check stability (e.g., bounded trajectories)
        if np.all(np.linalg.norm(trajectories - trajectories[0], axis=2) < 10):
            stable_configs.append((positions, velocities))
    return stable_configs
