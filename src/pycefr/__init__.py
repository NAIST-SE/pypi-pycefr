#   -------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   -------------------------------------------------------------
"""Python Package Template"""
from __future__ import annotations

__version__ = "0.0.5"

import os

location = os.path.dirname(os.path.realpath(__file__))
my_data = os.path.join(location, 'data','dicc.txt')
print(my_data)

with open(my_data) as dict_file:
# my_data_object = fin.readlines()
# with open('dicc.txt', 'r') as dict_file:
    """ Read file with levels """
    dict_text = dict_file.read()
    dictLevel = eval(dict_text)