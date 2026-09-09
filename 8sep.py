import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# -----------------------------
# SETTINGS
# -----------------------------
N = 6000
STEPS = 1000
DT = 0.035
G = 1.0

np.random.seed(42)

# -----------------------------
# CREATE A GALAXY
# -----------------------------

# Distance of each star from center
r = np.random.power(2.0, N) * 20 + 0.5

# Random angle
theta = np.random.uniform(0, 2 * np.pi, N)

# Slight vertical thickness
z = np.random.normal(0, 0.15, N)

# Convert polar -> Cartesian
x = r * np.cos(theta)
y = r * np.sin(theta)

# -----------------------------
# CENTRAL MASS
# -----------------------------

central_mass = 900

# Circular orbital velocity:
# v = sqrt(GM/r)
speed = np.sqrt(G * central_mass / r)

# Tangential velocity
vx = -speed * np.sin(theta)
vy = speed * np.cos(theta)

# Add tiny randomness
vx += np.random.normal(0, 0.08, N)
vy += np.random.normal(0, 0.08, N)

# -----------------------------
# FIGURE
# -----------------------------

fig, ax = plt.subplots(figsize=(10, 10))

ax.set_facecolor("black")
fig.patch.set_facecolor("black")

ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

ax.set_xticks([])
ax.set_yticks([])

stars = ax.scatter(
    x,
    y,
    s=np.random.uniform(0.1, 2.5, N),
    alpha=0.7
)

# Central black hole
ax.scatter(
    [0],
    [0],
    s=120,
    color="black",
    edgecolors="white",
    linewidths=0.5
)

# -----------------------------
# PHYSICS
# -----------------------------

def update(frame):

    global x, y, vx, vy

    # Distance from center
    radius = np.sqrt(x**2 + y**2)

    # Prevent division by zero
    radius = np.maximum(radius, 0.3)

    # Gravitational acceleration
    acceleration = -G * central_mass / radius**3

    ax_force_x = acceleration * x
    ax_force_y = acceleration * y

    # -------------------------
    # Update velocity
    # -------------------------

    vx += ax_force_x * DT
    vy += ax_force_y * DT

    # -------------------------
    # Add tiny "galactic drag"
    # -------------------------
    #
    # This makes the particles
    # slowly organize into arms.

    vx *= 0.9997
    vy *= 0.9997

    # -------------------------
    # Update position
    # -------------------------

    x += vx * DT
    y += vy * DT

    # -------------------------
    # Spiral distortion
    # -------------------------

    angle = np.arctan2(y, x)

    spiral = 0.0008 * radius

    vx += -np.sin(angle) * spiral
    vy +=  np.cos(angle) * spiral

    # -------------------------
    # Update screen
    # -------------------------

    stars.set_offsets(np.column_stack((x, y)))

    return stars,


# -----------------------------
# ANIMATION
# -----------------------------

animation = FuncAnimation(
    fig,
    update,
    frames=STEPS,
    interval=20,
    blit=True
)

plt.show()