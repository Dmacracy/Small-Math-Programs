import numpy as np
from matplotlib import pyplot as plt

def graph_f(f, x_min, x_max, N, name):
    x = np.arange(x_min, x_max, (x_max - x_min) / N)
    y = f(x)
    plt.plot(x, y, 'b-')
    plt.savefig(name)

def graph_fft(f, x_min, x_max, N, name):
    x = np.arange(x_min, x_max, (x_max - x_min) / N)
    y = f(x)
    y2 = np.fft.fft(y)
    freq = np.fft.fftfreq(x.shape[-1], d=(x_max - x_min) / N)
    plt.clf()
    plt.plot(freq, y2.real, 'g-', freq, y2.imag, 'r-')
    plt.savefig(name)

if __name__ == '__main__':
    graph_f(np.sin, 0.0, 2.0 * np.pi, 1000, "Sine.png")
    graph_fft(np.sin, 0.0, 2.0 * np.pi, 1000, "FourierSine.png")
