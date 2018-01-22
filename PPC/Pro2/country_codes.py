# country_codes
# Created by JKChang
# 22/01/2018, 21:01
# Tag:
# Description: 

from pygal_maps_world.maps import COUNTRIES


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
