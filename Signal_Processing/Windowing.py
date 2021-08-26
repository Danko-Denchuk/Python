from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('test_5_analog_signal_adc_a.csv')
print(len(data))
# data = data.drop(data.index[[0, 500]])

data = data.to_numpy()

data = data.ravel()

N = len(data)
n = np.arange(N)
sr = 1/5000000 # Sampling rate
T = 0.0262144 # Period
frequency = n/T

n_oneside = N//2
f_oneside = frequency[:n_oneside]

window = signal.windows.chebwin(N, at=100)
# window = pd.DataFrame(window)

print(data)
print(window)

transformed_window = fft(window)

transformed_data = fft(data)

windowed_data = np.multiply(data, window)

windowed_transformed_data = fft(windowed_data)


# Subplots (Rows, Columns)
fig, ax = plt.subplots(3,2)

ax[0][0].plot(window, 'b')
ax[0][0].set_title("Dolph-Chebyshev window")
ax[0][0].set_ylabel("Amplitude")
ax[0][0].set_xlabel("Sample")


ax[0][1].plot(f_oneside, np.abs(transformed_window[:n_oneside]), 'g')
ax[0][1].set_title("Dolph-Chebyshev transformed")
ax[0][1].set_ylabel("dB")
ax[0][1].set_xlabel("Freq")

ax[1][0].plot(data, 'b')
ax[1][0].set_title("Data")
ax[1][0].set_ylabel("Amplitude")
ax[1][0].set_xlabel("Sample")

ax[1][1].plot(f_oneside, np.abs(transformed_data[:n_oneside]), 'g')
ax[1][1].set_title("Transformed data")
ax[1][1].set_ylabel("dB")
ax[1][1].set_xlabel("Freq")
# ax[2,1].legend(max(transformed_data))

ax[2,0].plot(windowed_data, 'b')
ax[2,0].set_title("Windowed data")
ax[2,0].set_ylabel("Amplitude")
ax[2,0].set_xlabel("Sample")
ax[2,0].legend("200")

ax[2,1].plot(np.abs(windowed_transformed_data[:n_oneside]), 'g')
ax[2,1].set_title("Windowed and transformed data")
ax[2,1].set_ylabel("dB")
ax[2,1].set_xlabel("Freq")
# ax[2,1].legend(max(windowed_transformed_data))

plt.tight_layout()
plt.show()
