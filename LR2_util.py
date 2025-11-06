import numpy
import matplotlib.pyplot as plt

# NUMERICAL IMPLEMENTATION OF OPTICAL FOURIER TRANSFORM
# BASED ON FAST FOURIER TRANSFORM

N = 150
M = 256
A = 5
b_tilda = N * N / (4 * A * M)
s = 1
p = 1


def discretize_1d(n, a, b, fun):
    h = (b - a) / n
    return h, numpy.array([fun(a + i * h) for i in range(n)])

def discretize_2d(n, a, b, fun):
    h = (b - a) / n
    return h, numpy.array([[fun(a + i * h, a + j * h) for j in range(n)] for i in range(n)])

def simpson_integrate(a, b, n, fun, params):
    t = a
    S = 0
    h = (b - a) / n
    while t < b:
        S += fun(t + h, params) + 4 * fun(t + h / 2, params) + fun(t, params)
        t += h
    S *= h / 6
    return S


def gauss_1d(x):
    return numpy.exp(- s * x ** 2)


def gauss_2d(x, y):
    return numpy.exp(- s * x**2 - p * y**2)


def input_fun_1d(x):
    return (4 * x**2 - 2) * numpy.exp(- x**2 / 2)


def input_fun_2d(x, y):
    return (4 * x**2 - 2)*(4 * y**2 - 2) * \
           numpy.exp(- x**2 / 2) * numpy.exp(- y**2 / 2)


def analytical_fourier_1d(u):
    return -numpy.sqrt(2 * numpy.pi) * (16 * (numpy.pi**2) * u**2 - 2) *\
           numpy.exp(-2 * (numpy.pi**2) * u**2)


def analytical_fourier_2d(u, v):
    return 2 * numpy.pi * (16 * numpy.pi**2 * u**2 - 2) * (16 * numpy.pi**2 * v**2 - 2) *\
           numpy.exp(-2 * numpy.pi**2 * u**2 - 2 * numpy.pi**2 * v**2)


# Finite Fourier Transform based on Fast Fourier Transform
# f - vector of the input function
# hx - discretization step of the returned array of spectra
def fft_1d(f, hx):
    # дополнение нулями, разбиение на две части и их обмен
    f_zeros = numpy.append(f[N//2:], numpy.zeros(M - N))
    f_zeros = numpy.append(f_zeros, f[:N//2])
    # БПФ
    F = numpy.fft.fft(f_zeros, M)
    # разбиение F на две половины, обмен местами и вырезание центральной части из получившегося вектора
    return hx * numpy.append(F[M - N//2:], F[:N//2])

# Fast Fourier Transform 2D
def fft_2d(f, hx):
    F = numpy.zeros((N, N), dtype=complex)
    temp = numpy.zeros((N, N), dtype=complex)
    # strings
    for i in range(N):
        temp[i] = fft_1d(f[i], hx)
    temp = temp.T
    # columns
    for i in range(N):
        F[i] = fft_1d(temp[i], hx)
    return F.T


def fourier_transform_1d(fun):
    def in_integral(x, u):
        return fun(x)*numpy.exp(- 2 * numpy.pi * 1j * u * x)
    h = 2 * b_tilda / N
    F = [simpson_integrate(-A, A, N, in_integral, -b_tilda + i * h) for i in range(N)]
    return numpy.array(F)


def plot_1d(x, f, label, f2=None, label2=None):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, numpy.abs(f), color='blue', label=label)
    if f2 is not None:
        plt.plot(x, numpy.abs(f2), color='red', label=label2)
    plt.title("Amplitude")
    plt.legend()
    plt.grid()
    plt.subplot(1, 2, 2)
    plt.plot(x, numpy.angle(f), color='blue', label=label)
    if f2 is not None:
        plt.plot(x, numpy.angle(f2), color='red', label=label2)
    plt.title("Phase")
    plt.grid()
    plt.legend()
    plt.show()


def plot_2d_array(x, y, z, name):
    mycmap = plt.get_cmap("plasma")
    plt.set_cmap(mycmap)
    extent = [x[0], x[-1], y[0], y[-1]]
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(numpy.abs(z), extent=extent)
    plt.title("Amplitude " + name)
    plt.colorbar()
    plt.subplot(1, 2, 2)
    plt.imshow(numpy.angle(z), extent=extent, vmin=-numpy.pi, vmax=numpy.pi)
    plt.title("Phase " + name)
    plt.colorbar()
    plt.show()


def plot_2d(x, y, name, fun):
    z = numpy.zeros((len(x), len(y)))
    i = 0
    for val_x in x:
        j = 0
        for val_y in y:
            z[i][j] = fun(val_x, val_y)
            j = j + 1
        i = i + 1
    plot_2d_array(x, y, z, name)
