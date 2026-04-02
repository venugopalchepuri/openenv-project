class GridEnv:
    def __init__(self, size=5):
        self.size = size
        self.reset()

    def reset(self):
        self.agent = [0, 0]
        self.goal = [self.size - 1, self.size - 1]
        return self.state()

    def state(self):
        return {"agent": self.agent, "goal": self.goal}

    def step(self, action):
        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        dx, dy = moves.get(action, (0, 0))
        self.agent[0] = max(0, min(self.size - 1, self.agent[0] + dx))
        self.agent[1] = max(0, min(self.size - 1, self.agent[1] + dy))

        done = self.agent == self.goal
        reward = 1.0 if done else -0.01

        return self.state(), reward, done