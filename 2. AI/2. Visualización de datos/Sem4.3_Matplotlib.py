import numpy as np

import matplotlib.pyplot as plt

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Line plot
ax1.plot(x, y, 'b-', linewidth=2)
ax1.set_xlabel('X Label')
ax1.set_ylabel('Y Label')
ax1.set_title('Sine Wave')
ax1.grid(True, alpha=0.3)

# Plot 2: Scatter plot
ax2.scatter(x, np.cos(x), c='red', alpha=0.6)
ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_title('Cosine Wave')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
