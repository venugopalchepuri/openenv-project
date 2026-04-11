from env.graders import (
    grade_easy,
    grade_medium,
    grade_hard,
    grade_expert,
    grade_insane,
)
class GridEnv:
    def __init__(self, size=5, goal=None):
        self.size = size
        self.max_steps = 30
        self.custom_goal = goal
        self.reset()

    def reset(self):
        self.agent = [0, 0]

        # allow dynamic goal (for tasks)
        if self.custom_goal:
            self.goal = self.custom_goal
        else:
            self.goal = [self.size - 1, self.size - 1]

        self.obstacles = [[1, 1], [2, 2]]
        self.steps = 0
        return self.state()

    def state(self):
        return {
            "agent": self.agent,
            "goal": self.goal,
            "obstacles": self.obstacles,
            "steps": self.steps
        }

    def step(self, action):
        self.steps += 1

        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        dx, dy = moves.get(action, (0, 0))

        new_pos = [
            max(0, min(self.size - 1, self.agent[0] + dx)),
            max(0, min(self.size - 1, self.agent[1] + dy))
        ]

        # avoid obstacles
        if new_pos not in self.obstacles:
            self.agent = new_pos

        done = self.agent == self.goal or self.steps >= self.max_steps

        reward = grade_task(self.state())

        return self.state(), reward, done