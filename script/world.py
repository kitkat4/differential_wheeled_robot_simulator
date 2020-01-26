import robot

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

class World:

    def __init__(self, time_span, time_interval):
        self.robots_ = []
        self.time_span_ = time_span
        self.time_interval_ = time_interval
        
    def add_robot(self, name, pose, radius, color="black"):
        
        self.robots_.append(robot.Robot(name, pose, radius, color))

    def add_robot(self, robot):
        
        self.robots_.append(robot)

    def draw(self):

        fig = plt.figure(figsize=(8, 8))

        ax = fig.add_subplot(111)
        ax.set_aspect("equal")
        ax.set_xlim((-5, 5))
        ax.set_ylim((-5, 5))
        ax.set_xlabel("X", fontsize=20)
        ax.set_ylabel("Y", fontsize=20)

        elems = []

        self.ani = anm.FuncAnimation(fig, self.one_step, fargs=(elems, ax), \
                                     frames=int(self.time_span_ / self.time_interval_) + 1,
                                     interval=int(self.time_interval_ * 1000), repeat=False)

        plt.show()

    def one_step(self, i, elems, ax):
        
        while elems:
            elems.pop().remove()

        time_string = "t = %.2f[s]" % (self.time_interval_ * i)
        elems.append(ax.text(-4.4, 4.5, time_string, fontsize=10))

        for robot in self.robots_:
            robot.draw(ax, elems)
            if hasattr(robot, "one_step"):
                robot.one_step(self.time_interval_)

        
        
        
        
