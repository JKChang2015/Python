# random_walk
# Created by JKChang
# 22/01/2018, 13:46
# Tag:
# Description:

from random import choice


class RandomWalk():
    '''random walk for any directions'''

    def __init__(self, num_points):
        self.num_points = num_points

        # starting point
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''fill all the walk positions'''
        while len(self.x_values) < self.num_points:
            # directions and distances
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # don't allow stay in the same place
            if x_step == 0 and y_step == 0:
                continue

            # fill next x_value and y_value
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
