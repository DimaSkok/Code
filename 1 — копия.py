import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7, 7))

origin = np.zeros(6)

vectors = np.vstack((np.eye(2), [[-0.7, -0.7]], [[0.7, 0.8]], [[0.95, 0.2]], [[-0.2, -0.7]]))
qkeys = ["y", "z", "x", "$M$", "$\\pi$", ""]
qkeys_x, qkeys_y = [0.95, 0, -0.68, 0.68, 0.92, -0.2], [0, 0.95, -0.68, 0.78, 0.19, -0.7]
labelposes = ['N', 'W', 'S', 'N', 'N', 'S']

for o, u, v, q_x, q_y, q_key, lp in zip(origin, vectors[:, 0], vectors[:, 1],
                                           qkeys_x, qkeys_y, qkeys, labelposes):
    q = ax.quiver(o, o, u, v, angles='xy', scale_units='xy', scale=1,
                  headaxislength=0 if q_key=='' else 4.5, headlength=0 if q_key=='' else 5)
    ax.quiverkey(q, q_x, q_y, 0, q_key, coordinates='data', fontproperties={'size': 20}, labelpos=lp)

ax.quiverkey(q, 0, 0.05, 0.05, "$O$", coordinates='data', fontproperties={'size': 20}, labelpos='W')

ax.add_patch(plt.Circle((0, 0), 0.8, color='k', fill=False, lw=2))
ax.add_patch(patches.Arc([-0.38, 0.92], 3., 3., 0, theta1=263, theta2=322, lw=2))
ax.add_patch(patches.Arc([-1.1, 0.6], 3., 3., 30, theta1=269, theta2=333.5, lw=2))

x, y = [-0.16, 0.3, 0.39], [-0.56, 0.07, 0.45]
ax.scatter(x, y, s=50, c='k')

ax.quiverkey(q, -0.35, -0.58, 0, "$\\Omega$", coordinates='data', fontproperties={'size': 24}, labelpos='N')
ax.quiverkey(q, 0.11, -0.5, 0, "$i$", coordinates='data', fontproperties={'size': 20}, labelpos='N')
ax.quiverkey(q, 0.198, -0.15, 0, "$\\omega$", coordinates='data', fontproperties={'size': 20}, labelpos='W')
ax.quiverkey(q, 0.355, 0.23, 0, "$\\upsilon$", coordinates='data', fontproperties={'size': 20}, labelpos='W')

lim = 1
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)
plt.axis('off');