# world_population
# Created by JKChang
# 22/01/2018, 20:40
# Tag:
# Description:world population

import json
import math
import operator
from itertools import islice

from pygal.style import LightColorizedStyle
from pygal.style import RotateStyle
from pygal_maps_world.maps import World

from RD_Club.Pro2.country_codes import get_country_code


def chunks(data, SIZE=10000):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k: data[k] for k in islice(it, SIZE)}


def millify(n):
    millnames = ['', ' K', ' M', ' B', ' T']
    n = float(n)
    millidx = max(0, min(len(millnames) - 1, int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))
    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])


filename = 'resources/population.json'
with open(filename) as file:
    pop_data = json.load(file)

population_dict = {}

for pop_dict in pop_data:
    if pop_dict['Year'] == 2016:
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            population_dict[code] = population

sorted_pop = dict(sorted(population_dict.items(), key=operator.itemgetter(1)))
res = []

for item in chunks(sorted_pop, len(sorted_pop) // 10):
    res.append(item)

map_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(wm_style=map_style)
wm.title = 'World Population in 2016'
temp = 0
for group in res[:-1]:
    mean = millify(int(sum(group.values()) / len(group)))
    title = '%s - %s' % (temp, mean)
    wm.add(str(title), group)
    temp = mean
wm.add('> %s' % temp, res[-1])
wm.render_to_file('resources/world_population 2016.svg')
