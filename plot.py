import numpy as np
from data import get_data
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Plot:
    def __init__(self, figure):
        self.figure = figure
        self.init_plot()

    def init_plot(self):
        ax = self.figure.add_subplot(111, autoscale_on=False, xlim=(-2, 2), ylim=(-2, 2))
        ax.grid()
        self.line, = ax.plot([], [], 'o-', lw=2)
        self.time_template = 'time = %.1fs'
        self.time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
        self.data = get_data()

    def init(self):
        self.line.set_data([], [])
        self.time_text.set_text('')
        return self.line, self.time_text

    def animate(self, i):
        thisx = [0, self.data[0][i], self.data[2][i]]
        thisy = [0, self.data[1][i], self.data[3][i]]

        self.line.set_data(thisx, thisy)
        self.time_text.set_text(self.time_template % (i*self.data[5]))
        return self.line, self.time_text

    def plot_animation(self, canvas):
        ani = animation.FuncAnimation(self.figure, self.animate, np.arange(1, len(self.data[4])),
                                      interval=25, blit=True, init_func=self.init)
        canvas.draw()
    # def plot_function(self, canvas):
    #     plt.clf()
    #     canvas.draw()
    #     x = self.arguments
    #     y = []
    #     for number in x:
    #         y.append(self.function(number, 0))
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.plot(x, y, 'ro')
    #     canvas.draw()
    #
    # def plot_derivative(self, canvas):
    #     x = self.arguments
    #     y = []
    #     if self.deriv_type == DerivativeType.central:
    #         for number in x:
    #             y.append(deriv.central(self.function, number, 1)[0])
    #     elif self.deriv_type == DerivativeType.backward:
    #         for number in x:
    #             y.append(deriv.backward(self.function, number, 1)[0])
    #     elif self.deriv_type == DerivativeType.forward:
    #         for number in x:
    #             y.append(deriv.forward(self.function, number, 1)[0])
    #     else:
    #         print("Fatal error occured!")
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.plot(x, y)
    #     canvas.draw()



