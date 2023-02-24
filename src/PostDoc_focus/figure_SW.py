import numpy as np
import matplotlib.pyplot as plt
from PyThemes import Beamer_169


L = 3     # taille du domaine (m)
Nx = 2000  # résolution spatiale, nbre point domaine (pas d'espace régulier)
x = np.linspace(0, L, Nx)
dx = x[1]-x[0]
xint = np.linspace(-dx, L + dx, Nx + 1)

hc = 0.5     # hauteur colonne (en m)
lc = .5     # largeur colonne (en m)

# bosse
hb = 0.1    # hauteur bosse guassienne topographie
sigb = .1   # Largeur bosse guassienne topographie
xb = 1.5     # position bosse guassienne topographie
Bint = hb*np.exp(-(xint + dx/2 - xb)**2/sigb**2)
B = (Bint[1:] + Bint[:-1])/2


DATA = np.load('results.npy')

indexes = [0, 100, 200, 300, -1]
colors = plt.cm.Blues(np.linspace(0.2, 0.8, len(indexes)))[::-1]

fig, ax = plt.subplots(1, 1, constrained_layout=True,
                       figsize=(Beamer_169.fig_width, 0.3*Beamer_169.fig_width))

ax.plot(x/lc, B/hc, 'k', lw=2)
for i, c in zip(indexes, colors):
    mask = (DATA[i][0, :] - B) > 0.001
    ax.plot(x[mask]/lc, DATA[i][0, :][mask]/hc, color=c)

ax.set_xlabel('$L/L_{0}$')
ax.set_ylabel('$H/H_{0}$')
ax.set_xlim(0, 6)
ax.set_ylim(bottom=0)
plt.savefig('SW_figure.svg')
# plt.show()
