import copy
import random
from typing import Dict

#Picking balls from a hat; some estimated probabilities:

#Hat class represents a hat, with a number of balls of various colors.
#The draw method randomly picks a number of the balls, without replacement.

class Hat:
    def __init__(self, **kwargs: Dict[str, int]):
        self.kwargs = kwargs
        self.contents = []
        self.size = 0
        for key, value in kwargs.items():
            while value > 0:
                self.contents.append(key)
                value -= 1
                self.size += 1
    def draw(self, no_of_draws=int):
        if no_of_draws >= self.size:
            result = []
            k = self.size
            for i in range(0,k):
                result.append(self.contents.pop(0))
            return result
        result = []
        for i in range(0, no_of_draws):
            draw_number = random.randint(0, len(self.contents)-1 )
            result.append(self.contents.pop(draw_number))

        return result
    


hat1 = Hat( red = 5, blue = 3 )
#print(hat1.contents, hat1.size)
print(hat1.draw(8))

#The experiment function answers the following question with an approximation
#based on a Monte Carlo simulation of picking balls from a hat:

#Given a hat and its contents, an assortment of colored balls, what is
#the probability that for each color of ball a sufficient quantity of said
#balls are drawn in n draws?

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for i in range(0, num_experiments):
        hatcopy = Hat( **hat.kwargs )
        current_draw = hatcopy.draw(num_balls_drawn)
        all_color_match = True
        for key, value in expected_balls.items():
            if value > current_draw.count(key):
                all_color_match =False
        if all_color_match:
            counter += 1
    return counter / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)