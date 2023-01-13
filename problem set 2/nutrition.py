# Take user input case insensitively
f = input("Input Fruit: ").lower()
# Dictionary of accepted fruits and their calories
fruits = {
    'apple':130,
    'banana':110,
    'avocado':50,
    'cantaloupe':50,
    'grapefruit':60,
    'grapes':90,
    'melon':50,
    'kiwi':90,
    'lemon':15,
    'lime':20,
    'nectarine':60,
    'orange':80,
    'peach':60,
    'pear':100,
    'pineapple':50,
    'plums':70,
    'strawberries':50,
    'cherries':100,
    'tangerine':50,
    'watermelon':80,
    }
# If fruit in accepted fruits print out calories else reject input
if f in fruits:
    print(f"Calories:{fruits[f]}")
else:
    print("Fruit not in database.")
