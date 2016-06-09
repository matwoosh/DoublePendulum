import numpy as np
import matplotlib.animation as animation


class Plot:
    def __init__(self, figure, data):
        self.figure = figure
        self.data = data.get_data()
        self.init_plot()

    def init_plot(self):
        ax = self.figure.add_subplot(111, autoscale_on=False, xlim=(-5, 5), ylim=(-5, 5))
        ax.grid()
        self.line, = ax.plot([], [], 'o-', lw=2)
        self.time_template = 'time = %.1fs'
        self.time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

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
                                      interval=25, blit=True, init_func=self.init, repeat=False)
        canvas.draw()

    def set_data(self, new_data):
        self.data = new_data




