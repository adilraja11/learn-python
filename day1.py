## Variables

# Convention snake_case
first_name = 'Muhammad Adil'
last_name = ' Raja Saputra'

# Constant -> All CAPS -> SCREAMING_SNAKE_CASE
APP_NAME = 'devscale-app'

# Start with non-number or _
his_name = 'cahya'
_get_name = 'cahya'

## Data Types

# integer
my_age = 25

# float
my_pi = 3.14

result = my_age + my_pi # the result must be a float data type

# string
your_name = 'Doni'

# Multi Line string
my_address = """
Komplek Dewa Kembar Blok A/8
Cilincing, Jakarta Utara
14130
"""

# Boolean
is_logged_in = False
is_logged_out = True

## Sequence Type

# List -> mutable, non-fixed size
nations = ['France', 'England', 'Russia']
nations.append('Argentina') # Add
nations.remove('France') # Delete

# slicing string -> [start:end:step]
username = 'marsinf@EDTS0012456'
slice_username = username[:7] # Result: marsinf

# Tuple -> immutable, fixed size
coordiante = (0, 1, 2, 5)

# Range
index_range = range(10) # range(0, 10)
my_list = list(index_range) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary -> Key-Value Pairs data
user = {
    "full_name": 'John Doe',
    "NIM": '24060120140000',
    "phone_number": '02134567890'
}

_get_full_name = user['full_name'] # klo key nya gada bakal return traceback error
_get_favorite = user.get("favorite") # return none

## Traversal

# Format
description = """
My name is {full_name}
i live at {city}
"""

description_format = description.format(full_name="John", city="Jakarta")

# play with inputs
first_number = input('Masukkan angka pertama: ')
second_number = input('Masukkan angka kedua: ')

# need to make sure the data type input
print(int(first_number) + int(second_number))



