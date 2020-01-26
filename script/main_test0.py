#!/usr/bin/env python3
#coding: utf-8

import world
import robot
import agent

import numpy as np

import math
import sys

if __name__ == "__main__":

    world = world.World(10, 0.1)

    agent1 = agent.Agent(0.2, 0.0)
    agent2 = agent.Agent(0.2, 10.0 * math.pi / 180.0)

    robot1 = robot.Robot("robot_1", np.array([0.0, 0.0, 0.0]), 0.2, "black", agent1)

    robot2 = robot.Robot("robot_2", np.array([1.0, 2.0, math.pi / 2.0]), 0.2, "red", agent2)

    world.add_robot(robot1)
    world.add_robot(robot2)

    world.draw()
    
