import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import axes3d, Axes3D

# Numerical integration

# Input Signal
def f(x, beta):
    return cmath.exp(1j * x * beta)

# Kernel K(ksi, x)
def K(x, ksi, alpha):
    return math.pow(x, alpha * ksi - 1)


# f under integral
def function(x, ksi, alpha, beta):
    return K(x, ksi, alpha) * f(x, beta)


# Integral via rectangles
def integral(a, b, n, ksi, alpha, beta):
    c = a
    res = 0
    h_x = (b - a) / (n - 1)
    while c < b:
        res += function(c + h_x, ksi, alpha, beta)
        c += h_x
    res *= h_x
    return res


# Amplitude and Phase
def plots_A_and_phi(x, y, function_name, function_args):
    amplitude = [abs(_) for _ in y]
    phase = [cmath.phase(_) for _ in y]
    plt.figure()
    plt.subplots_adjust(bottom=0.2)
    plt.plot(x, amplitude)
    plt.xlabel(function_args)
    plt.ylabel('Amplitude')
    plt.title('Amplitude ' + function_name + '(' + function_args + ')')
    plt.grid()
    plt.show()
    plt.figure()
    plt.subplots_adjust(bottom=0.2)
    plt.plot(x, phase)
    plt.xlabel(function_args)
    plt.ylabel('Phase ')
    plt.title('Phase ' + function_name + '(' + function_args + ')')
    plt.grid()
    plt.show()


# Plot of amplitude and phase of output signal
def plots_output_signal(a, b, p, q, m, n, alpha, beta):
    h_ksi = (q - p) / (m - 1)
    X = [p + h_ksi * i for i in range(m)]
    Y = [integral(a, b, n, ksi, alpha, beta) for ksi in X]
    plots_A_and_phi(X, Y, 'F', 'ξ')


# 3D plot of Kernel function
def plot_ker_3D(a, b, p, q, n, m, alpha):
    fig = plt.figure()
    #ax = fig.gca(projection='3d')
    ax = Axes3D(fig)
    h_x = (b - a) / (n - 1)
    h_ksi = (q - p) / (m - 1)
    X = np.arange(a, b, h_x)
    KSI = np.arange(p, q, h_ksi)
    X, KSI = np.meshgrid(X, KSI)
    Z = np.power(X, alpha * KSI - 1.0)
    # Plot the surface.
    mycmap = plt.get_cmap('plasma')
    ax.set_title('K(x, ξ), α = ' + str(alpha))
    ax.set_xlabel('X')
    ax.set_ylabel('ξ')
    surf = ax.plot_surface(X, KSI, Z, cmap=mycmap)
    ax.set_zlim(np.amin(Z), np.amax(Z))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf)
    plt.show()


if __name__ == '__main__':
    n = 1000
    m = 1000
    a = 1.0
    b = 5.0
    p = 0.0
    q = 3.0
    alpha = 3.0
    beta = 0.5
    h_x = (b - a) / (n - 1)
    h_ksi = (q - p) / (m - 1)
    X = [a + h_x * i for i in range(n)]
    Y = [f(x, beta) for x in X]
    KSI = [p + h_ksi * i for i in range(m)]
    plots_A_and_phi(X, Y, 'f', "x, β")
    plots_output_signal(a, b, p, q, m, n, alpha, beta)
    plot_ker_3D(a, b, p, q, n, m, alpha)
