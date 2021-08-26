import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import scipy.fftpack
from scipy import signal

# Importing the data from the file
data=pd.read_csv('Prueba4_D128.csv')
# Data set length or sample size
n=len(data)
# Spacing
dt=1.0/(n)


window=pd.DataFrame(signal.windows.blackmanharris(n))
dwd=window*data
data=dwd
x=np.linspace(0.0, n*dt, n)

# y=data[data[:]>600]
# y.dropna(inplace=True)
print(data)

# Example 1
xf=np.linspace(0.0, 1.0//(2.0*dt), n//2)
yf=np.fft.fft(data)


fig, ax= plt.subplots(2,1)
ax[0].plot(xf, 2.0/n * np.abs(yf[:n//2]), 'g')
ax[1].plot(x,data, 'r')
# ax[0].plot(, , 'o')

ax[0].set_xlabel('f')
ax[0].set_ylabel('dB')
ax[0].set_title('Transformada')

ax[1].set_xlabel('t')
ax[1].set_ylabel('f(t)')
ax[1].set_title('Onda de entrada')

plt.tight_layout()
plt.show()

# Example 2
# t=np.arange(256)
# sp=np.fft.fft(data)
# freq=np.fft.fftfreq(data)
# plt.plot(freq, sp.real, freq, sp.imag)
# plt.show()
