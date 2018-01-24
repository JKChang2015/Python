# countries
# Created by JKChang
# 22/01/2018, 20:56
# Tag:
# Description: 

from pygal_maps_world.maps import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
