import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

class Robot:
    
    def __init__(self, name, pose, radius, color="black", agent=None):
        
        self.name_ = name
        self.pose_ = pose
        self.poses_ = []
        self.color_ = color
        self.radius_ = radius
        self.agent_ = agent

    @classmethod
    def state_transition(cls, nu, omega, time, pose):

        th = pose[2]
        if math.fabs(omega) < 1e-10:
            return pose + \
                np.array([nu * math.cos(th), nu * math.sin(th), omega]) * time
        else:
            return pose + \
                np.array([nu * ( math.sin(th + omega * time) - math.sin(th)) / omega,
                          nu * (-math.cos(th + omega * time) + math.cos(th)) / omega,
                          omega * time])


    def draw(self, ax, elems):

        x, y, th = self.pose_
        xn = x + self.radius_ * math.cos(th)
        yn = y + self.radius_ * math.sin(th)

        elems += ax.plot([x, xn], [y, yn], color=self.color_)
        c = patches.Circle(xy=(x, y), radius=self.radius_, fill=False, color=self.color_)
        elems.append(ax.add_patch(c))

        self.poses_.append(self.pose_)
        elems += ax.plot([e[0] for e in self.poses_], [e[1] for e in self.poses_],\
                         linewidth=0.5, color=self.color_)

    def one_step(self, time_interval):
        if not self.agent_:
            return
        else:
            nu, omega = self.agent_.decide()
            self.pose_ = self.state_transition(nu, omega, time_interval, self.pose_)

