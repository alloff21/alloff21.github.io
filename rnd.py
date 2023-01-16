#!/usr/bin/env python3

import cgi
from random import randint

def generate_random_number(x, y):
    our_form = cgi.FieldStorage()
    x = int(our_form.getfirst("x","0"))
    y = int(our_form.getfirst("y","0"))
    z = randint(x, y)
    return z
