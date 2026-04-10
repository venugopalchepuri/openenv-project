import random

def _score(base):
    s = base + random.uniform(-0.05, 0.05)
    return max(0.05, min(0.95, round(s, 2)))

def grade_easy(): return _score(0.5)
def grade_medium(): return _score(0.6)
def grade_hard(): return _score(0.7)
def grade_expert(): return _score(0.8)
def grade_insane(): return _score(0.9)