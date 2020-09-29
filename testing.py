from prob_calculator import Hat, experiment

hat1 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)