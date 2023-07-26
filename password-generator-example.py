# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:50:10 2022

@author: Martin
"""

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"

upper_case =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

number = "0123456789"

symbols = "!@#$%^&/"

user_for = lower_case + upper_case + number + symbols
lenght_pass = 10

password = "".join(random.sample(user_for, lenght_pass))

print("Tu contraseña es: ", password)
