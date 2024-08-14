import pandas as pd
import numpy as np

# number 
normal_A1C = 5.6

# string  
define_A1C = 'blood glucose level over past three months'

# list 
A1C_values = [7.5, 5.2, 4.3, 8.8]

# dictionary 
a1c_patientinfo = {
    'patient_name': {
        'name_first': 'Vanessa',
        'name_last': 'Chen',
        'age': 23,
        'A1C_level': 4.7,
        },
    'patient2': {
        'name_first': 'Taylor',
        'name_last': 'Swift',
        'age': 34,
        'A1C_level': 5.5,
        },
    'patient3': {
        'name_first': 'Nick',
        'name_last': 'Jonas',
        'age': 31,  
        'A1C_level': 7.1, 
        },
}

#function and print statements
def A1C_comparison(new_value, old_value):
    print(f'{old_value} is your previous A1C value')
    print(f'{new_value} is your current A1C value')
    if new_value < old_value:
        print ('Your A1C is lower now')
    else:
        print('Your A1C is higher now') 

A1C_comparison(5.4, 7.2)