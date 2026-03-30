import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

# Physical constants
g = 9.81  # acceleration due to gravity, in m/s^2
L1 = 1.0  # length of pendulum 1 in m
L2 = 1.0  # length of pendulum 2 in m
m1 = 1.0  # mass of pendulum 1 in kg
m2 = 1.0  # mass of pendulum 2 in kg

# Equations of motion
def equations(t, y):
    θ1, z1, θ2, z2 = y
    c, s = np.cos(θ1-θ2), np.sin(θ1-θ2)
    
    dz1 = (m2*g*np.sin(θ2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
           (m1+m2)*g*np.sin(θ1)) / L1 / (m1 + m2*s**2)
    
    dz2 = ((m1+m2)*(L1*z1**2*s - g*np.sin(θ2) + g*np.sin(θ1)*c) + 
           m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    
    return [z1, dz1, z2, dz2]

# Initial conditions: θ1, dθ1/dt, θ2, dθ2/dt
y0 = [np.pi/2, 0, np.pi/2, 0]

# Time domain
t = np.linspace(0, 10, 500)

# Solve the differential equations
sol = solve_ivp(equations, [t.min(), t.max()], y0, t_eval=t, method='RK45')

# Extract the solutions
θ1, θ2 = sol.y[0], sol.y[2]

# Convert to Cartesian coordinates
x1 = L1 * np.sin(θ1)
y1 = -L1 * np.cos(θ1)
x2 = x1 + L2 * np.sin(θ2)
y2 = y1 - L2 * np.cos(θ2)

fig, ax = plt.subplots()
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
line, = ax.plot([], [], 'o-', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data([0, x1[frame], x2[frame]], [0, y1[frame], y2[frame]])
    return line,

ani = FuncAnimation(fig, update, frames=range(len(t)), init_func=init, blit=True)
plt.show()