import numpy as np
from numpy import sin, cos
import scipy.integrate as integrate


class Data:
    def __init__(self, G, L1, L2, M1, M2, th1, th2, time):
        self.G = G
        self.L1 = L1
        self.L2 = L2
        self.M1 = M1
        self.M2 = M2
        self.th1 = th1
        self.th2 = th2
        self.animation_time = time

    def derivs(self, state, t):

        dydx = np.zeros_like(state)
        dydx[0] = state[1]

        del_ = state[2] - state[0]
        den1 = (self.M1 + self.M2)*self.L1 - self.M2*self.L1*cos(del_)*cos(del_)
        dydx[1] = (self.M2*self.L1*state[1]*state[1]*sin(del_)*cos(del_) +
                   self.M2*self.G*sin(state[2])*cos(del_) +
                   self.M2*self.L2*state[3]*state[3]*sin(del_) -
                   (self.M1 + self.M2)*self.G*sin(state[0]))/den1

        dydx[2] = state[3]

        den2 = (self.L2/self.L1)*den1
        dydx[3] = (-self.M2*self.L2*state[3]*state[3]*sin(del_)*cos(del_) +
                   (self.M1 + self.M2)*self.G*sin(state[0])*cos(del_) -
                   (self.M1 + self.M2)*self.L1*state[1]*state[1]*sin(del_) -
                   (self.M1 + self.M2)*self.G*sin(state[2]))/den2

        return dydx

    def get_data(self):
        # create a time array from 0..100 sampled at 0.05 second steps
        dt = 0.05
        t = np.arange(0.0, self.animation_time, dt)

        # th1 and th2 are the initial angles (degrees)
        # w10 and w20 are the initial angular velocities (degrees per second)
        w1 = 0.0
        w2 = 0.0

        # initial state
        state = np.radians([self.th1, w1, self.th2, w2])

        # integrate your ODE using scipy.integrate.
        y = integrate.odeint(self.derivs, state, t)

        x1 = self.L1*sin(y[:, 0])
        y1 = -self.L1*cos(y[:, 0])

        x2 = self.L2*sin(y[:, 2]) + x1
        y2 = -self.L2*cos(y[:, 2]) + y1
        return x1, y1, x2, y2, y, dt

    def set_data(self, G, L1, L2, M1, M2, th1, th2, time):
        self.G = G
        self.L1 = L1
        self.L2 = L2
        self.M1 = M1
        self.M2 = M2
        self.th1 = th1
        self.th2 = th2
        self.animation_time = time
