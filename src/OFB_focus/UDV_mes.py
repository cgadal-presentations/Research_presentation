import numpy as np
import matplotlib.pyplot as plt
import os

path_data = "/media/cyril/IMFT data/OFB_Colmatage/processing/UDV/release01"
data = np.load(os.path.join(path_data, 'data.npy'), allow_pickle=True).item()

fig, ax = plt.subplots(1, 1, layout='constrained', figsize=(3, 5))
ax.plot(-data['U_av'][0], data['z_interp'], label='u')
# ax.plot(data['U_av'][1], data['z_interp'], label='v')
ax.set_xlabel('Velocity [cm/s]')
ax.set_ylabel('Height [cm]')
ax.set_ylim(0.7, 6)
ax.set_xlim(left=0.02)
# ax.set_yscale('log')
plt.savefig('UDV_mes.svg')
