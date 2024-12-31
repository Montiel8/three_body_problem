import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def visualize(positions):
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    points, = ax.plot([], [], 'bo')

    def update(frame):
        points.set_data(positions[frame, :, 0], positions[frame, :, 1])
        return points,

    anim = FuncAnimation(fig, update, frames=len(positions), interval=50)
    plt.show()
