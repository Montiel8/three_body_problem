import tkinter as tk
from simulation import simulate
from visualization import visualize
import numpy as np

def run_simulation():
    masses = [1, 1, 1]
    initial_positions = np.array([[0, 1], [-1, -1], [1, -1]])
    initial_velocities = np.array([[0.5, 0], [0, 0.5], [-0.5, -0.5]])
    time_step = 0.01
    num_steps = 1000

    positions = simulate(masses, initial_positions, initial_velocities, time_step, num_steps)
    visualize(positions)

root = tk.Tk()
root.title("Three-Body Problem Simulator")

run_button = tk.Button(root, text="Run Simulation", command=run_simulation)
run_button.pack()

root.mainloop()
