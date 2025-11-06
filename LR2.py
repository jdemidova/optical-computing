from LR2_util import *

if __name__ == '__main__':
    x_f = numpy.linspace(-A, A, N, endpoint=False)
    x_F = numpy.linspace(-b_tilda, b_tilda, N, endpoint=False)

    # 1D case

    h, array = discretize_1d(N, -A, A, gauss_1d)
    # исходный пучок Гаусса
    plot_1d(x_f, array, 'exp(-s*x^2)')

    # БПФ пучка Гаусса
    fft_F = fft_1d(array, h)
    plot_1d(x_F, fft_F, 'БПФ[exp(-s*x^2)]')

    # Фурье-преобразование через интеграл для пучка Гаусса
    num_F = fourier_transform_1d(gauss_1d)
    # БПФ и интегральный метод на одном графике
    plot_1d(x_F, fft_F, 'БПФ[exp(-s*x^2)]', num_F, 'Числ.Фурье[exp(-s*x^2)]')

    h, array = discretize_1d(N, -A, A, input_fun_1d)
    plot_1d(x_f, array, '(4*x^2-2)*exp(-x^2/2)')
    # БПФ для входной функции
    fft = fft_1d(array, h)
    # только БПФ на графике
    plot_1d(x_F, fft, 'БПФ[function]')

    # БПФ и аналитическое решение на одном графике
    plot_1d(x_F, fft, 'БПФ[function]', [analytical_fourier_1d(x) for x in x_F], 'Аналит.Фурье[function]')

    # Двумерный случай

    h, array2 = discretize_2d(N, -A, A, gauss_2d)
    plot_2d(x_f, x_f, name="exp(-s*x^2-p*y^2)", fun=gauss_2d)

    fft2 = fft_2d(array2, h)
    plot_2d_array(x_F, x_F, fft2, name="2D БПФ[gauss(x, y)]")

    h, array2 = discretize_2d(N, -A, A, input_fun_2d)
    plot_2d(x_f, x_f, name="function(x, y)", fun=input_fun_2d)
    fft2 = fft_2d(array2, h)
    plot_2d_array(x_F, x_F, fft2, name="2D БПФ[function(x, y)]")
    analytical = numpy.zeros((N, N))
    for i in range(N):
        for j in range(N):
            analytical[i][j] = analytical_fourier_2d(x_F[i], x_F[j])
    plot_2d_array(x_F, x_F, analytical, name="Аналит.Фурье[function]")
