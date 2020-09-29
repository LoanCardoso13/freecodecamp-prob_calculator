import random

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = []
        for ball_color in self.kwargs:
            self.contents += [ ball_color for balls in range(self.kwargs[ball_color]) ]

    def draw_balls(self, n):
        if n > len(self.contents):
            n = len(self.contents)
        balls_drawn = []
        for _ in range(n):
            balls_drawn.append(self.contents.pop(random.randrange(0, len(self.contents))))
        return balls_drawn

    def return_balls(self, balls):
        for ball in balls:
            self.contents.append(ball)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0    # Variable to count number of positive experiments
             # Perform experiment num_experiments times: 
    for _ in range(num_experiments):
        count = 0    # Count positive result for single color within experiment 
        taken = hat.draw_balls(num_balls_drawn)    # Randomly taken from Hat.
        for color in expected_balls:
            if taken.count(color) >= expected_balls[color]:
                count += 1
        if count == len(expected_balls):           # Positive experiment is 
            M += 1                                 # when all single color re-
        hat.return_balls(taken)                    # sults were positive. Return  
    probability = M / num_experiments              # balls to Hat after  
    return probability                             # experiment. 

