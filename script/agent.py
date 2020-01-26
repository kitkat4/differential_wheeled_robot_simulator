

class Agent:
    def __init__(self, nu, omega):
        self.nu_ = nu
        self.omega_ = omega

    def decide(self, observation=None):
        return self.nu_, self.omega_

