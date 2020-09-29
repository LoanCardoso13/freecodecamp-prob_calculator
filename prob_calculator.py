import random
# I believe this code can be perfected with the 'list comprehension' technique 
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
    M = 0
    for i in range(num_experiments):
        count = 0
        taken = hat.draw_balls(num_balls_drawn)
        for color in expected_balls:
            if taken.count(color) >= expected_balls[color]:
                count += 1
        if count == len(expected_balls):
            M += 1
        hat.return_balls(taken)
    probability = M / num_experiments
    return probability

