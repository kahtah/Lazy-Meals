# Tired of having to plan your meals?
# Use this by clearing out the text between the ' ' below with your personal favorites to customize!

import random

Breakfast = [
    'Oatmeal ',
    'Eggs and toast ',

]

Lunch = [
    'ramen',
    'peanut butter and jelly sandwich',
    'rice and veggies',
]

Dinner = [
    "spaghetti",
    "mac n cheese",
    "chicken and rice",
    "tofu and rice",
    "tofu and rice",
    "chickpea stew",
]

selected = random.choice(Breakfast)

selected2 = random.choice(Lunch)

selected3 = random.choice(Dinner)

print(selected + 'is your breakfast today. ')
print('Lunch today is ' + selected2 + '.')
print('Dinner shall be ' + selected3 + '.')