from urllib.parse import urlencode
from collections import OrderedDict

def bound_int(value, min_value, max_value):
    return int(min(max(value, min_value), max_value))

def get_adorable_avatar(email, size_pixels, border_radius=50):
    size_pixels = bound_int(size_pixels, 40, 285)
    border_radius = bound_int(border_radius, 0, 50)) # ???
    return f"https://avatars.adorable.io/{size_pixels}/{email}.png"

def get_ui_avatar(name, size_pixels=None, rounded=True):
    """ Generates avatars with initals from names """
    query = OrderedDict()

    query['name'] = "+".join([p.capitalize() for p in name.split()])
    
    # 16 and 512. Default: 64
    if size_pixels is not None:
        query['size'] = str(bound_int(size_pixels, 16, 512))

    query['rounded'] = rounded

    query_string = urlencode(query)
    return f"https://ui-avatars.com/api/?{query_string}"
