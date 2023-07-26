# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:20:32 2022

@author: Martin
"""

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = "0123456789"

symbols = "!@#$%^&*/"

use_for = lower_case + upper_case + number + symbols
lenght_for_pass = 10

password = "".join(random.sample(use_for, lenght_for_pass))

print("Tu contraseña es:", password)
 
